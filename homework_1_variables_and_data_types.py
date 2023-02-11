# Grad MEDIU :Ex 1- Ce este o variabila:
# O variabila este o bucata de memorie, putem sa ne-o imaginam ca pe o cutie de valori pe care punem o eticheta,
# atribuindu-i o valoare.

# Ex 2: declarare si initializare tipuri de date:
# 1. String
nume = 'Zoicas'
prenume = 'Ramona'
# 2. Integer
varsta_candidat = 32
# 3. Float
nota_obtinuta = 8.40
# 4. Boolean
admis = True

# Ex 3: utilizam functia type pentru a afla daca au tipul de date scontat
print(type(nume))
print(type(varsta_candidat))
print(type(nota_obtinuta))
print(type(admis))

#Ex 4: Rotunjeste Float-ul cu functia ROUND, si suprascrie variabila - verifica apoi tipul de date
print(round(nota_obtinuta))
nota_obtinuta = int(nota_obtinuta)
print(type(nota_obtinuta))

# Ex 5: Folosește print() și printează în consola 4 propoziții folosind cele 4 variabile.
# Rezolvă nepotrivirile de tip prin ce modalitate dorești.
print(f'Ma numesc' + nume + prenume + '.')
print(f'Am varsta de' + str(varsta_candidat) + '.')
print(f'La examenul de admitere am obtinut nota' + str(nota_obtinuta) + '.' )
print(f'Candidatul este' + str(admis) + '.')
# Rezolva nepotrivirile
print(f'Ma numesc {nume} {prenume}')
print(f'Am varsta de {varsta_candidat} ani.')
print(f'La examenul de admitere am obtinut nota {nota_obtinuta}.' )
print(f'Candidatul este admis ? {admis} .')

# Ex 6: Citește de la tastatură:
# - numele;
# - prenumele.
# Afișează: 'Numele complet are x caractere'.

nume = input('Completeaza numele')
prenume = input('Completeaza prenumele')
print(f'Numele complet are {len(nume + prenume)} caractere.')

# Ex 7: Citește de la tastatură:
# - lungimea;
# - lățimea.
# Afișează: 'Aria dreptunghiului este x'.
lungime = int(input('Introdu lungimea dreptunghiului'))
latime = int(input('Introdu latimea dreptunghiului'))
print(f'Aria dreptunghiului este {lungime * latime} .')

# Ex 8: Având stringul: 'Coral is either the stupidest animal or the smartest rock':
# - afișează de câte ori apare cuvântul 'the'
sentence1 = 'Coral is either the stupidest animal or the smartest rock'
print (sentence1.count('the')) # am aplicat formula : My_str.functii ajutatoare

# Ex 9: Același string.
# ● Afișează de câte ori apare cuvântul 'the';
# ● Printează rezultatul.
#CRED CA AM REZOLVAT ANTERIOR( IN EX 8).

# Ex 10 :Același string.
# ● Folosiți un assert ca să verificați dacă acest string conține doar numere.
sentence1 = 'Coral is either the stupidest animal or the smartest'
assert sentence1.isdigit() == True, "Error: does not contain only numbers."

# EXERCITII DIFICULTATE MEDIU / GREU
#1 Exercițiu:
# - citește de la tastatură un string de dimensiune impară;
# - afișează caracterul din mijloc
# pentru nr impar (odd):
text = input('Introduceti un string impar:')
mijloc = text[len(text)//2]
print(mijloc)
# pentru string par:
text2 = input('Introduceti un string par:')
left_middle = text2[(len(text2) - 1) // 2]
right_middle = text2[len(text2) // 2]
print(left_middle, right_middle)

#2 Exercitiu:
# Folosind assert, verifică dacă un string este palindrom.
string_test= input('va rugam introduceti un cuvant:')
rev = (string_test[::-1])
print (string_test==rev)
assert string_test == rev, "error , not palindrom"

#3 Exercitiu: Folosind o singură linie de cod :
# - citește un string de la tastatură (ex: 'alabala portocala');
# - salvează fiecare cuvânt într-o variabilă;
# - printează ambele variabile pentru verificare.

string1 = input('Introduceti un string din mai multe cuvinte:')
cuvant1,cuvant2 = string1.split()
print (type(cuvant1),(type(cuvant2)))

#4 Exercitiu:
# - citește un string de la tastatură (ex: alabala portocala);
# - salvează primul caracter într-o variabilă - indiferent care este el, încearcă
# cu 2 stringuri diferite;
# - capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul
# caracter => alAbAlA portocAla.
string_ex4 = input('Introduceti un string din mai multe cuvinte:')
primul_caracter = string_ex4[0]
print (primul_caracter)
print (type(primul_caracter))
# Varianta rezolvare UPPER ,string_modificat = x[0]+x[1:len(x)-1].replace(x[0],x[0].upper()) +x[len(x)-1]

#5 Exercitiu:
# - citește un user de la tastatură;
# - citește o parolă;
# - afișează: 'Parola pt user x este ***** și are x caractere';
# - ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să
# afișeze corect.
# eg: parola abc => ***
# parola abcd => ****

user = input('Introduceti un user:')
parola = input('Introduceti o parola:')
print(f'Parola criptata este: ("x"*len{parola})')





