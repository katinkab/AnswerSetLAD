%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ------------------------------------------------ %
%  AnswerSetLAD - an implementation of LAD in ASP  %
% ------------------------------------------------ %
%                                                  %  
%          SPANNED PATTERN GENERATION              % 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%CONSTANTS%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%user can choose constant: sign (positive pattern: 1; negative pattern: 0)

%%%sign of pattern
#const sign=1.

%%%GENERATE%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%set of covered observations (every subset of positive (negative) observations is possible)
1{cov(sign,X):i(sign,X,_,_)}.
%%Counts how many observations are covered
nbrcovered(N):-N=#sum{1,X:cov(sign,X)}.

%%%DEFINE%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%pattern generation (find literals)
%%each literal included in a covered observation is a candidate
lit_candidate(S,B):-cov(sign,X),i(sign,X,S,B).
%%literal must appear in every covered observation to be included in pattern
not_lit(S,B):-lit_candidate(S,B),cov(sign,Y),not i(sign,Y,S,B).
lit(S,B):-not not_lit(S,B), lit_candidate(S,B).
countlit(E):-E=#sum{1,(S,B):lit(S,B)}.

%%is the literal combination in an observation of opposite sign?
in_op(Y,(S,B)):-lit(S,B),i(Q,Y,S,B),Q!=sign.
countinop(Y,D):-i(Q,Y,_,_),Q!=sign,D=#sum{1,(S,B):in_op(Y,(S,B))}.

%%can we add an observation (not covered yet) to this set of literals? (does it actually cover more?)
obsnotincover(sign,Y):-i(sign,Y,_,_), not cov(sign, Y).
not_addobs(sign,Y):-obsnotincover(sign,Y),lit(S,B), not i(sign,Y,S,B).
addobs(sign,Y):-obsnotincover(sign,Y), not not_addobs(sign,Y).

%%%TEST%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%not a pattern if full literal combination (pattern) covers an obs of opposite sign
:-D=E,countlit(E),countinop(_,D).

:-addobs(sign,_).

#show countlit/1.
#show lit/2.
#show nbrcovered/1.
#show cov/2.

