clear;
model = Network('model');

node{1} = DelayStation(model, 'Delay');
node{2} = QueueingStation(model, 'Queue1', SchedStrategy.PS);

node{2}.setNumServers(2);

% Default: scheduling is set as FCFS everywhere, routing as Random
jobclass{1} = ClosedClass(model, 'Class1', 3, node{1}, 0);
jobclass{2} = ClosedClass(model, 'Class2', 1, node{1}, 0);

node{1}.setService(jobclass{1}, Exp(3));
node{1}.setService(jobclass{2}, Exp(0.5));

node{2}.setService(jobclass{1}, Exp(0.1));
node{2}.setService(jobclass{2}, Exp(1));

M = model.getNumberOfStations();
K = model.getNumberOfClasses();

P = cell(K,K);
P{1,1} = [0.3,0.1;
    0.2,0];
P{1,2} = [0.6,0;
    0.8,0];
P{2,2} = [0,1  ;
    0,0];
P{2,1} = [0,0  ;
    1,0];

%%pause
model.linkNetwork(P);
%model.initDefault;
model.initFromMarginalAndStarted([2,1;1,0],[0,0;1,0]);

options = Solver.defaultOptions;
options.keep=true;
options.verbose=1;

disp('This example shows the execution of the solver on a 2-class 2-node class-switching model with specified initial state.')
% This part illustrates the execution of different solvers
solver={};
solver{end+1} = SolverCTMC(model,options);
solver{end+1} = SolverJMT(model,options);
solver{end+1} = SolverSSA(model,options);
solver{end+1} = SolverFluid(model,options);
solver{end+1} = SolverAMVA(model,options);
solver{end+1} = SolverNC(model,options);
for s=1:length(solver)
    fprintf(1,'SOLVER: %s\n',solver{s}.getName());
    %[QN,UN,RN,TN] = solver{s}.getAvg(); % numerical data 
    AvgTable = solver{s}.getAvgTable()
end
