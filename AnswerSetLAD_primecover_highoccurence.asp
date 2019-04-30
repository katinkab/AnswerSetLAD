%%%Dieses ASP Programm soll ein vollständiges pattern cover bestehend aus 
%		high-literal-occurence prime pattern berechnen


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

%weights for primes depending on the literal occurence over all prime patterns
%literal ((variable Y, value V), sign of pattern S, occurence Q)
occ(((Y,V),S),Q) :- pat(_,S,_,(Y,V)), Q = #sum{1,N,S,D : pat(N,S,D,(Y,V)) }.
occ(((Y,V),S),0) :- pat(_,S,_,_), pat(_,_,_,(Y,V)), not pat(_,S,_,(Y,V)).

literalweight(((Y,V),S), P,Q,N,R) :- occ(((Y,V),S),P), occ(((Y,X),S),Q), occ(((Y,V),W),N), occ(((Y,X),W),R), V!=X, W!=S.
fullliteralweight(((Y,V),S), W) :- literalweight(((Y,V),S), P,Q,N,R), W=P*(N+R)-N*(P+Q).

%weights for patterns (sum over the literal weights)
patternweight((N,S,D),K) :- pat(N,S,D,_), K = #sum{W, (Y,V),S  : fullliteralweight(((Y,V),S), W), pat(N,S,D,(Y,V)) }. 

% TEST
:- i(P,X,_,_), not theorycov(P,X).

% OPTIMIZE
#minimize{ 1@2,N,S,D : primecover(N,S,D) }.
#maximize{ K@1 : patternweight((N,S,D),K), primecover(N,S,D) }.

#show primecover/3.
%#show occ/2.
%#show literalweight/5.
#show literalweight/5.
#show fullliteralweight/2.
%#show patternweight/2.
