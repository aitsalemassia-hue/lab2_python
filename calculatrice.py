
reponse=input("voulez-vous faire une opération(oui,non) ?")
while reponse=="oui":
     nombre_1=float(input("donner un nombre :"))
     nombre_2=float(input("donner un  autre nombre :"))
     print ("menu :")
     print ("1:la somme ")
     print ("2:la soustraction ")
     print ("3:le produit ")
     print ("4:la division ")
     choix=input(" entrer votre choix (1,2,3,4) :")
     if choix=='1':
          print(f" {nombre_1}+{nombre_2} = {nombre_1 + nombre_2}")
     elif choix=='2':
          print(f" {nombre_1}-{nombre_2} = {nombre_1 - nombre_2}")
     elif choix=='3':
          print(f" {nombre_1}*{nombre_2} = {nombre_1 * nombre_2}")
     elif choix =='4':
          if nombre_2!=0:
               print(f" {nombre_1}/{nombre_2} = {nombre_1 / nombre_2}")
          else:
               print("impossible de divisé sur 0 ")
     else :
          print("choix invalide !")
     reponse=input("voulez-vous faire une autre opération(oui,non) ?")

