# Tipovi podataka: prosti i slozeni 
# varijable sa celim brojem - int - intiger
# brojevi sa decimalama - float 
# bool - true/false
# string - niz karaktera

# print - ispis necega u terminalu
# pretvaranje iz jednog tipa u drugi
# type


# Operatori
# -aritmeticki operatori (+ - * / % **)
#- relacijski-rezultat je uvek bool- (<><=>=, ==, != )
#- operatori za dodelu vrednosti - += -=

#Logicki operator - true/false
# and-true if both of them are true, za povezivanje izraza
# or- true if either one of them are true, 
# not - not true-false, not false-true, 
# povezivanje nam se vrsi uz pomoc logickih operatora 

# Metode stringa:
# -indeksiranje 0123456789
# -indeksiranje sa minusom -1 -2 -3 -4 -5 -6 -7 -8 -9 (zadnji broj ima indeks -1)
# -replace - sluze za zamenjivanje
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
# print(skola[-5 ::-1 ])
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

# len replace  upper lower[ : :-1]

#-----------------------------------------------------------------------------------------------
#pocetna krajnja vrednost
#i nam je kao brojac broji br ponavljanja
#for i in range(1,10,2)

# for i in range(10):
#     print("cao")
# #---------------------
# for i in range(1,10):
#     print(i)
# #--------------------
# for i in range(10,1,-1):
#     print(i)
#ispisuje unazad
#--------------------

# Ispisati brojeve od 1 do 100, ali samo parne brojeve

# for i in range(0,101,2):
#     print(i)
#for i in range(1,100):
#   if i%2==0:
# print(i)

#----------------------

# #prolazak kroz stringove i reci
# rec="pajton"
# for i in rec:
#     print(i)
#----------------------
# rec="pajton"
# for i in range(len(rec)):
    # print(rec[i])  
    # print(i)
#----------------------

# Napisati program koji ce da ispise zbir sumu prvih 100 brojeva
# sum = 0. for i in range(1, 101): sum = sum + i. print(sum) ...

# sum=0
# for i in range(1, 101):
#     sum+=i
# print(sum)
    
#----------------------

# faktorijal unetog broja 
# 4!=4*3*2*1

# broj= int(input("Unesite neki broj: "))
# fakt=1
# for i in range(broj,0,-1):
#     fakt*=i
# print(fakt)

# --------------------------------
# zbir kvadrata i kvadrat zbira

# zbir_kvadrata=0
# kvadrat_zbira=0

# for i in range(1,101):
#     kvadrat_zbira+=i
#     zbir_kvadrata+=i**2
# print(zbir_kvadrata**2-kvadrat_zbira)
# -------------------------------------------------------------------------------

# for i in range(1,51):
#     if i%3==0 and i%5==0:
#         print("fizzbuzz")
#     elif i%3==0:
#         print("fizz")
#     elif i%5==0:
#         print("buzz")
#     else:
        # print(i)
# ------------------------------
# ispisati sve kvadrate brojeva od 1 do n

# broj=int(input("Unesite broj: "))

# for i in range(1,broj):
#     print("Kvadrat broja ", i, "je ", i**2)


# ---------------------------------------------------------------------------------------------------------

# for i in range(1,10):
#         print(str(i)*i) 

# 1 * 1
# 2 * 2
# 3 * 3

# -------------------------------


# n=int(input("Unesite broj: "))

# for i in range(1,11):
#     print(f"{n} x {i} = {n*i}")
# ------------------------------------

# f-string
# print(f"{n}x {i} = {n*i}")
# ------------------------------------

# for i in range(1,10):
    # for j in range(1,10):
        # print(i,j)
# # -----------------------------------
# print("----------------------------------------------------------------------")
# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j, end="\t")
#     print()
# print("----------------------------------------------------------------------")

# --------------------------------
# n=0
# for i in range(1,1000):
#     if i%3==0 or i%5==0:
#         n+=i
# print(n)
# # --------------------------------------------------------------------------------------------------------
# [ : : ]-bice na testu

# n=0
# for i in range(1,1001):
#     n=n+i**i
# print(str(n)[-10::1])
# ---------------------------------


# broj=int(input("Unesite broj: "))
# sum=0

# for i in str(broj):
#     sum+=int(i)
# print(sum)
    
# ----------------------------------------

# continue-preskace ako je neki br jednak nekom br
# break-do tu radi for ptlja

# projcentureler

# for if else elif operatori and or not [::]


# for a in range(1,1000):
#     for b  in range(1,1000):
#         for c in range(1,1000):
#             if a<b<c and a**2+b**2==c**2 and a+b+c==1000:
#                 print(a*b*c)
#                 break
# --------------------------------------------------------------------------------------------

# liste, matrice, append, remove, sort, extend, nizovi, pop, insert, clear:

#             
# =======
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
# print(skola[-5 ::-1 ])
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

# len replace  upper lower[ : :-1]

#-----------------------------------------------------------------------------------------------
#pocetna krajnja vrednost
#i nam je kao brojac broji br ponavljanja
#for i in range(1,10,2)

# for i in range(10):
#     print("cao")
# #---------------------
# for i in range(1,10):
#     print(i)
# #--------------------
# for i in range(10,1,-1):
#     print(i)
#ispisuje unazad
#--------------------

# Ispisati brojeve od 1 do 100, ali samo parne brojeve

# for i in range(0,101,2):
#     print(i)
#for i in range(1,100):
#   if i%2==0:
# print(i)

#----------------------

# #prolazak kroz stringove i reci
# rec="pajton"
# for i in rec:
#     print(i)
#----------------------
# rec="pajton"
# for i in range(len(rec)):
    # print(rec[i])  
    # print(i)
#----------------------

# Napisati program koji ce da ispise zbir sumu prvih 100 brojeva
# sum = 0. for i in range(1, 101): sum = sum + i. print(sum) ...

# sum=0
# for i in range(1, 101):
#     sum+=i
# print(sum)
    
#----------------------

# faktorijal unetog broja 
# 4!=4*3*2*1

# broj= int(input("Unesite neki broj: "))
# fakt=1
# for i in range(broj,0,-1):
#     fakt*=i
# print(fakt)

# --------------------------------
# zbir kvadrata i kvadrat zbira

# zbir_kvadrata=0
# kvadrat_zbira=0

# for i in range(1,101):
#     kvadrat_zbira+=i
#     zbir_kvadrata+=i**2
# print(zbir_kvadrata**2-kvadrat_zbira)
# -------------------------------------------------------------------------------

# for i in range(1,51):
#     if i%3==0 and i%5==0:
#         print("fizzbuzz")
#     elif i%3==0:
#         print("fizz")
#     elif i%5==0:
#         print("buzz")
#     else:
        # print(i)
# ------------------------------
# ispisati sve kvadrate brojeva od 1 do n

# broj=int(input("Unesite broj: "))

# for i in range(1,broj):
#     print("Kvadrat broja ", i, "je ", i**2)


# ---------------------------------------------------------------------------------------------------------

# for i in range(1,10):
#         print(str(i)*i) 

# 1 * 1
# 2 * 2
# 3 * 3

# -------------------------------


# n=int(input("Unesite broj: "))

# for i in range(1,11):
#     print(f"{n} x {i} = {n*i}")
# ------------------------------------

# f-string
# print(f"{n}x {i} = {n*i}")
# ------------------------------------

# for i in range(1,10):
    # for j in range(1,10):
        # print(i,j)
# # -----------------------------------
# print("----------------------------------------------------------------------")
# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j, end="\t")
#     print()
# print("----------------------------------------------------------------------")

# --------------------------------
# n=0
# for i in range(1,1000):
#     if i%3==0 or i%5==0:
#         n+=i
# print(n)
# # --------------------------------------------------------------------------------------------------------
# [ : : ]-bice na testu

# n=0
# for i in range(1,1001):
#     n=n+i**i
# print(str(n)[-10::1])
# ---------------------------------


# broj=int(input("Unesite broj: "))
# sum=0

# for i in str(broj):
#     sum+=int(i)
# print(sum)
    
# ----------------------------------------

# continue-preskace ako je neki br jednak nekom br
# break-do tu radi for ptlja

# projcentureler

# for if else elif operatori and or not [::]


# for a in range(1,1000):
#     for b  in range(1,1000):
#         for c in range(1,1000):
#             if a<b<c and a**2+b**2==c**2 and a+b+c==1000:
#                 print(a*b*c)
#                 break
# --------------------------------------------------------------------------------------------

# niz= [
#     [1, 0, 0],
#     [0, 1, 0],
#     [0, 0, 1]
# ]
# flag=True
# for i in range(len(niz)):
#     for j in range(len(niz[i])):
#         if (i==j and niz[i][j] != 1) or (i != j and niz[i][j] != 0):
#             flag=False
#             break
# print(flag)

# petlje - omogucavaju nam da odredjeni deo koda ponavljamo vise puta, odredjeni i neodredjeni put 
# for petlje sa odredjenim br puta se ponavlja
# while moze i odredjeni i neodredjei br puta da se ponavlja 
# break - kod se prekida 
# continiue - nastavlja
# logicki operatori
# liste-podrzavaju duplikate, changeable, 
# while petlja - slabo se koristi 
# append - ubacuje el na kra niza
# sort
# extend - produziti
# matrice - liste u listama
# pop - pod odredjenim indeksom
# clear - ocistiti, izbrisati 
# remove- vrednost uklanja
# liste - varijable koje sadze niz karaktera 
# count - izracuvana koliko elemenata ima u nizu, obicno su to duplikati 


# niz=[2,3,7,6,2,4,9]
# parni=[]
# neparni=[]
# for i in niz:
#     if i%2==0 and i not in parni:
#         parni.append(i)
#     elif i%2!=0 and i not in neparni:
#         neparni.append(i)

# print([parni, neparni])

# ---------------------------------------------------------------

# dani=["mon", "tue", "wed", "thur", "fri"]
# indeksi=[1,3,4]
# res=[]

# for i in indeksi:
#     res.append(nizDana[i])
    

# for i in range (len(dana)):
#     for j in indeksi:
#         if i==j:
#             res.append(niz[i])

# print(res)
# ------------------------------------------------------------------
# ------------------------------------------------------------------
# setovi su neodredjeni indeksima, taplovi (tuple) su odredjeni indeksima, type

# x= ("apple", "cherry", "banana")

# y = list(x)

# y =   ["apple", "cherry", "banana"]
#           0         1         2

# y[1]= "kiwi"

# x = tuple(y)

# print(x)

# ----------------------------------------

# x= ("apple", "cherry", "banana")

# y=list(x)

# y.append("watermalon")

# x=tuple(y)

# print(x)

# ---------------------------------------

# dodavanje tuple-a na tuple
# tuple nema metode kao lista, i indeksiran je u odnosu na setove

# x=("apple", "cherry", "banana")
# y=("orange", "kiwi")
# x+=y
# print(x)

# -----------------------------
# fruits=("apple", "banana", "cherry")

# (green, yellow, red)=fruits

# print(green)
# print(red)
# print(yellow)

# # unpack tuple
# for petljom se prolazi na isti nacin kao kroz liste
# -------------------------------

# x=(1,2,3,4,56,3,3,21,2,33,4,2,8,2,2)

# y=x.count(2)
# # count nam sluzi da izbrojimo koliko ima duplikata u nekom tuple-u
# print(y)

# fruits=("apple", "banana", "cherry", "watermelon")

# if "apple" in fruits:
#     print("nalazi se")
# -------------------------------------------------------------



# -------------------------------------------------------------

# dictionary - dict -  objekti  - slozeni tipovi podataka - sluze da se smesti vise vrednosti
# imaju dve vrednosti:  1. key i 2. value

# dict={
#     "ime": "Maja",
#     "prezime": "plojovic",
#     "skola": True,
#     "godine": 18
# }


# print(dict["ime"])
# print(dict["godine"])

# ordered (indeksirane su) , changable, ne podrzavaju duplikate, mozemo for petljom da prolazimo kroz dict
# dict.value() - ispisuje vrednosti, dict.keys()-ispisuje kljucne reci, dict.items() - ispisuje sve redom
# kad zelimo da dodamo neki novi key u recniku, stavljamo ime varijable [ i unutra pod navodnicima stavljamo ime key]
# kad dodajemo novu vrednost samo napisemo dict["ime"]= "novo ime", i  ta rec ili ime se over ride-A 
# update- uz pomoc ovoga dodajemo i key i value od jednom

# for i in dict.values():
# for i in dict.keys():

    # print(i)
    # print(dict[i])

# recnik={
#     "prezime": "plojovic",
#     "skola": True,
#     "godine": 18,
#     "ime":"maja"
# }
# recnik["ime"]="osman"

# print(recnik)
# --------------------------------------------
# copilot

# nesto = dict()

# n= int(input("Unesite neki broj: "))


# for i in range(1,n+1):

#     n[i]=i**2


# print(n)


# --------------------------------------------
# ispisati vrednost od history = 80
# sampleDict={
#     "class": {
#         "students": {
#             "name":"petar",
#              "marks":{
#                 "math": 70,
#                 "history":80
#              }
#         }
#     }
# }


# print(sampleDict["class"]["students"]["marks"]["history"])

# ---------------------------------------------

# dict={
#     "emp1":{
#         "name":"petar", 
#         "salary":500
#     },

#     "emp2":{
#         "name":"marija",
#          "salary":600
#     },

#     "emp3":{
#         "name":"osman", 
#         "salary":400
#     }
# }

# for i in dict.values():
#     if i["name"]=="marija":
#         i["salary"]=1000
#         break
# print(dict)

# # ----------------------------------------------------------------------------
# DONE WITH PYTHON COURSE
# ------------------------------------------------------------------------------