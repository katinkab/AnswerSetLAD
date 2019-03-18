train_nbrposobs(3).
train_nbrnegobs(7).

minimalcover((1,1),(1,1)). 
prev((1,1),1).
prev((0,1),0).

minimalcover((1,2),(7,0)). 
prev((1,2),1).
prev((0,2),0).

minimalcover((1,3),(11,0)). 
minimalcover((1,3),(9,1)). 
minimalcover((1,3),(10,0)). 
minimalcover((1,3),(14,0)). 
prev((1,3),1).
prev((0,3),0).

minimalcover((0,4),(10,1)).
prev((1,4),0).
prev((0,4),2).

minimalcover((0,5),(14,1)).
minimalcover((0,5),(1,0)).
prev((1,5),0).
prev((0,5),4).

primecover((0,6),(13,0)).
primecover((0,6),(1,0)).
primecover((0,6),(7,1)).
prev((1,6),0).
prev((0,6),4).

