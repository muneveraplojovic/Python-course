# Tipovi podataka: prosti i slozeni 
# varijable sa celim brojem - int - intiger
# brojevi sa decimalama - float 
# bool - true/false
# string - niz karaktera

# print - ispis necega u terminalu
# pretvaranje iz jednog tipa u drugi
# type


# Operatori
# -aritmeticki operatori (+-*/%**)
#- relacijski-rezultat je uvek bool- (<><=>=, ==, != )
# - operatori za dodelu vrednosti - += -=

#Logicki operator - true/false
# and-true if both of them are true, za povezivanje izraza
# or- true if either one of them are true, 
# not - not true-false, not false-true, 

# Metode stringa:
# -indeksiranje 0123456789
# -indeksiranje sa minusom -1 -2 -3 -4 -5 -6 -7 -8 -9 (zadnji broj ima indeks -1)
# -replace
# -length len - vraca druzinu stringa, ne funkcionise kod brojeva
# -upper

# if statement/condition
# else statement
#proveravamo povrsine kvadrata i pravougaonika uz pomoc if and else statement 


# brojgodina = 17
# moj_broj = 5.78
# print(brojgodina)

# num1=int(input("Unesite broj: "))
# num2=int(input("Unesite broj: "))
# num3=int(input("Unesite broj: "))

# sum=num1+num2+num3
# div=int(sum/3)
# print("Aritmeticka sredina vasih unetih brojeva je: ", div)


# a=int(input("Unesite duzinu stranice a: "))
# b=int(input("Unesite duzinu stranice b: "))

# povrsina=int(a*b)
# print("Povrsina vaseg pravougaonika je: ", povrsina)


# x,y,z="banana", "cherry", "chocolate"
# print(x,z,y)

# x=z=y="Bananana"
# print(x)
# print(z)
# print(y)


# obim i povrsina kruga
# pi=3.14
# r=int(input("Unesite broj poluprecnika: "))

# pov=2*r*pi
# obim=2**2*pi
# print("povrsina", pov)
# print("obim", obim)
#----------------------------------------------

# unesite 3 stranice trougla i da se izracuna obim


# str1=int(input("unesite stranicu 1: "))
# str2=int(input("unesite stranicu 2: "))
# str3=int(input("unesite stranicu 3: "))

# obim=str1+str2+str3

# print("obim je: ", obim)

# galon=4.54
# litri=float(input("Unesite broj litara: "))

# sum=litri*galon
# print(sum)

# ------------------------------------------------------------------------------

# skola= "gimnazija"
# rezultat= skola.replace("g", "G")
# print(rezultat)

# x=int(input("unesite broj: "))
# y=int(input("unesite broj: "))

# z=(x**2+y**2)**2
# print("vrednost izraza je: ", z)

# galoni=float(input("Unesite galone: "))
# litri= galoni* 4.54
# print(litri)


# broj1= float(input("Unesite broj 1: "))
# broj2= float(input("Unesite broj 2: "))
# broj3= float(input("Unesite broj 3: "))

# # rezultat=(broj1+broj2)/broj3

# print((broj1+broj2)/broj3)
# skola="gimnazija"
# print(skola[2 : ])
# # prva vrednost se racuna a zadnja se ne racuna

# print(skola[2: :])
# # pocetna, zavrsna, korak 

# print(skola[2: :2])
# # print(skola[ : :-1]) ispise rec gimnazija unazad

# rec= str(input("unesite rec: "))
# rez= rec.replace(rec[0], rec[0].upper())
# print(rez)

# ----------------------------------------------------------------------------------

# broj1 = 5
# broj2 = 6
# if broj1 > broj2:
#     print("true")
# else:
#     print("false")
# indentacija-odvajanje spejsovima
# else statement - sve ostalo
# -------------------------
# broj=float(input("Unesite broj: "))

# if broj > 0:
#     print("Broj je pozitivan!")
# else:
#     print("Broj je negativan!")


# dve tacke obavezne posle if i else-a
# ------------------------------
# a=
# b= 
# a=b izracunati povrsinu kvadrata a2
# a!=povrsina pravougaonika a*b

# stranica_a=float(input("Unesite stranicu a: "))
# stranica_b=float(input("Unesite stranicu b: "))

# if stranica_a==stranica_b:
#     print("Povrsina kvadrata je: ", stranica_a**2)
# else:
#     print("Povrsina pravougaonika je: ", stranica_a*stranica_b)

# --------------
# proveriti da li je uneta rec polindrom

# palindrom=str(input("Unesite neku rec: "))

# if palindrom == palindrom[ : :-1]:
#     print("Rec je palindrom")
# else:
#     print("Rec nije palindrom")

# ocena=int(input("unesite ocenu: "))

# if ocena ==5:
#     print("odlican 5")
# elif 