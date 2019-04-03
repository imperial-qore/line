function [Pr,G,runtime] = solver_nc_marg(qn, options)
% Copyright (c) 2012-2019, Imperial College London
% All rights reserved.

M = qn.nstations;    %number of stations
K = qn.nclasses;    %number of classes
state = qn.state;
mu = qn.mu;
phi = qn.phi;
S = qn.nservers;
NK = qn.njobs';  % initial population per class
C = qn.nchains;

PH=cell(M,K);
for i=1:M
    for k=1:K
        PH{i,k} = Coxian(mu{i,k}, phi{i,k}).getRepresentation();
    end
end
%% initialization

% determine service times
ST = zeros(M,K);
V = zeros(M,K);
for k = 1:K
    for i=1:M
        ST(i,k) = 1 ./ map_lambda(PH{i,k});
    end
end
ST(isnan(ST))=0;
for c=1:qn.nchains
    V = V + qn.visits{c};
end

alpha = zeros(qn.nstations,qn.nclasses);
Vchain = zeros(qn.nstations,qn.nchains);
REFchain = zeros(qn.nstations,qn.nchains);
for c=1:qn.nchains
    inchain = find(qn.chains(c,:));
    for i=1:qn.nstations
        Vchain(i,c) = sum(qn.visits{c}(i,inchain)) / sum(qn.visits{c}(qn.refstat(inchain(1)),inchain));
        REFchain(i,c) = 1 / sum(qn.visits{c}(qn.refstat(inchain(1)),inchain));
        for k=inchain
            alpha(i,k) = alpha(i,k) + qn.visits{c}(i,k) / sum(qn.visits{c}(i,inchain)); % isn't alpha(i,j) always zero when entering here?
        end
    end
end

Vchain(~isfinite(Vchain))=0;
alpha(~isfinite(alpha))=0;

Lchain = zeros(M,C);
STchain = zeros(M,C);

Nchain = zeros(1,C);
refstatchain = zeros(C,1);
for c=1:qn.nchains
    inchain = find(qn.chains(c,:));
    isOpenChain = any(isinf(qn.njobs(inchain)));
    for i=1:qn.nstations
        % we assume that the visits in L(i,inchain) are equal to 1
        STchain(i,c) = ST(i,inchain) * alpha(i,inchain)';
        if isOpenChain && i == qn.refstat(inchain(1)) % if this is a source ST = 1 / arrival rates
            STchain(i,c) = 1 / sumfinite(qn.rates(i,inchain)); % ignore degenerate classes with zero arrival rates
        else
            STchain(i,c) = ST(i,inchain) * alpha(i,inchain)';
        end
    end
    Nchain(c) = sum(NK(inchain));
    refstatchain(c) = qn.refstat(inchain(1));
    if any((qn.refstat(inchain(1))-refstatchain(c))~=0)
        error(sprintf('Classes in chain %d have different reference station.',c));
    end
end
STchain(~isfinite(STchain))=0;
Tstart = tic;

[M,K]=size(STchain);

Lchain = zeros(M,K);
mu = ones(M,sum(Nchain));
for i=1:M
    Lchain(i,:) = STchain(i,:) .* Vchain(i,:);
    if isinf(S(i)) % infinite server
        mu(i,1:sum(Nchain)) = 1:sum(Nchain);
    else
        mu(i,1:sum(Nchain)) = min(1:sum(Nchain), S(i)*ones(1,sum(Nchain)));
    end
end
Lchain(~isfinite(Lchain))=0;

G = pfqn_gmvald(Lchain, Nchain, mu);
for ist=1:qn.nstations
    ind = qn.stationToNode(ist);
    isf = qn.stationToStateful(ist);
    [~,nivec] = State.toMarginal(qn, ind, state{isf});
    if min(nivec) < 0 % user flags that state of i should be ignored
        Pr(i) = NaN;
    else
        set_ist = setdiff(1:qn.nstations,ist);
        nivec_chain = nivec * qn.chains';
        
%        F_i = pfqn_ca(ST(ist,:).*V(ist,:),nivec);
%        Vchain_i = pfqn_gmvald(REFchain(ist,:), nivec_chain, mu_chain(ist,:), options);
%        Gchain_minus_i = pfqn_gmvald(Lchain(set_ist,:), Nchain-nivec_chain, mu_chain(set_ist,:), options);
%        Pr(ist) = F_i * Vchain_i * Gchain_minus_i / G ;
        
%        F_i = pfqn_gmvald(Lchain(ist,:), nivec_chain, mu_chain(ist,:), options);
%        G_minus_i = pfqn_gmvald(Lchain(set_ist,:), Nchain-nivec_chain, mu_chain(set_ist,:), options);
%        g0_i = pfqn_gmvald(ST(ist,:).*alpha(ist,:),nivec, mu_chain(ist,:), options);
%        G0_i = pfqn_gmvald(STchain(ist,:),nivec_chain, mu_chain(ist,:), options);        
%        Pr(ist) = F_i * G_minus_i / G * (g0_i / G0_i);
        
%        G_minus_i = pfqn_gmvald(Lchain(set_ist,:), Nchain-nivec_chain, mu_chain(set_ist,:), options);
%        F_i = prod(Vchain(ist,:).^nivec_chain);
%        H_i = pfqn_gmvald(ST(ist,:).*alpha(ist,:),nivec, mu_chain(ist,:), options);
%        Pr(ist) =  G_minus_i / G * H_i * F_i;
        
        G_minus_i = pfqn_gmvald(Lchain(set_ist,:), Nchain-nivec_chain, mu(set_ist,:), options);
        F_i = pfqn_gmvald(ST(ist,:).*V(ist,:), nivec, mu(ist,:), options);
        Pr(ist) =  F_i * G_minus_i / G;
    end
end
runtime = toc(Tstart);
Pr(isnan(Pr))=0;
lG = log(G);
if options.verbose > 0
    fprintf(1,'Normalizing constant (NC) analysis completed in %f sec\n',runtime);
end
return
end
