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
# # elif 
# --------------------------------------------------------------------------------

# manje od 6 godina-dete, izmedju 7-18 - adolescent, vise od 18-odrasla osoba

# godine=int(input("Molimo vas unesite koliko imate godina: "))

# if godine <= 6:
#     print("Ti si dete!")
# elif godine>=7 and godine<=18:
#     print("Ti si adolescent!")
# elif godine>18:
#     print("Ti si odrasla osoba!")
    
# -------------------------------

# proveriti da li je uneti broj paran ili neparan

# broj=int(input("Unesite neki broj: "))

# if broj%2==0:
#     print("Broj je paran!")
# else:
#     print("Broj je neparan!")

# -------------------------------

# kada unesemo broj treba da nam prikaze mesec

# broj=int(input("Unesite neki broj od 1 do 12: "))

# if broj==1:
#     print("Januar!")
# elif broj==2:
#     print("Februar!")
# elif broj==3:
#     print("Mart!")
# elif broj==4:
#     print("April!")
# elif broj==5:
#     print("Maj!")
# elif broj==6:
#     print("Jun!")
# elif broj==7:
#     print("Jul!")
# elif broj==8:
#     print("Avgust!")
# elif broj==9:
#     print("Septembar!")
# elif broj==10:
#     print("Oktobar!")
# elif broj==11:
#     print("Novembar!")
# elif broj==12:
#     print("Decembar!")

# ------------------------------

# kalkulator

# broj_1=int(input("Unesite broj: "))
# broj_2=int(input("Unesite broj: "))
# operacija=str(input("Izaberite operaciju sabiranja, oduzimanja, mnozenja ili deljenja: "))

# if operacija=="+":
#     print(broj_1+broj_2)
# elif operacija=="-":
#     print(broj_1-broj_2)
# elif operacija=="*":
#     print(broj_1*broj_2)
# elif operacija=="/":
#     print(broj_1/broj_2)

# --------------------------------

# Homework 1

# rec=str(input("Unesite neku rec: "))
# uneta_rec=rec.lower()
# print(uneta_rec)
# brojac=0
# vokali=["a","e","i","o","u"]

# for sent in uneta_rec:
#     if sent in vokali:
#         brojac=brojac+1

# print("Broj samoglasnika u reci je:", brojac)


# Homework 2

# print("--------------------------")

# broj=int(input("Unesite neki broj: "))

# if broj%6==0:
# if broj%2==0 and broj%3==0:
#     print("Broj je deljiv sa 6")
# else:
#     print("Broj nije deljiv sa 6")

#-------------------------------------------------------------------------------

# rec=str(input("Unesite neku rec: "))

# if "a" in rec or "e" in rec or "i" in rec:
#     print("Nalazi se ")
# else:
#     print("Ne nalazi se ")

# --------------------------

# pretvaranje jednog tipa podatka u drugi
# var=6.45
# print(int(var))
# print(str(var))
# print(bool(var))

# print(type(var)) - proveravanje tipa 
# python casting on w3 school
# ------------------------------

# unesemo tri stranice i proverimo da li je trougao jednakostranican jedankokraki i da li uopste postoji 

# stranica_a=int(input("Unesite stranicu a: "))
# stranica_b=int(input("Unesite stranicu b: "))
# stranica_c=int(input("Unesite stranicu c: "))

    
# if (stranica_a+stranica_b)>stranica_c:
#     print("Trougao postoji!") 
#     if stranica_a==stranica_b==stranica_c:
#         print("Jedankostranicni!")
#     elif stranica_a!=stranica_b!=stranica_c:
#         print("Raznostrani")
#     elif (stranica_a==stranica_b)!=stranica_c or (stranica_a==stranica_c)!=stranica_b or (stranica_c==stranica_b)!=stranica_a:
#         print("Jednakokraki")
# else:
#     print("Trougao ne postoji")
    
#---------------------------------------

# uneti rec putem terminala, da li je prvo pocetno slovo veliko, ako nije da se ispise
# rez= rec.replace(rec[0], rec[0].upper())



# rec=str(input("Unesite neku rec: "))

# if rec[0]==rec[0].upper():
#     print("uneli ste tacno")
# else: 
#     rec=rec.replace(rec[0], rec[0].upper())
#     print(rec)

# ------------------------------------
# uneti br putem terminala, 3-fizz, 5-buzz, 3,5-fizzbuzz, ukoliko nije deljiv ispise samo taj broj

# broj=int(input("Unesite neki broj: "))

# if broj%3==0 and broj%5==0:
#         print ("FIZZBUZZ")
# elif broj%3==0:
#     print("FIZZ")
# elif broj%5==0:
#         print("BUZZ")
# else:
#     print(broj)

# ----------------------------------------------------------------------------------------------