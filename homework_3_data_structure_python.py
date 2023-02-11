# Exerciții OBLIGATORII - grad de dificultate: Usor spre Mediu
# 1. Declară o listă note_muzicale în care să pui do re mi etc până la do
# ● Afișeaz-o
# ● Inversează ordinea folosind slicing și suprascrie această listă.
# ● Printează varianta actuală (inversată).
# ● Pe această listă aplică o metodă care bănuiești că face același lucru,
# adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz,
# deoarece metoda face asta automat.
# ● Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta
# inițială.
# RASPUNS:
# note_muzicale = ['do','re','mi','fa','sol','la','si','do']
# print(note_muzicale)
# note_muzicale = note_muzicale[::-1]
# print(note_muzicale)
# new = list(reversed(note_muzicale))
# print(new)

# 2. De câte ori apare ‘do’?
# note_muzicale = ['do','re','mi','fa','sol','la','si','do']
# print(note_muzicale.count('do'))

# 3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
# Găsește 2 variante să le unești într-o singură listă.
# list_1 = [3, 1, 0, 2]
# list_2 = [6, 5, 4]
# lista_unita_var1 = list(list_1 + list_2)
# print(lista_unita_var1)
# lista_unita_var2 = [*list_1,*list_2]  # AM UTILIZAT METODA DESPACHETARII
# print(lista_unita_var2)

#  4.● Sortează și afișază lista generată la exercițiul anterior.
#     ● Elimina numărul 0 folosind o funcție.
#     ● Afișaza iar lista.
# lista_unita = [3, 1, 0, 2, 6,  4]
# lista_sortata = sorted(lista_unita)
# lista_unita = lista_sortata
# print(lista_sortata)
# print(lista_unita.remove(0))

# 5. Folosind un if verifică lista generată la exercițiul 3 și afișază:
# ● Lista este goală.
# ● Lista nu este goală.
# REZOLVARE:
# lista_unita = [0,1,2,3,4,5,6]
# if len(lista_unita) > 0:
#     print('Lista nu este goala!')
# else:
#     print('Lista este goala!')

# 6. Folosește o funcție care să șteargă lista de la exercițiul 3.
# lista_unita = [0,1,2,3,4,5,6]
# lista_unita.clear()
# print(lista_unita)

# 7. Copy paste la exercițiul 5. Verifică încă o dată.
# Acum ar trebui să se afișeze că lista e goală.
# if len(lista_unita) > 0:
#     print('Lista nu este goala!')
# else:
#     print('Lista este goala!') # da este goala daca nu suprascriu lista si o las lista_unita.clear[].

# 8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# Folosește o funcție că să afișezi Elevii (cheile)
# REZOLVARE:
# dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# print(dict1.keys())


# 9. Printează cei 3 elevi și notele lor
# Ex: ‘Ana a luat nota {x}’
# Doar nota o vei lua folosindu-te de cheie
# dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# REZOLVARE:
# for key , value in dict1.items():
#     print (f'{key} a luat nota {value}.')


# 10. Dorel a făcut contestație și a primit 6
# ● Modifică nota lui Dorel în 6
# ● Printează nota după modificare
# dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# dict1['Dorel'] = 6
# print(dict1)


# 11. Gigel se transferă din clasă
# ● Căuta o funcție care să îl șteargă
# ● Vine un coleg nou. Adaugă Ionică, cu nota 9
# ● Printează noii elevi
# REZOLVARE:
# dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# dict1.pop('Gigel')
# dict1['Ionut'] = 9
# print(dict1)


# 12.
# Set
# zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}
# ● Adaugă în zilele_sapt ‘luni’
# ● Afișeaza zile_sapt
# REZOLVARE:
# zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}
# zile_sapt.add('luni') # nu se adauga in lista deoarece set-urile nu accepta duplicate,dar nu ne da nici eroare
# print(zile_sapt)


# 13.Folosește un if și verifică dacă:
# ● Weekend este un subset al zilelor din săptămânii.
# ● Weekend nu este un subset al zilelor din săptămânii.
# REZOLVARE:
# zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}
# if weekend.issubset(zile_sapt) :
#     print('este subset')
# else:
#     print('nu este subset')
#
# if not weekend.issubset(zile_sapt):
#     print('nu este subset')
# else:
#     print('este subset')


# 14. Afișează diferențele dintre aceste 2 seturi.
# REZOLVARE:
# zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}
# print(zile_sapt.difference(weekend))


# 15. Afișază intersecția elementelor din aceste 2 seturi.
# REZOLVARE:
# zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}
# print(zile_sapt.intersection(weekend))


# Exerciții OPTIONALE - grad de dificultate: Mediu spre greu(may need google) .
# 1. Ne imaginăm o echipă de fotbal pt teren sintetic.
# 3 Schimbări maxime admise:
#
# ● Declară o Listă cu 5 jucători
# ● Schimbari_efectuate = te joci tu cu valori diferite
# ● Schimbari_max = 3
# Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
# - Efectuează schimbarea
# - Șterge jucătorul scos din listă
# - Adaugă jucătorul intrat
# - Afișaza a intra x, a ieșit y, mai ai z schimbări
# Dacă jucătorul nu e în teren:
# - Afișază ‘ nu se poate efectua schimbarea deoarece jucătorul x nu e în
# teren’
# - Afișază ‘mai ai z schimbări’
# Testează codul cu diferite valori
#
# Google search hint
# “how to check if item îs în list python”

# REZOLVARE:
# echipa_fotbal = ['jucatorul 1', 'jucatorul 2', 'jucatorul 3', 'jucatorul 4', 'jucatorul 5']
# i = input('Introduceti jucatorul pe care doriti sa il schimbati:')
# schimbari_max = 3
# if i in echipa_fotbal and schimbari_max <= 3 :
#     schimbari_ramase = schimbari_max - 1
#     j = input('Introduceti jucatorul pe care doriti sa il introduceti pe teren:')
#     print(f'A intrat {j}, a ieșit {i}, mai ai {schimbari_ramase} schimbari ramase.')
#     indexul_input = int(echipa_fotbal.index(i))
#     echipa_fotbal[indexul_input] = j
# else:
#     print(f'Nu se poate efectua schimbarea deoarece jucătorul {i} nu e în teren')
#     print(f'Mai ai {schimbari_max} schimbari ramase.')
# print(echipa_fotbal)








