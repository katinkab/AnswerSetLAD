%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ------------------------------------------------ %
%  AnswerSetLAD - an implementation of LAD in ASP  %
% ------------------------------------------------ %
%                                                  %  
%       STRONG SPANNED PATTERN GENERATION          % 
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

%%%%%try to add a new observation
%%which of the literals of the pattern appears in the new observation?
lit_in_new(Y,(S,B)):-lit(S,B),i(sign,Y,S,B), not cov(sign,Y).
nbrlitinnew(Y,M):-lit_in_new(Y,_),M=#sum{1,(S,B):lit_in_new(Y,(S,B))}.

%%is the literal combination (with new obs Y) in an observation of opposite sign Z?
litinnew_in_op(Z,(S,B),Y):-lit_in_new(Y,(S,B)),i(Q,Z,S,B),Q!=sign.
litinnew_countinop(Z,D,Y):-i(Q,Z,_,_),Q!=sign,litinnew_in_op(Z,_,Y),D=#sum{1,(S,B):litinnew_in_op(Z,(S,B),Y)}.
%%if pattern is fully included in an obs of opposite sign, then this is not a bigger pattern.
notabiggerpat(Y):-nbrlitinnew(Y,M),litinnew_countinop(Z,D,Y),M=D.

%%%TEST%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%not a pattern if full literal combination (pattern) covers an obs of opposite sign
:-D=E,countlit(E),countinop(_,D).

%%if we find a pattern which is not fully included, then the original pattern (covered set) does not form a strong (spanned) pattern
:-not notabiggerpat(Y),lit_in_new(Y,_).

#show countlit/1.
#show lit/2.
#show nbrcovered/1.
#show cov/2.
