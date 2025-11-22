# premier conversion
celsius=float(input(" donner une valeur en Celsius :"))#lire un nombre en celsiuis 
Fahrenheit=celsius*(9/5)+32 #la relation de coversion en Fahrenheit
Kelvin=celsius+273.15 # la relation de conversion kelvin 
print(f"{celsius}°C={Fahrenheit}°F={Kelvin}°K")
celsius=Fahrenheit*(5/9)-32 # la relation de conversion en celsius 
F=float (input("donner une valeur en  Fahrenheit"))# lire une valeur en Fahrenheit
celsius=F*(5/9)-32
print(f"{F}°F={celsius}°C={Kelvin}°K")

#second conversion 
reponse=input("voulez-vous convertir une temperature(oui,non) ?")
while reponse =="oui":
     print ("menu: ")
     print("1.conversion en Fahrenheit et Kelvin ")
     print("2. conversion en Celsius et Kelvin ")
     print("3.conversion en Celsius et  en Fahrenhe ")
     choix=int (input("entrer votre choix (1,2,3)"))

     if choix ==1:
          C=float(input(" donner une valeur en Celsius :"))
          F=C*(9/5)+32 #la relation de coversion en Fahrenheit
          K=C+273.15 # la relation de conversion kelvin 

          print(f"{C}°C={F}°F={K}°K")

     elif choix==2:
          F=float (input("donner une valeur en  Fahrenheit"))
          C=F*(5/9)-32 # la relation de conversion en celsius 
          K=C+273.15 
          print(f"{F}°F={C}°C={K}°K")

     elif choix ==3:
          K=float (input("donner une valeur en  kelvin"))
          C=K-273.15
          F=C*(9/5)+32
          print(f"{K}°K={F}°F={C}°C")

     else :
          print ("choix invalide ")   
     reponse=input("voulez-vous convertir une temperature(oui,non) ?")



