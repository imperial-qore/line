function [AvgChain,QTc,UTc,RTc,TTc] = getAvgChainTable(self,Q,U,R,T)
% Copyright (c) 2012-2018, Imperial College London
% All rights reserved.

M = self.model.getNumberOfStations();
K = self.model.getNumberOfChains();
if nargin == 1
    [Q,U,R,T] = self.model.getAvgHandles();
end
[QNc,UNc,RNc,TNc] = self.getAvgChain(Q,U,R,T);

ChainObj = self.model.getChains();
ChainName = cellfun(@(c) c.name,ChainObj,'UniformOutput',false);
ChainClasses = cell(1,length(ChainName));
for c=1:length(ChainName)
    ChainClasses{c} = ChainObj{c}.classnames;
end
if isempty(QNc)
    AvgChain = table();
    QTc = table();
    UTc = table();
    RTc = table();
    TTc = table();
else
    Qval = zeros(M,K); Uval = zeros(M,K);
    Rval = zeros(M,K); Tval = zeros(M,K);
    Chain = cell(K*M,1);
    Classes = cell(K*M,1);
    Station = cell(K*M,1);
    for i=1:M
        for k=1:K
            Chain{(i-1)*K+k} = ChainName{k};
            Classes{(i-1)*K+k} = ChainClasses{k};
            Station{(i-1)*K+k} = Q{i,k}.station.name;
            Qval((i-1)*K+k) = QNc(i,k);
            Uval((i-1)*K+k) = UNc(i,k);
            Rval((i-1)*K+k) = RNc(i,k);
            Tval((i-1)*K+k) = TNc(i,k);
        end
    end
    QLen = Qval(:); % we need to save first in a variable named like the column
    QTc = table(Station,Chain,Classes,QLen);
    Util = Uval(:); % we need to save first in a variable named like the column
    UTc = table(Station,Chain,Classes,Util);
    RespT = Rval(:); % we need to save first in a variable named like the column
    RTc = table(Station,Chain,Classes,RespT);
    Tput = Tval(:); % we need to save first in a variable named like the column
    TTc = table(Station,Chain,Classes,Tput);
    AvgChain = table(Station,Chain,Classes,QLen,Util,RespT,Tput);
end
end