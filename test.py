 
# 2. Tipovi podataka u Pythonu:
#     -prosti
#     -slozeni
# Prosti: 
#   -int-intiger-ceo broj
#   -float-decimalni broj
#   -bool- boolean- true/False
#   -str-string-niz karaktera
# -----------------------------------
# 4. 

# n=int(input("Unesite neki broj: "))
# for i in range(1,11):
#     print(n, "x", i, "=", i*n)

# ----------------------------------- 
# 3.
   
# for i in range(1,10):
#     print(str(i)*i)

# -----------------------------------
# 5. 
 
# broj_1=int(input("Unesite neki broj: "))
# broj_2=int(input("Unesite neki broj: "))
# operacija=str(input("Unesite neku od aritmetickih operacija: +, -, *, / :  "))

# if operacija=="+":
#     print( broj_1, "+", broj_2, "=", broj_1+broj_2)
# elif operacija=="-":
#     if broj_1<0:
#         print( broj_2, "-", broj_1, "=", broj_2-broj_1)
#     else:
#         print( broj_1, "-", broj_2, "=", broj_1-broj_2)
# elif operacija=="*":
#     print( broj_1, "*", broj_2, "=", broj_1*broj_2)
# elif operacija=="/":
#     if broj_1<0:
#         print( broj_2, "/", broj_1, "=", broj_2/broj_1)
#     else:
#         print( broj_1, "/", broj_2, "=", broj_1/broj_2)    
#  ---------------------------------------------------------   # 
# 6. 

# print(not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)
#          False  i  True 
#                     False ili False
#                               False i True
#                                       False i True       
#                                               False ili False
#                                                              False
# #                   
# print(1 > 1 or 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6) 
#        False ili True
#                 True ili False
#                         True i True
#                                 True i True
#                                     True ili False 
#                                                True
# ----------------------------------------------------------  
# 7. 

# rec=str(input("Unesite neku rec: "))

# if rec[0]==rec[0].upper():
#     print("uneli ste tacno")
# else: 
#     rec=rec.replace(rec[0], rec[0].upper())
#     print(rec)
# ------------------------------------------------------
# 8.

# for i in range(1,51):
#     if i%3==0 and i%5==0:
#         print("fizzbuzz")
#     elif i%5==0:
#         print("buzz")
#     elif i%3==0:
#         print("fizz")
#     else:
#         print(i)
# ----------------------------------------------------
# 9. 

# for i in range(100,401,2):
#     print(i, end=", ")
# ------------------------------------------------