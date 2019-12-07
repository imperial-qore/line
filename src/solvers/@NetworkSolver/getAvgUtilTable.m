function [AvgTable,UT] = getAvgUtilTable(self,U,keepDisabled)
% [AVGTABLE,UT] = GETAVGUTILTABLE(SELF,U,KEEPDISABLED)

% Return table of average station metrics
%
% Copyright (c) 2012-2020, Imperial College London
% All rights reserved.
if ~exist('keepDisabled','var')
    keepDisabled = false;
end

M = self.model.getNumberOfStations();
K = self.model.getNumberOfClasses();
if nargin == 1
    U = self.model.getAvgUtilHandles();
end
UN = self.getAvgUtil();
if isempty(UN)
    AvgTable = Table();
    UT = Table();
elseif ~keepDisabled
    Uval = [];
    Class = {};
    Station = {};
    for i=1:M
        for k=1:K
            if any(sum([UN(i,k)])>0)
                Class{end+1,1} = U{i,k}.class.name;
                Station{end+1,1} = U{i,k}.station.name;
                Uval(end+1) = UN(i,k);
            end
        end
    end
    Util = Uval(:); % we need to save first in a variable named like the column
    UT = Table(Station,Class,Util);
    AvgTable = Table(Station,Class,Util);
else
    Uval = zeros(M,K);
    Class = cell(K*M,1);
    Station = cell(K*M,1);
    for i=1:M
        for k=1:K
            Class{(i-1)*K+k} = U{i,k}.class.name;
            Station{(i-1)*K+k} = U{i,k}.station.name;
            Uval((i-1)*K+k) = UN(i,k);
        end
    end
    Util = Uval(:); % we need to save first in a variable named like the column
    UT = Table(Station,Class,Util);
    AvgTable = Table(Station,Class,Util);
end
end
