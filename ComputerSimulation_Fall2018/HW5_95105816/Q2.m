interarrival = [1.8 2 2.2 1.9 1.8];
serviceTime = [2 4 3 3 4 3];
utilization = min(1, (mean(interarrival) .^ 2)/ (mean(serviceTime) .^ 3));
tests = [0 0 0 0 0];
for i = 1:5
    interarrival = exprnd(2, [1 99]);
    serviceTime = normrnd(3, 0.04, [1 100]);
    tests(i) = min(1, (mean(interarrival) .^ 2)/ (mean(serviceTime) .^ 3));
end
[h0, p, interval, comp] = ttest(tests, utilization)
if h0 == 0
    disp("suitable model");
else
    disp("unsuitable model");
end