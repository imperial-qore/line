classdef DiscreteDistrib < Distrib
    % Copyright (c) 2018, Imperial College London
    % All rights reserved.
    
    properties
    end
    
    methods
        %Constructor
        function self = DiscreteDistrib(p,x)
            % p(i) is the probability of item i
            % x(i) is the value of item i
            n = length(p);
            if ~exist('x','var')
                x=1:n;
            end
            self = self@Distrib('DiscreteDistr',1,[1,n]);
            setParam(self, 1, 'p', p(:)', 'java.lang.Double');
            setParam(self, 2, 'x', x(:)', 'java.lang.Double');
            setParam(self, 3, 'f', cumsum(p(:)')/sum(p), 'java.lang.Double');
            self.javaClass = '';
            self.javaParClass = '';
        end
        
        function ex = getMean(self)
            p = self.getParam(1).paramValue;
            n = length(p);
            ex = sum(p*(1:n)');
        end
        
        function SCV = getSCV(self)
            p = self.getParam(1).paramValue;
            n = length(p);
            e2 = sum(p*(1:n).^2');
            var = e2 - ex^2;
            SCV = var / ex^2;
        end
        
        function X = sample(self, n)
            f = self.getParam(3).paramValue;
            r = rand(n,1);
            X = maxpos(min(repmat(r,1,size(f,2))<=f,2)')';
        end
        
        function Ft = evalCDF(self,k)
            f = self.getParam(3).paramValue;
            if k>=1 && k<length(f)
                Ft = f(k);
            else
                Ft = 0;
            end            
        end
        
        function pk = getPmf(self, v)
            p = self.getParam(1).paramValue;
            x = self.getParam(2).paramValue;
            if ~exist('v','var')
                pk = p;
                return
            end
            for i=1:length(v)
                pk(i) = p(find(x==v(i),1));
            end
        end
        
        function bool = isDisabled(self)
            p = self.getParam(1).paramValue;
            bool = any(isnan(p));
        end
    end
    
end
