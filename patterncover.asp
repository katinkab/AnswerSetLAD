%%% Dieses Programm soll ein vollstämdiges pattern cover für eine Menge von Beobachtungen berechnen.
%%% Dabei soll es (anders als in meinen früheren Implementierungen) nicht auf eine bereits berechnete Menge von Pattern zurückgreifen.
%%% Es soll selbst Pattern berechnen und im nächsten Schritt auswählen.
%%% Eine Lösungsmenge ist eine Menge von Pattern, die alle Beobachtungen abdeckt.

%%%GENERATE%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%one complete pattern cover (It includes pattern X for sign 'sign')
1{completecover(pat(lit((T,C),lit((S,B),Z)),N+1,(P,X))):pat(lit((T,C),lit((S,B),Z)),N+1,(P,X))}.

%%%DEFINE%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
pat(lit((S,B),none),1,(P,X)):-i(P,X,S,B).
pat(lit((T,C),lit((S,B),Z)),N+1,(P,X)):-pat(lit((S,B),Z),N,(P,X)),i(P,X,T,C),(S,B)!=(T,C),S<T.

%%prefered pattern (wenn sie verschiedene obs covern)
prefered(lit((T,C),lit((S,B),Z)),M,(P,X,none),1):-pat(lit((T,C),lit((S,B),Z)),M,(P,X)).
prefered(lit((T,C),lit((S,B),Z)),M,(P,X,(Y,none)),N+1):-prefered(lit((T,C),lit((S,B),Z)),M,(P,X,none),N),pat(lit((T,C),lit((S,B),Z)),M,(P,Y)),X!=Y.

%%%TEST%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%literal combination must not be in observation of opposite sign
:-completecover(pat(K,M,(1,_))),completecover(pat(K,M,(0,_))).
%%all observations must be covered
:-i(_,X,_,_),not completecover(pat(_,_,(_,X))).

%%minimal set of patterns (THIS TAKES TOOOOOO LONG)
%#minimize {1@1,M:completecover(M)}.
%also waehle spezielle pattern, die bereits hohes coverage haben

#show completecover/1.
#show prefered/4.
