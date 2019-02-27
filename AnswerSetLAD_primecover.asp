%%%Dieses ASP Programm berechnet ein minimal prime pattern cover bestehend aus 
%			prime pattern


%Input: 1) All prime patterns 
% 		format: pat(number, sign, degree, (variable, value)).
%		+ coverage 
%		format: cov(patnumber, sign, degree, (obssign, obsnumber)).
%	2) data set
%		format: i(obssign, obsnumber, variable, value).



% GENERATE
{ primecover(N,S,D) } :- pat(N,S,D,_).

% DEFINE
%covered by pattern chosen for cover (/theory)
theorycov(P,X) :- primecover(N,S,D), cov(N,S,D,(P,X)).

% TEST
:- i(P,X,_,_), not theorycov(P,X).

% OPTIMIZE
#minimize{ 1,N,S,D : primecover(N,S,D) }.

#show primecover/3.
