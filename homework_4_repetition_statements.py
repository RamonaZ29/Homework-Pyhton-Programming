# Exerciții OBLIGATORII - grad de dificultate: Usor spre Mediu .
# 1.Având lista:
# mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
# 'Fiat', 'Trabant', 'Opel']
# Folosește un for că să iterezi prin toată lista și să afișezi;
# ● ‘Mașina mea preferată este x’.
# ● Fă același lucru cu un for each.
# ● Fă același lucru cu un while.
# REZOLVARE:

# FOR
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# for i in range(len(masini)):
#     print(f'Masina mea preferata este {masini[i]}')

# FOR EACH
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# for masina in masini:
#     print(f'Masina mea preferata este {masina}')

# WHILE
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# i = 0
# while i < len(masini):
#     print(f'Masina mea preferata este {masini[i]}')
#     i += 1

# 2. Aceeași listă:
# Folosește un for else
# În for
# - Modifică elementele din listă astfel încât să fie scrie cu majuscule,
# exceptând primul și ultimul.
# În else:
# - Printează lista.
# REZOLVARE:
# FOR ELSE
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# for i in range(1,len(masini)-1):
#         masini[i] = masini[i].upper()
# else:
#     print(f'Noua lista de masini va fi {masini}')

# 3. Aceeași listă:
# Vine un cumpărător care dorește să cumpere un Mercedes.
# Itereaza prin ea prin modalitatea aleasă de tine.
# Dacă mașina e mercedes:
# Printează ‘am găsit mașina dorită de dvs’
# Ieși din ciclu folosind un cuvânt cheie care face acest lucru
# Altfel:
# Printează ‘Am găsit mașina X. Mai căutam‘
# REZOLVARE:
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# for masina in masini:
#     if masina == 'Mercedes':
#         print('Am găsit mașina dorită de dvs')
#         break
#     else:
#         print(f'Am gasit masina {masina}. Mai cautam.')

# 4. Aceași listă;
# Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
# excepția Trabant și Lăstun.
# - Dacă mașina e Trabant sau Lăstun:
# Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
# else).
# - Printează S-ar putea să vă placă mașina x.
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# for masina in masini:
#     if masina == 'Lăstun' or masina == 'Trabant': # e corect asa?
#         continue
#     print(f'S-ar putea sa va placa masina {masina}.')

# 5. Modernizează parcul de mașini:
# ● Crează o listă goală, masini_vechi.
# ● Itereaza prin mașini.
# ● Când găsesti Lăstun sau Trabant:
# - Salvează aceste mașini în masini_vechi.
# - Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
# ● Printează Modele vechi: x.
# ● Modele noi: x.
# REZOLVARE:
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# masini_vechi = []
# for i in range(len(masini)):
#     if masini[i] in ['Lăstun','Trabant']:
#         masini_vechi.append(masini[i])
#         masini[i] = 'Tesla'
# print(f'Masini vechi: {masini_vechi}')
# print(f'Masini noi: {masini}')

# 6. Având dict:
# pret_masini = {
# 'Dacia': 6800,
# 'Lăstun': 500,
# 'Opel': 1100,
# 'Audi': 19000,
# 'BMW': 23000
# }
# Vine un client cu un buget de 15000 euro.
# ● Prezintă doar mașinile care se încadrează în acest buget.
# ● Itereaza prin dict.items() și accesează mașina și prețul.
# ● Printează Pentru un buget de sub 15000 euro puteți alege mașină
# xLastun
# ● Iterează prin listă.
# REZOLVARE:
# masini_in_buget = []
# pret_masini = {
# 'Dacia': 6800,
# 'Lăstun': 500,
# 'Opel': 1100,
# 'Audi': 19000,
# 'BMW': 23000
# }
# for cheie , valoare in pret_masini.items() :
#     if  valoare <= 15000:
#         print(f'Pentru un buget de 15000 euro puteti alege : {cheie}')

# 7. Având lista:
# numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# ● Iterează prin ea.
# ● Afișează de câte ori apare 3 (nu ai voie să folosești count).
# REZOLVARE:
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# count = 0
# for i in numere:
#     if i == 3:
#         count = count + 1
#     else:
#         continue
# print(count)

# 8. Aceeași listă:
# ● Iterează prin ea
# ● Calculează și afișează suma numerelor (nu ai voie să folosești sum).
# REZOLVARE:
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# suma = 0
# for numar in numere:
#     suma += numar
# print(suma)

# 9. Aceeași listă:
# ● Iterează prin ea.
# ● Afișază cel mai mare număr (nu ai voie să folosești max).
# REZOLVARE:
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# numar_maxim = numere[0]
# for i in numere:
#     if i > numar_maxim:
#         numar_maxim = i
# print(f'Cel mai mare numar este: {numar_maxim}')

# 10. Aceeași listă:
# ● Iterează prin ea.
# ● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
# Ex: dacă e 3, să devină -3
# ● Afișază noua listă.
# REZOLVARE:
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# numere_cu_semn_opus = []
# for i in numere:
#     if i > 0:
#         numere_cu_semn_opus.append(-i)
#     else:
#         numere_cu_semn_opus.append(-(i))
# print(numere_cu_semn_opus)

# Exerciții OPTIONALE - grad de dificultate: Mediu spre greu: may need Google.
# 1.
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# Itereaza prin listă alte_numere
# Populează corect celelalte liste
# Afișeaza cele 4 liste la final
# # REZOLVARE:
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# for i in alte_numere:
#     if i % 2 == 0:
#         numere_pare.append(i)
#     else:
#         numere_impare.append(i)
#     if i >= 0:
#         numere_pozitive.append(i)
#     else:
#         numere_negative.append(i)
# print(f'Lista numere pare: {numere_pare}')
# print(f'Lista numere impare: {numere_impare}')
# print(f'Lista numere pozitive: {numere_pozitive}')
# print(f'Lista numere negative: {numere_negative}')


# 2. Aceeași listă:
# Ordonează crescător lista fară să folosești sort.
# REZOLVARE:
#CU BUBBLE SORT CU VARIABILA SWAP
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# for i in range(len(alte_numere)-1):
#     for j in range(i+1,len(alte_numere)-1):
#         if alte_numere[i] > alte_numere[j]:
#             swap = alte_numere[i]
#             alte_numere[i] = alte_numere[j]
#             alte_numere[j] = swap
# print(f'Lista sortata este : {alte_numere}')
#sau
# Ordonează crescător lista fară să folosești sort.
# REZOLVARE:
#CU BUBBLE SORT FARA VARIABILA SWAP
#CU BUBBLE SORT CU VARIABILA SWAP
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# for i in range(len(alte_numere)-1):
#     for j in range(i+1,len(alte_numere)-1):
#         if alte_numere[i] > alte_numere[j]:
#             swap = alte_numere[i]
#             alte_numere[i],alte_numere[j] = alte_numere[j],alte_numere[i]
#             alte_numere[j] = swap
# print(f'Lista sortata este : {alte_numere}')

# 3. Ghicitoare de număr:
# numar_secret = Generați un număr random între 1 și 30
# Numar_ghicit = None
# Folosind un while
# User alege un număr
# Programul îi spune:
# ● Nr secret e mai mare
# ● Nr secret e mai mic
# ● Felicitări! Ai ghicit!
# REZOLVARE:
#import random
# numar_ghicit = int(input('Introdu un un nr intre 1 si 30:'))
# numar_secret = random.randint(1, 30)
# print(numar_secret)
# while numar_ghicit == numar_secret:
#     print('Ai ghicit nr!')
#     break #NU SUNT SIGURA CA TREBUIE BREAK AICI CA MERGE SI FARA
# if numar_ghicit > numar_secret:
#     print('Nr secret e mai mic!')
# else:
#     print('Nr secret e mai mare!')

# 4. Alege un număr de la tastatură
# Ex: 7
# Scrie un program care să genereze în consolă următoarea piramidă
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# Ex:3
# 1
# 22
# 333
# REZOLVARE:
# rows = int(input('Introdu un un nr natural mai mare ca 0 :'))
# for i in range(rows+1): # loop exterior
#     for j in range(i): # loop continut (interior) -for in for
#         print(i,end='') # afiseza numarul
#     print('') # linie noua dupa fiecare sir de numere

# 5.
# tastatura_telefon = [
# [1, 2, 3],
# [4, 5, 6],
# [7, 8, 9],
# [0]
# ]
# Iterează prin listă 2d
# Printează ‘Cifra curentă este x’
# (hint: nested for - adică for în for)
# REZOLVARE
# tastatura_telefon = [
# [1, 2, 3],
# [4, 5, 6],
# [7, 8, 9],
# [0]
# ]
# for i in range(len(tastatura_telefon)):
#     for j in range(len(tastatura_telefon[i])):
#         print(f'Cifra curenta este {tastatura_telefon[i][j]}') #




