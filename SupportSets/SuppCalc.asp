%Generate
{support(C):entry(_,C,_)}.

%rowsum for row R exists if sum over entries in row is greater or equal to 1 
rowsum(R):- 1 <= #sum{E,C:support(C),entry(R,C,E)}, entry(R,_,_).

%FOR TESTING
sum(S,R):- S = #sum{E,C:support(C),entry(R,C,E)}, entry(R,_,_).

%minimize columns needed such that rowsum still exists
:-entry(R,_,_), not rowsum(R).

#minimize {1,C:support(C)}.

%#show rowsum/1.
#show sum/2.
#show support/1.
