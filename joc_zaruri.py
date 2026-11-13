import random

# aruncam cele 2 zaruri
zar1 = random.randint(1, 6)
zar2 = random.randint(1, 6)

print("Primul zar:", zar1)
print("Al doilea zar:", zar2)

suma = zar1 + zar2
print("Suma este:", suma)

if suma == 7 or suma == 11:
    print("AI CASTIGAT")
elif suma == 2 or suma == 3 or suma == 12:
    print("AI PIERDUT")
else:
    print("MAI INCEARCA")