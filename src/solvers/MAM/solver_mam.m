function [QN,UN,RN,TN,CN,XN] = solver_mam(qn, PH, options)
%[Q,U,R,T,C,X] = SOLVER_MAM(QN, PH, OPTIONS)

%Copyright (c) 2012-2019, Imperial College London
%All rights reserved.
global SCVmam
global BuToolsVerbose;
global BuToolsCheckInput;
global BuToolsCheckPrecision;
%generate local state spaces
I = qn.nnodes;
M = qn.nstations;
K = qn.nclasses;
C = qn.nchains;
N = qn.njobs';
V = cellsum(qn.visits);

QN = zeros(M,K);
UN = zeros(M,K);
RN = zeros(M,K);
TN = zeros(M,K);
CN = zeros(1,K);
XN = zeros(1,K);

lambda = zeros(1,K);
for c=1:C
    inchain = find(qn.chains(c,:));
    lambdas_inchain = qn.rates(qn.refstat(inchain(1)),inchain);
    lambdas_inchain = lambdas_inchain(isfinite(lambdas_inchain));
    lambda(inchain) = sum(lambdas_inchain);
end

chain = zeros(1,K);
for k=1:K
    chain(k) = find(qn.chains(:,k));
end

if M>=2 && qn.nclosedjobs == 0
    %    open queueing system (one node is the external world)
    BuToolsVerbose = false;
    BuToolsCheckInput = false;
    BuToolsCheckPrecision = 1e-14;
    
    pie = {};
    D0 = {};
    for ist=1:M
        switch qn.sched{ist}
            case SchedStrategy.EXT
                TN(ist,:) = qn.rates(ist,:);
                TN(ist,isnan(TN(ist,:)))=0;
            case {SchedStrategy.FCFS, SchedStrategy.HOL, SchedStrategy.PS}
                for k=1:K
                    %                    divide service time by number of servers and put
                    %                    later a surrogate delay server in tandem to compensate
                    PH{ist,k} = map_scale(PH{ist,k}, map_mean(PH{ist,k})/qn.nservers(ist));
                    pie{ist,k} = map_pie(PH{ist,k});
                    D0{ist,k} = PH{ist,k}{1};
                end
        end
    end
    
    it_max = options.iter_max;
    for it=1:it_max
        %it
        %        now estimate arrival processes
        if it == 1
            %            initially form departure processes using scaled service
            DEP = PH;
            for ind=1:M
                for r=1:K
                    ist = qn.nodeToStation(ind);
                    DEP{ind,r} = map_scale(PH{ist,r}, 1 / (lambda(r) * V(ind,r)) );
                end
            end
        end
        
        config = struct();
        config.merge = 'super';
        %config.compress = 'mixture.order1';
        config.compress = 'none';
        config.space_max = 128;
        
        ARV = solver_mam_estflows(qn, DEP, config);
        
        QN_1 = QN;
        
        for ist=1:M
            ind = qn.stationToNode(ist);
            switch qn.nodetype(ind)
                case NodeType.Queue
                    if length(ARV{ind}{1}) > config.space_max
                        fprintf(1,'Arrival process at node %d is now at %d states. Compressing.\n',ind,length(ARV{ind}{1}));
                        ARV{ind} = mmap_compress(ARV{ind});
                    end
                    [Qret{1:K}] = MMAPPH1FCFS({ARV{ind}{[1,3:end]}}, {pie{ist,:}}, {D0{ist,:}}, 'ncMoms', 1);
                    QN(ist,:) = cell2mat(Qret);
                    TN(ist,:) = mmap_lambda(ARV{ind});
            end
            for k=1:K
                UN(ist,k) = TN(ist,k) * map_mean(PH{ist,k});
                %add number of jobs at the surrogate delay server
                QN(ist,k) = QN(ist,k) + TN(ist,k)*(map_mean(PH{ist,k})*qn.nservers(ist)) * (qn.nservers(ist)-1)/qn.nservers(ist);
                RN(ist,k) = QN(ist,k) ./ TN(ist,k);
            end
        end
        
        if it >=3 && max(abs(QN(:)-QN_1(:))./QN_1(:)) < options.iter_tol
            break;
        end
        
        for ist=1:M
            ind = qn.stationToNode(ist);
            switch qn.nodetype(ind)
                case NodeType.Queue
                    [Ret{1:2*K}] = MMAPPH1FCFS({ARV{ind}{[1,3:end]}}, {pie{ist,:}}, {D0{ist,:}}, 'stDistrPH');
                    for r=1:K
                        
                        %obtain response time distribution for class r
                        alpha = Ret{(r-1)*2+1}; T0 = Ret{(r-1)*2+2};
                        RD = {T0,(-T0)*ones(length(alpha),1)*alpha(:)'}; %PH to MAP
                        tRD = sum(RD{2},2);
                        pieRD = map_pie(RD);
                        
                        %define a ph for the arrival process of class r
                        A = mmap_hide(ARV{ind},setdiff(1:K,r));
                        
                        %define a ph for the service process of class r
                        S = PH{ist,r};
                        pieS = map_pie(S);
                        tS=sum(S{2},2);
                        
                        %with probability rho the output is the
                        %inter-arrival time, with probability 1-rho is the
                        %sum of inter-arrival time and response time
                        %distribution
                        rho = sum(UN(ist,:));
                        Afull = (sum(QN(ist,:)))/rho; % from A = (1-rho)*0 + rho*Afull
                        pidle_fullonarrival = 1 - (Afull)/(1+Afull);
                        pidle_emptyonarrival = 1 - rho;
                        
                        % remove from iat time spent in service
                        DAS = mmap_scale(A,map_mean(A)-0*map_mean(S));
                        tDA = sum(DAS{2},2);
                        pieDA = map_pie(DAS);
                        
                        DEP0ir = [DAS{1}, rho*tDA*pieRD, (1-rho)*tDA*pieS;
                            0*tRD*pieDA,  RD{1}, 0*tRD*pieS;
                            0*sum(S{2},2)*pieDA, 0*sum(S{2},2)*pieRD, S{1}];
                        
                        DEP1ir = abs([0*A{2}, 0*tDA*pieRD, 0*tDA*pieS; ...
                            pidle_fullonarrival*tRD*pieDA, 0*RD{2},  (1-pidle_fullonarrival)*tRD*pieS; ...
                            pidle_emptyonarrival*tS*pieDA, 0*tS*pieRD, (1-pidle_emptyonarrival)*S{2}]);
                        
                        DEP{ind,r} = map_normalize({DEP0ir,DEP1ir});
                        
                        DEP{ind,r} = map_scale(DEP{ind,r}, 1 / (lambda(r) * V(ind,r)) );
                        SCVd(ind,r) = map_scv(DEP{ind,r});
                        IDCd(ind,r) = map_idc(DEP{ind,r});
                    end
            end
        end
        
        if it>1
            SCVmam=SCVd(2:end);
            %SCVmam
            %IDCd
            %QN
        end
    end
    
else
    warning('This model is not supported by SolverMAM yet. Returning with no result.');
end
if options.verbose
    fprintf(1,'MAM parametric decomposition completed in %d iterations.\n',it);
end
end
