%this program calculates the predictions of observations according to a discriminant build by a theory (e.g. primecover_highoccurence)
%Input: Testset of observations, primecover (including pat(N,S,D,(V,Q)). cov(N,S,D,(Z,Y)). train_nbrnegobs(T). train_nbrposobs(P).)

%constants
%Choose constants: threshold for prediction%
#const threshold=0.

%count observations of testset
testnbrposobs(P) :- P=#sum{1,X:i(1,X,_,_)}.
testnbrnegobs(T) :- T=#sum{1,X:i(0,X,_,_)}.

%----------------------------

%obs X (of sign Z) is covered by primecover(N number, S sign, D degree) , if all entries are covered
testset_not_allright(N,S,D,(Z,X)) :- i(Z,X,_,_), pat(N,S,D,(V,Q)) , not i(Z,X,V,Q).
testset_allright(N,S,D,(Z,X)) :- not testset_not_allright(N,S,D,(Z,X)), i(Z,X,_,_), pat(N,S,D,(_,_)).

%coverage of patterns
coverage(N,S,D,C) :- pat(N,S,D,_), C = #sum{1, (Z,X) : cov(N,S,D,(Z,X))}.

%prediction
%patterns are weighted by their coverage normalized by the total number of positive (negative) observations
%predict positive:
predict((1,Y),correctclass(Z)) :- i(Z,Y,_,_), train_nbrnegobs(T), train_nbrposobs(P), #sum{C*T,(N,1,D):coverage(N,1,D,C),testset_allright(N,1,D,(Z,Y));-F*P,(M,0,E):coverage(M,0,E,F),testset_allright(M,0,E,(Z,Y))}>threshold*T*P.
%predict negative
predict((0,Y),correctclass(Z)) :- i(Z,Y,_,_), train_nbrnegobs(T), train_nbrposobs(P), #sum{C*T,(N,1,D):coverage(N,1,D,C),testset_allright(N,1,D,(Z,Y));-F*P,(M,0,E):coverage(M,0,E,F),testset_allright(M,0,E,(Z,Y))}<=threshold*T*P.

%---------------------------

%statistics
correctpos(C,of(P)) :- testnbrposobs(P), C = #sum{ 1,Y : predict((1,Y),correctclass(1)) }.
correctneg(C,of(T)) :- testnbrnegobs(T), C = #sum{ 1,Y : predict((0,Y),correctclass(0)) }.
falsepos(C,of(T)) :- testnbrnegobs(T), C = #sum{ 1,Y : predict((1,Y),correctclass(0)) }.
falseneg(C,of(P)) :- testnbrposobs(P), C = #sum{ 1,Y : predict((0,Y),correctclass(1)) }.

#show predict/2.
#show correctpos/2.
#show correctneg/2.
#show falsepos/2.
#show falseneg/2.
