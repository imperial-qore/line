classdef Det < ContinuousDistrib & DiscreteDistrib
    % Deterministic distribution
    %
    % Copyright (c) 2012-2019, Imperial College London
    % All rights reserved.
    
    properties
    end
    
    methods
        function self = Det(t)
            % Construct a deterministic distribution with value t
            self@ContinuousDistrib('Det',1,[t,t]);
            self@DiscreteDistrib('Det',1,[t,t]);
            setParam(self, 1, 't', t, 'java.lang.Double');
            self.javaClass = 'jmt.engine.random.DeterministicDistr';
            self.javaParClass = 'jmt.engine.random.DeterministicDistrPar';
        end
        
        function ex = getMean(self)
            % Get distribution mean
            ex = self.getParam(1).paramValue;
        end
        
        function SCV = getSCV(self)
            % Get distribution squared coefficient of variation (SCV = variance / mean^2)
            SCV = 0;
        end
        
        function X = sample(self, n)
            % Get n samples from the distribution
            X = self.getParam(1).paramValue * ones(n,1);
        end
        
        function Ft = evalCDF(self,t)
            % Evaluate the cumulative distribution function at t
            if t < self.getParam(1).paramValue
                Ft = 0;
            else
                Ft = 1;
            end
        end
    end
    
end

