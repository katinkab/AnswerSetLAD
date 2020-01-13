%%%Dieses ASP Programm ist ein Parser, der primecover.asp einliest 
%%	und eine Datei für _predict erstellt

%Input: 1) All prime patterns 
% 		format: pat(number, sign, degree, (variable, value)).
%		+ coverage 
%		format: cov(patnumber, sign, degree, (obssign, obsnumber)).
%	2) data set
%		format: i(obssign, obsnumber, variable, value).


theorypat(N,S,D,(V,X)) :- primecover(N,S,D), pat(N,S,D,(V,X)).
theorycov(N,S,D,(V,X)) :- primecover(N,S,D), cov(N,S,D,(V,X)).

train_nbrposobs(C):-C=#sum{1,X:i(1,X,_,_)}.
train_nbrnegobs(C):-C=#sum{1,X:i(0,X,_,_)}.

#show theorypat/4.
#show theorycov/4.
#show train_nbrposobs/1.
#show train_nbrnegobs/1.
