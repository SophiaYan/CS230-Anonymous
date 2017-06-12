load('LOC.mat');


%% plot runtime
load('Runtime.mat');
load('LIM.mat');
plot(LOC, LIM(1:6) / 7000, '*-', LOC, Runtime, '^-'); 
legend('Size of MSE file(Divided by 700)','Generate MSE', 'Parse MSE', 'Generate JSON', 'TOTAL');grid
xlabel('Line of Code (LOC)');
ylabel('Time (seconds)');
title('Running Time for Each Component');
saveas(gcf, 'time.jpg');

%% plot runtime comparison
LOCCom = [2421,2569,19630,46002,246109];
plot(LOC, RuntimeCodecity, '^-');grid
legend('NewbieTOGO','CodeCity');
xlabel('Line of Code (LOC)');
ylabel('Time (seconds)');
title('Running Time Comparison with CodeCity (seconds)');
saveas(gcf, 'time_comparison.jpg');

%% plot memory usage
load('MemoryUsage.mat');
plot(LOC, MemoryUsage, '^-');grid
legend('DFSWalktree', 'GenDependGraph','Inc Avg.');
xlabel('Line of Code (LOC)');
ylabel('Memory Usage (MiB)');
title('Memory Usage and Increment for 2 Critical Methods');
saveas(gcf, 'memory.jpg');
