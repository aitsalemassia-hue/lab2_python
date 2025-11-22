phrase =input("Entrez une phrase : ")
longueur = len(phrase)
print(f"la longueur de votre phrase est : {longueur}")
print("la phrase en majuscule: ",phrase.upper())#on garde L’ancienne version
print("la phrase en minuscule:",phrase.lower())
phrase_modifiee=phrase.upper()
print ("comparaison entre la phrase originale et la modifiée :", phrase == phrase_modifiee)
print("l'inverse de la phrase :",phrase[::-1])
if phrase == phrase[::-1]:
     print("\nla phrase est un palindrome")
else:
     print("\nla phrase n'est pas un palindrome")