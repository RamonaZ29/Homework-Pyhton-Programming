#import math
# Exerciții obligatorii - grad de dificultate: Usor spre Mediu .
# 1.Funcție care să calculeze și să returneze suma a două numere
# REZOLVARE
# def suma_a_doua_numere(a,b):
#     suma = a + b
#     return suma
# print (suma_a_doua_numere(5,28))
# print(suma_a_doua_numere(-8,13.4))

# 2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar
# REZOLVARE:
# def par_impar(numar):
#     if numar % 2 == 0:
#         return True
#     else:
#         return False
# print(par_impar(778))
# print(par_impar(-8.99))

# 3. Funcție care returnează numărul total de caractere din numele tău complet.
# (nume, prenume, nume_mijlociu)
# REZOLVARE:
# def calcul_numar_caractere(nume,prenume_1,prenume_2):
#     nr_caractere = len(nume) + len(prenume_1) + len(prenume_2)
#     return nr_caractere
# print(calcul_numar_caractere('Zoicas','Ramona','Bianca'))
# print(calcul_numar_caractere('Abroham','Ioan','3ugen'))
# CUM OFER POSIBILITATEA UTILIZARII FUNCTIEI PT CEI CE AU DOAR UN PRENUME?

# 4. Funcție care returnează aria dreptunghiului
# REZOLVARE:
# def aria_dreptunghiului(lungime, latime):
#     aria_dr = lungime*latime
#     return aria_dr
# print(aria_dreptunghiului(25,5))
# print(aria_dreptunghiului(13.4,3))

# 5. Funcție care returnează aria cercului
# REZOLVARE:
# VARIANTA 1
# def aria_cercului(raza,pi=3.14):
#     aria_cerc = pi*(raza**2)
#     return aria_cerc
# print(aria_cercului(5))
# print(aria_cercului(12.3))
# VARIANTA 2
# def arie_cerc(raza):
#     arie = math.pi*(raza**2)
#     return arie
# print(arie_cerc(3.14))
# print(arie_cerc(7))
# CUM E MAI CORECT 1-A VARIANTA SAU CU IMPORT.MATH?

# 6. Funcție care returnează True dacă un caracter x se găsește într-un string dat
# și False dacă nu găsește.
# REZOLVARE:
#VARIANTA 1
# def find_character(string,caracter):
#     if string.find(caracter)>0:
#         return True
#     else:
#         return False
# print(find_character('Ana are mere.','c'))
# print(find_character('3276472tgfdvhvvdhcbj','j')) #DE CE NU GASESTE PRIMUL CARACTER, CHIARA DACA EL EXISTA: EX -
# NU ILGASESTE PE 3
#VARIANTA 2
# def find_character(string,caracter):
#     if caracter in string:
#         return True
#     else:
#         return False
# print(find_character('3i3u5eihfjkgn','3'))
# print(find_character('Ana are mere.','c'))

# 7. Funcție fără return, primește un string și printează pe ecran:
# ● Nr de caractere lower case este x
# ● Nr de caractere upper case exte y
# REZOLVARE:
# def lowercase_and_uppercase_counting(string):
#     uppercase = 0
#     lowercase = 0
#     others = 0
#     for letter in string:
#         if letter.isupper():
#             uppercase += 1
#         elif letter.islower():
#             lowercase += 1
#         else:
#             others += 1
#     print(uppercase)
#     print(lowercase)
#     print(others)
# print(lowercase_and_uppercase_counting('Love'))
# print(lowercase_and_uppercase_counting('Mercredi3 and Jeudi$'))
# DE CE PRINTEAZA NONE DUPA NR CARACTERELOR?

# 8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu
# numerele pozitive
# REZOLVARE:
# def lista_cu_numere_pozitive(list_of_numbers):
#     list_of_positive_numbers=[]
#     for number in list_of_numbers:
#         if number >=0:
#             list_of_positive_numbers.append(number)
#     return list_of_positive_numbers
# print(lista_cu_numere_pozitive([3,5,-2]))
# print(lista_cu_numere_pozitive([-45665,670,0]))
# SUGESTIE VARIANTA CU *ARGS!
# def lista_cu_numere_pozitive(*args):
#     list_of_positive_numbers = []
#     for i in [*args]: # AICI DE RETINUT CA *args il pune in paranteze patrate [] ca sa returneze o lista cu nr pozitive
#         if i >=0:
#             list_of_positive_numbers.append(i)
#     return list_of_positive_numbers
# print(lista_cu_numere_pozitive(3,5,-2))
# print(lista_cu_numere_pozitive(-45665,670,0))

# 9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
# ● Primul număr x este mai mare decat al doilea nr y
# ● Al doilea nr y este mai mare decat primul nr x
# ● Numerele sunt egale.
# REZOLVARE:
# def compararea_a_2_numere(x,y):
#     if x>y:
#         print(f'Primul număr {x} este mai mare decat al doilea nr {y}')
#     elif y>x:
#         print(f'Al doilea număr {y} este mai mare decat primul nr {x}')
#     else:
#         print('Numerele sunt egale.')
# print(compararea_a_2_numere(-7.5,-4))
# print(compararea_a_2_numere(3,3))
# DE CE NONE DUPA PRINT?

# 10. Funcție care primește un număr și un set de numere.
# ● Printeaza ‘am adaugat numărul nou în set’ + returnează True
# ● Printeaza ‘nu am adaugat numărul
# REZOLVARE:
# def numar_in_set_de_numere(numar,set_numere):
#     if numar not in set_numere :
#         print('am adaugat numărul nou în set')
#         return True
#     else:
#         print('nu am adaugat numarul')
# print(numar_in_set_de_numere(5,{3,6,7}))
# print(numar_in_set_de_numere(5,{5,8,-214.4}))
# WHY 'NONE' DACA INTRA PE ELSE?




# Exerciții OPTIONALE - grad de dificultate: Mediu spre greu: may need Google.
# 1. Funcție care primește o lună din an și returnează câte zile are acea luna
# REZOLVARE:
# from calendar import monthrange
# def zile_in_luna(year,month):
#     return monthrange(year,month) [1] # se trece in paranteza [1] numarul primei luni?-asa am gasit pe google
# print(zile_in_luna(2023,2))
# print(zile_in_luna(2020,2))


# 2. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea,
# împărțirea a două numere.
# În final vei putea face:
# a, b, c, d = calculator(10, 2)
# ● print("Suma: ", a)
# ● print("Diferenta: ", b)
# ● print("Inmultirea: ", c)
# ● print("Impartirea: ", d)
# REZOLVARE:
# def calculator(x,y):
#     a = x + y
#     b = x- y
#     c = x * y
#     d = x/y
#     return a,b,c,d
# a,b,c,d = calculator(4,2)
# print('Suma: ', a)
# print('Diferenta: ', b)
# print('Inmultirea: ', c)
# print('Impartirea: ', d)
# a,b,c,d = calculator(-7.5,3)
# print('Suma: ', a)
# print('Diferenta: ', b)
# print('Inmultirea: ', c)
# print('Impartirea: ', d)


# 3. Funcție care primește o lista de cifre (adică doar 0-9)
# Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
# Returnează un DICT care ne spune de câte ori apare fiecare cifră
# => dict {
# 0: 0
# 1 :2
# 2: 0
# 3: 1
# 4: 0
# 5: 3
# 6: 0
# 7: 2
# 8: 0
# 9: 1
# }
# REZOLVARE:
# def lista_de_cifre_care_returneaza_dict(lista_cifre):
#     dict = {}
#     for i in range(10):
#         dict[i] = lista_cifre.count(i)
#     return dict
# print(lista_de_cifre_care_returneaza_dict([3,4,5,3,1,0]))
# print(lista_de_cifre_care_returneaza_dict([6,9,-6,0,7,10]))
# CUM FAC SA APARA LA RETURN ,UNA SUB ALTA?


# 4. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele
# REZOLVARE:
# VARIANTA 1
# def max_from_3_numbers(a,b,c):
#     return max(a,b,c)
# print(max_from_3_numbers(133,54,-4))
# print(max_from_3_numbers(3534.66,0,4))
# sau
# VARIANTA 2:
# def max_from_3_numbers(a,b,c):
#     if a>b and a>c:
#         return a
#         print(f'valoarea maxima introdusa este {a}')
#     elif b>a and b>c:
#         return b
#         print(f'valoarea maxima introdusa este {b}')
#     elif c>a and c>b:
#         return c
#         print(f'valoarea maxima introdusa este {c}')
#     else:
#         print('Introduceti numere valide si diferite!')
# print(max_from_3_numbers(133,54,-4))
# print(max_from_3_numbers(3534.660,0,4))


# 5. Funcție care să primească un număr și să returneze suma tuturor numerelor
# de la 0 la acel număr
# Exemplu: daca dam nr 3. Suma va fi 6 (0+1+2+3)
# REZOLVARE:
# def sum_all_numbers_in_a_range(x):
#     total= sum(range(x+1))
#     return total
# print(sum_all_numbers_in_a_range(3))
# print(sum_all_numbers_in_a_range(6))


# Exerciții Opționale - BONUS
# 1.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați
# numerele comune
# Exemplu:
# list1 = [1, 1, 2, 3]
# list2 = [2, 2, 3, 4]
# Răspuns: {2, 3}
# VARIANTA 1( SET'S INTERSECTION PROPERTY)
# def intersectia_a_2_liste_de_numere(list1,list2):
#     elemente_list1 = set(list1)
#     elemente_list2 = set(list2)
#     if (elemente_list1 & elemente_list2):
#         print(elemente_list1 & elemente_list2)
#         return (elemente_list1 & elemente_list2)
#     else:
#         print("No common elements")
# print(intersectia_a_2_liste_de_numere([1,1,2,3],[1,2,8,3]))
# OR
# def intersectia_a_2_liste_de_numere(list1,list2):
#     return list(set(list1).intersection(list2)) #LIST e din settings pt a arata structura de date returnata!
# print(intersectia_a_2_liste_de_numere([1,1,2,3],[1,2,8,3]))
# VARIANTA 2 (FOR LOOP)
# def intersectia_a_2_liste_de_numere(list1,list2):
#     result = [i for i in list1 if i in list2] # am gasit-o pe net.  E SYNTAXA?
#     return result
# print(intersectia_a_2_liste_de_numere([1,1,2,3],[1,2,8,3]))
# VARIANTA 3 (USING COLLECTIONS)
# import collections
# def intersectia_a_2_liste_de_numere(list1,list2):
#     result = collections.Counter(list1) & collections.Counter(list2)
#     return result.keys()
# print(intersectia_a_2_liste_de_numere([1,1,2,3],[1,2,8,3]))


# 2.. Funcție care să aplice o reducere de preț
# Dacă produsul costa 100 lei și aplicăm reducere de 10%. Pretul va fi 90
# Tratați cazurile în care reducerea e invalida. De exemplu o reducere de 110% e
# invalidă.
# REZOLVARE:
# def aplica_reducere_de_pret(pret_initial,reducere):
#     if reducere<100 and reducere>0:
#         pret_final = pret_initial - (pret_initial * reducere/100)
#         return pret_final
#     else:
#         print('Reducerea introdusa e invalida!')
# print(aplica_reducere_de_pret(800,10))
# print(aplica_reducere_de_pret(800,110))
# print(aplica_reducere_de_pret(800,-10))


# 3. Funcție care să afișeze data și ora curentă din ro
# (bonus: afișați și data și ora curentă din China)
# REZOLVARE:
#from _datetime import datetime,date #FOR NOW
#import pytz #FOR TIMEZONE
# def current_date_and_time_RO():
#     timezone = pytz.timezone('Europe/Bucharest')
#     data = date.today()
#     now = datetime.now().strftime('%H:%M:%S')
#     return data, now
# print(current_date_and_time_RO())
#
# def date_and_time_China():
#     timezone = pytz.timezone('Asia/Shanghai')
#     data = pytz.datetime.date.today()
#     now = datetime.now(timezone).strftime('%H:%M:%S')
#     return data, now
# print(date_and_time_China())


# 4. Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la
# Crăciun dacă nu vrei să ne zici cand e ziua ta :)
# REZOLVARE:
# import datetime
# def counting_days_till_my_Bday():
#     dt = datetime.datetime
#     now = dt.now()
#     time_left = dt(year=2023,month=9,day=29) - dt(year=now.year, month=now.month, day=now.day)
#     return time_left.days
# print(counting_days_till_my_Bday()
