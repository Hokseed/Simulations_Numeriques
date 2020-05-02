clear all; close all; clc



% Paramètres de la loi binomiale

n = [20,100,1000];

p = 1/2;

rng(234);

for j = 1:3

    Xrand = rand(1,n(j));

    X = zeros(1,n(j));

    ma = zeros(1,n(j));

    for i = 1:n(j)

        if Xrand(i) <= p

            X(i) = 1;

        else

            X(i) = -1;

        end

        ma(i) = sum(X(1:i));

    end



    figure;

    stairs(1:n(j),ma);

end



% trajectoires de X pour n fixé et différents T

n = 100;

T = [1;0.1;0.01];

alpha = 1;

s = sqrt(alpha.*T);



figure;

hold on

for j = 1:3

    Xrand = rand(1,n);

    X = zeros(1,n);

    ma = zeros(1,n);

    for i = 1:n

        if Xrand(i) <= p

            X(i) = s(j);

        else

            X(i) = -s(j);

        end

        ma(i) = sum(X(1:i));

    end



    stairs(1:n,ma);



end

legend({'T = 1','T=0.1','T=0.01'})


