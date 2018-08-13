%%% Dieses Programm soll ein vollstämdiges pattern cover für eine Menge von Beobachtungen berechnen.
%%% Dabei soll es (anders als in meinen früheren Implementierungen) nicht auf eine bereits berechnete Menge von Pattern zurückgreifen.
%%% Es soll selbst Pattern berechnen und im nächsten Schritt auswählen.
%%% Eine Lösungsmenge ist eine Menge von Pattern, die alle Beobachtungen abdeckt.

%sub(set(U,S,none),1,V) :- edge(U,V,S).
%rest rekursiv
%sub(set(U,SU,set(W,SW,T)),N+1,V) :- edge(U,V,SU), sub(set(W,SW,T),N,V), U<W.

%%%GENERATE%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%one complete pattern cover (It includes pattern X for sign 'sign')
1{completecover(pat(lit((T,C),lit((S,B),Z)),N+1,(P,X))):pat(lit((T,C),lit((S,B),Z)),N+1,(P,X))}.

%%%DEFINE%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
pat(lit((S,B),none),1,(P,X)):-i(P,X,S,B).
pat(lit((T,C),lit((S,B),Z)),N+1,(P,X)):-pat(lit((S,B),Z),N,(P,X)),i(P,X,T,C),(S,B)!=(T,C),S<T.

%%%TEST%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
:-

#show pat/3.
