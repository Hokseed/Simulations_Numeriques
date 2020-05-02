clear all; close all; clc



% Paramètres de la loi binomiale

n = 1;

p = 1/4;



% nombres de v.a.

N = 1000;



% pre-allocation valeurs

X = zeros(1,N);

XN = zeros(5,N);



% création vecteur de nombres aléatoires entre 0 et 1 (loi uniforme)

rng(123);

Xrand = rand(5,N);



% construction des valeurs

for j = 1:5

    for i = 1:N

        if(Xrand(j,i) <= p)

            X(i) = 1;

        else

            X(i) = 0;

        end

        % moyenne empirique sur les "i" premières v.a.

        XN(j,i) = 1/i * sum(X(1:i));

    end

end



% tracé de la moyenne empirique en fonction de N (1 réalisations)

figure;plot(1:N,XN(1,:));





% tracé de la moyenne empirique en fonction de N (5 réalisations)

figure;

hold on

for j = 1:5

    plot(1:N,XN(j,:));

end
