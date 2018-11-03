function name = getNodeFullName(self,node)
% Copyright (c) 2012-2018, Imperial College London
% All rights reserved.

if ischar(node)
    G = self.lqnGraph;
    name = G.Nodes.Node{self.getNodeIndex(node)};
else
    name = G.Nodes.Node{node};
end
end