#Tema_2- OPERATORI SI CONDITIONALE-
# 1. Explica cu cuv tale  cum fctioneaza un if else:
# RASPUNS
# If else - evalueaza conditii si bifurca codul in functie de rezultat (are 2 ramuri)

# 2. Verifică și afișează dacă x este număr natural sau nu.
# RASPUNS:
#  x = int(input('introdu un nr intreg:'))
#  if x >= 0:
#   print(f'numarul {x} este natural')
#  else:
#   print:(f'numarul {x} nu este natural')

# 3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
# RASPUNS:
# x = int(input('Introdu un nr intreg:'))
# if x > 0:
#     print(f'numarul {x} este pozitiv!')
# elif x < 0:
#     print('numarul {x} este negativ')
# else:
#     print(f'numarul {x} este neutru')

# 4. Verifică și afișează dacă x este între -2 și 13.
# RASPUNS:
# x = int(input('Introdu un nr intreg:'))
# if x < -2:
#     print(f'numarul {x} nu se afla in interval')
# elif x > 13:
#     print(f'numarul {x} nu este in interval')
# else:
#     print(f'numarul {x} se afla in interval')

# 5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5.
# RASPUNS:
# x = int(input('Introdu un nr intreg:'))
# y = int(input('Introdu un alt nr intreg:'))
# diferenta = x-y
# if diferenta < 5:
#     print(f'diferenta dintre {x} si {y} este {diferenta} si este mai mica de 5.')


# 6. Verifică dacă x NU este între 5 și 27 - a se folosi ‘not’.
# RASPUNS:
# x = int(input('Introdu un nr intreg:'))
# print(not 5<=x<=27)


# 7. x și y (int)
# Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai mare.
# RASPUNS:
# x = int(input('Introdu un nr intreg:'))
# y = int(input('Introdu un alt nr intreg:'))
# if x == y:
#     print(f'Numerele sunt egale')
# elif x < y:
#     print(f'Numarul {y} este mai mare.')
# else:
#     print(f'Numarul {x} este mai mare.')

# 8. x, y, z - laturile unui triunghi.
# Afișează dacă triunghiul este isoscel, echilateral sau oarecare.
# RASPUNS:
# x = int(input('Introdu dimensiunea primei laturi a triunghiului:'))
# if x <= 0:
#     print(int(input('Introduceti o valoare pozitiva:')))
# y = int(input('Introdu dimensiunea celei de-a doua laturi a triunghiului:'))
# if y <= 0:
#     print(int(input('Introduceti o valoare pozitiva:')))
# z = int(input('Introdu dimensiunea celei de-a treia laturi a triunghiului:'))
# if z <= 0:
#     print(int(input('Introduceti o valoare pozitiva:')))
# if x == y == z:
#     print('Triunghiul este echilateral!')
# elif x == y or x == z or y == z:
#     print('Triunghiul este isoscel!')
# else:
#     print('Triunghiul este oarecare!')

# 9. Citește o literă de la tastatură.
# Verifică și afișează dacă este vocală sau nu
# RASPUNS:
# x = str(input('Introduceti o litera:'))
# a = ('a')
# A = ('A')
# e = ('e')
# E = ('E')
# i = ('i')
# I = ('I')
# o = ('o')
# O = ('O')
# u = ('u')
# U = ('U')
# if x == a or x == A or x == e or x == E or x == i or x ==I or x == o or x == O or x == u or x == U:
#     print(f'litera {x} este vocala!')
# else:
#     print(f'litera {x} nu este vocala!')


# 10.Transformă și printează notele din sistem românesc în >
# Peste 9 => A
# Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 4 => E
# 4 sau sub => F
#REZOLVARE:
# x = float(input('Introduceti nota:'))
# if x <= 4 and x >= 1:
#     print(f'nota {x} se transforma in F')
# elif x > 4 and x <= 6:
#     print(f'nota {x} se transforma in E')
# elif x > 6 and x <= 7:
#     print(f'nota {x} se transforma in D')
# elif x > 7 and x <= 8:
#     print(f'Nota {x} se transforma in C')
# elif x > 8 and x <= 9:
#     print(f'nota {x} se transforma in B')
# elif x > 9 and x <= 10:
#     print(f'nota {x} se transforma in A')
# else:
#     print('Nu este o nota valida!')

# Exerciții OPTIONALE- grad de dificultate: Mediu spre greu -
# 1. Verifică dacă x are minim 4 cifre (x e int).
# (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
# RASPUNS:
# x = int(input('Introdu un nr intreg:'))
# nr_cifre = len(str(x))
# if nr_cifre >= 4:
#     print(f'Numarul introdus are {nr_cifre} cifre.')
# else:
#     print('Numarul introdus trebuie sa contina minim 4 cifre!')

# 2. Verifică dacă x are exact 6 cifre.
# RASPUNS:
# x = int(input('Introdu un nr intreg:'))
# count = len(str(x))
# if count == 6:
#     print('Numarul introdus are exact 6 cifre!')


# 3.Verifică dacă x este număr par sau impar (x e int).
# RASPUNS:
# x = int(input('Introdu un nr intreg:'))
# if (x % 2 == 0):
#     print(f'Numarul {x} este par!')
# else:
#     print(f'Numarul {x} este impar!')

# 4. x, y, z (int)
# Afișează care este cel mai mare dintre ele?
# RASPUNS:
# x = int(input('Introdu un nr intreg:'))
# y = int(input('Introdu al doilea nr intreg:'))
# z = int(input('Introdu al treilea nr intreg:'))
# print(f'Cel mai mare numar introdus este {max(x,y,z)}')


# 5. X, y, z - reprezintă unghiurile unui triunghi
# Verifică și afișează dacă triunghiul este valid sau nu.
# RASPUNS:
# x = int(input('Introdu dimensiunea unghiului x a triunghiului xyz'))
# if x < 0:
#     print('Introduceti valoare pozitiva!')
# else:
#     print(f'Unghiul x are {x} grade.')
# y = int(input('Introdu dimensiunea unghiului y a triunghiului xyz'))
# if y < 0:
#     print('Introduceti valoare pozitiva!')
# else:
#     print(f'Unghiul y are {y} grade.')
# z = int(input('Introdu dimensiunea unghiului z a triunghiului xyz'))
# if z < 0:
#     print('Introduceti valoare pozitiva!')
# else:
#     print(f'Unghiul z are {z} grade.')
# sum = x+y+z
# if sum == 180:
#     print('Triunghiul este valid!')
# else:
#     print('Suma unghiurilor triunghiului trebuie sa fie 180 de grade!')

# 6. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
# ● Citiți de la tastatură un int x
# ● Afișează stringul fără ultimele x caractere
# Exemplu: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte'
# RASPUNS:
# poezie = str('Coral is either the stupidest animal or the smartest rock')
# x = int(input('Introdu un nr intreg:'))
# if (x > len(poezie)) or x < 0:
#     print(f'Introduceti un nr mai mare ca 0 si mai mic decat {len(poezie)}')
# else:
#     print(poezie[:-x])

# 7. Același string. Declară un string nou care să fie format din primele 5 caractere + ultimele 5
# RASPUNS:
# poezie = str('Coral is either the stupidest animal or the smartest rock')
# poezie_noua = str(poezie[:5]) + str(poezie[-5:])
# print(poezie_noua)

# 8. Același string.
# ● Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint:
# este o funcție care te ajuta sa faci asta)
# ● Folosind această variabilă + slicing, afișează tot stringul până la acest
# cuvant
# ● output: 'Coral is either the stupidest animal or the smartest '
# RASPUNS:
# poezie = str('Coral is either the stupidest animal or the smartest rock')
# index_de_start = poezie.rfind('r')
# print(index_de_start)
# print(poezie[:index_de_start:])

# 9. Citește de la tastatura un string
# Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
# Atentie: se dorește ca programul sa fie case insensitive - 'apA' e acceptat
# RASPUNS:
# text = str(input('Introduceti un text :'))
# index0 = text[0]
# index_n = text[-1]
# print(index0+index_n)
# assert index0.lower() == index_n.lower()

# 10. Avand stringul '0123456789'
# ● Afișați doar numerele pare
# ● Afișați doar numerele impare
# (hint: folositi slicing, controlați din pas)
# RASPUNS:
# sir_numere = str('0123456789')
# print(sir_numere[::2])
# print(sir_numere[1::2])


#BONUS
# 11. Joc ghicit zarul
# Caută pe net și vezi cum se generează un număr random
# Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
# Luați un numărul ghicit de la utilizator
# Verificați și afișați dacă utilizatorul a ghicit
# Veți avea 3 opțiuni
# ● Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
# ● Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
# ● Ai ghicit. Felicitari! Ai ales x si zarul a fost y
# RASPUNS:
# import random din numpy
# x = int(input('Introduceti un numar de pe fetele zarului:'))
# print(x)
# dice_roll = random.randint(1,6)
# print(dice_roll)
# if x < dice_roll:
#     print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {x} dar a fost {dice_roll}')
# elif x > dice_roll:
#     print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {x} dar a fost {dice_roll}')
# else:
#     print(f'Ai ghicit. Felicitari! Ai ales {x} si zarul a fost {dice_roll}')


