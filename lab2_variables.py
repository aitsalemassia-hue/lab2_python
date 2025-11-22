A = 42              
B = 3.14          
X= "Python"         
vrai_ou_faux = True  
print("A =", A, "→", type(A),"B =", B, "→", type(B),"X =", X, "→"
, type(X),"vrai_ou_faux =", vrai_ou_faux, "→", type(vrai_ou_faux))    
age_str = input("Quel âge as-tu ? ")
print("Tu as saisi :", age_str, "→", type(age_str))

age = int(age_str)
print("Après conversion :", age, "→", type(age))
try:
    age = int(input("Quel âge as-tu ? "))
    print(f"Dans 5 ans tu auras {age + 5} ans.")
except ValueError:
    print("Saisie invalide, merci d'entrer un entier.")

print(float(7.23))
print(int(7.99))
print(str(100))
print(bool(False))
print(str(123))

