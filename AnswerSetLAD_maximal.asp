%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ------------------------------------------------ %
%  AnswerSetLAD - an implementation of LAD in ASP  %
% ------------------------------------------------ %
%                                                  %  
%          MAXIMAL PATTERN GENERATION              % 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%CONSTANTS%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%User can choose constants: sign, degree, homogeneity, prevalence

%%%sign of pattern
#const sign=1.

%%%degree
#const degree=1.

%%%homogeneity (percentage): 0..100% of coverage are "right" class obs (how many covered obs have to be of "right" class?)
#const homogeneity=100.

%%%prevalence (percentage): 0..100% of "right" class obs are covered (how many obs of "right" class have be covered?)
#const prevalence=0.

%%%count number of "right" observations (same sign as pattern)
nbrrightobs(C):-C=#sum{1,X:i(sign,X,_,_)}.


%%%GENERATE%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%one pattern of degree 'degree'
degree{pat(S,B):i(sign,_,S,B)}degree.

%%%DEFINE%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%coverage: obs X (of sign W) is covered by pat (meaning that all entries are covered)
not_covered(W,X):-i(W,X,_,_),pat(S,B),not i(W,X,S,B).
covered(W,X):-not not_covered(W,X),i(W,X,_,_).

%%%TEST%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%a pattern can't have different entry for same index
:-pat(S,B),pat(S,Q),Q<B.
%%%homogeneity: pattern can't cover more "wrong" obs than ok with homogeneity constant
:-#sum{homogeneity-100,X:covered(W,X),W=sign;homogeneity,X:covered(W,X),W!=sign}>0.
%%%prevalence: pattern has to cover as many "right" obs as wanted in prevalence constant
:-nbrrightobs(C),#sum{100,X:covered(W,X),W=sign}<prevalence*C.

%%%for maximal pattern calculation: maximize the number of covered obs
#maximize {1,X :covered(W,X)}.

#show pat/2.
