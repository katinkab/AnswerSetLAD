%%% Dieses Programm soll ein vollständiges pattern cover für eine Menge von Beobachtungen berechnen.
%%% Dabei soll es (anders als in meinen früheren Implementierungen) nicht auf eine bereits berechnete Menge von Pattern zurückgreifen.
%%% Es soll selbst Pattern berechnen und im nächsten Schritt auswählen.
%%% Eine Lösungsmenge ist eine Menge von Pattern, die alle Beobachtungen abdeckt.

%%%GENERATE%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%one complete pattern cover (It includes pattern X for sign 'sign')
1{completecover(lit((T,C),lit((S,B),Z)),N+1,(P,X)):pat(lit((T,C),lit((S,B),Z)),N+1,(P,X))}.

%%%DEFINE%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
pat(lit((S,B),none),1,(P,X)):-i(P,X,S,B).
pat(lit((T,C),lit((S,B),Z)),N+1,(P,X)):-pat(lit((S,B),Z),N,(P,X)),i(P,X,T,C),(S,B)!=(T,C),S<T.

%%%TEST%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%literal combination must not be in observation of opposite sign
:-completecover(K,M,(1,_)),completecover(K,M,(0,_)).
%%all observations must be covered
:-i(_,X,_,_),not completecover(_,_,(_,X)).

%%minimal set of patterns
#minimize{1,P:completecover(P,N,X)}.

#show completecover/3.

%%% Das Program funktioniert. Für große Datensätze aber sehr sehr langsam. Unbrauchbar.
%%% Es berechnet ein Pattern Cover (hier kein prime/strong/spanned).
