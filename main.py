import numpy as np

a1 = np.array([1, 2, 3])
print("a1", a1)

a2 = np.linspace(0, 100, 21)
print("a2", a2)

a3 = np.zeros(10) 
print("a3", a3) #stmpa a schermo dieci volte zero

a4 = np.ones(12) 
print("a4", a4) #stampa a schermo dodici volte uno

np.random.seed(18) #"seed"=> seme del random
r1 = np.random.rand(2, 3) #le cose colorate in verde indicano che ci troviamo in una libreria. In questo caso: "np"=> libreria, "random"=> package (sotto-libreria), "rand(2, 3)"=> funzione
print("r1", r1)

r1 = np.random.rand(2, 3)*15 #"*15"=>genera numeri casuali che vanno da zero a 15
print("r1", r1)

r2 = r1.reshape(3, 2)
print("r2", r2)