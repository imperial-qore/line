classdef SolverMVA < NetworkSolver
% Copyright (c) 2012-2018, Imperial College London
% All rights reserved.

    methods
        function self = SolverMVA(model,varargin)                        
            self = self@NetworkSolver(model, mfilename);
            self.setOptions(Solver.parseOptions(varargin, self.defaultOptions));
        end
                        
        function runtime = run(self)
            T0=tic;
            options = self.getOptions;
            if ~options.force && ~self.supports(self.model)
                if options.verbose
                    warning('This model is not supported by the %s solver. Quitting.',mfilename);
                end
                runtime = toc(T0);
                return
            end
            
            rng(options.seed,'twister');
            
            [qn] = self.model.getStruct();
            
            [Q,U,R,T,C,X] = solver_amva_analysis(qn, options);            
            runtime = toc(T0);
            
            self.setAvgResults(Q,U,R,T,C,X,runtime);
        end
    end
    
    methods(Static)
        function featSupported = getFeatureSet()
            featSupported = SolverFeatureSet;
            featSupported.setTrue({'Sink','Source',...
                'ClassSwitch','DelayStation','Queue',...
                'Cox2','Erlang','Exponential','HyperExp',...
                'StatelessClassSwitch','InfiniteServer','SharedServer','Buffer','Dispatcher',...
                'Server','JobSink','RandomSource','ServiceTunnel',...
                'SchedStrategy_INF','SchedStrategy_PS',...
                'SchedStrategy_DPS','SchedStrategy_FCFS',...
                'RoutingStrategy_PROB','RoutingStrategy_RAND',...                
                'ClosedClass','OpenClass','Replayer'});            
        end        
        
        function [bool, featSupported] = supports(model)
            featUsed = model.getUsedLangFeatures();    
            featSupported = SolverMVA.getFeatureSet();
            bool = SolverFeatureSet.supports(featSupported, featUsed);
        end
    end
    
    methods (Static)
        function options = defaultOptions(self)
            options = Solver.defaultOptions();
            options.iter_max = 10^3;
            options.iter_tol = 10^-6;
        end
    end
end