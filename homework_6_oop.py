# OBS! Pentru toate clasele, creați cel puțin 2 obiecte cu valori diferite și apelați toate metodele clasei.
# Exerciții obligatorii - grad de dificultate: Usor spre Mediu
# 1.Clasa Cerc
# Atribute: raza, culoare
# Constructor pentru ambele atribute
# Metode:
# ● descrie_cerc() - va PRINTA culoarea și raza
# ● aria() - va RETURNA aria
# ● diametru()
# ● circumferinta()
# REZOLVARE:
# from math import pi
# class Cerc:
#     def __init__(self,raza,culoare):
#         self.raza = raza
#         self.culoare = culoare
#
#     def descrie_cerc(self):
#         print(f'Cercul are culoarea {self.culoare} si raza {self.raza} cm.')
#
#     def aria_cerc(self):
#         aria = pi*self.raza**2
#         print(f'Aria cercului este {aria}.')
#         return aria
#
#     def diametru_cerc(self):
#         diametru = self.raza*2
#         print(f'Diametrul cercului este {diametru}.')
#         return diametru
#
#     def circumferinta_cerc(self):
#         circumferinta = 2*pi*self.raza**2
#         print(f'Circumferinta cercului este {circumferinta}.')
#         return circumferinta #trebuie sa adaug RETURN la metode?
#
# cerc_mic = Cerc(4,'roz') # obiect 1 instantiat
# print(cerc_mic.raza)
# print(cerc_mic.culoare)
# cerc_mic.descrie_cerc()
# cerc_mic.aria_cerc()
# cerc_mic.diametru_cerc()
# cerc_mic.circumferinta_cerc()

# cerc_mare = Cerc(10.5,'negru') # obiect 2 instantiat
# cerc_mare.descrie_cerc()
# cerc_mare.aria_cerc()
# cerc_mare.diametru_cerc()
# cerc_mare.circumferinta_cerc()

# 2. Clasa Dreptunghi
# Atribute: lungime, latime, culoare
# Constructor pentru toate atributele
# Metode:
# ● descrie()
# ● aria()
# ● perimetrul()
# ● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
# Ea va lua ca și parametru o nouă culoare și va suprascrie atributul self.culoare.
# Puteti verifica schimbarea culorii prin apelarea metodei descrie().
# REZOLVARE:
# class Dreptunghi:
#     def __init__(self,lungime,latime,culoare):
#         self.lungime = lungime
#         self.latime = latime
#         self.culoare = culoare
#
#     def descrie_dreptunghi(self):
#         print(f'Dreptunghiul are culoarea {self.culoare} iar lungimea {self.lungime} m si latimea {self.latime}m')
#
#     def aria_dreptunghiului(self):
#         aria = self.lungime * self.latime
#         print(f'Aria dreptunghiului este {aria}m patrati.')
#         return aria
#
#     def perimetru_dreptunghi(self):
#         perimetru = (self.lungime + self.latime)*2
#         print(f'Perimetrul dreptunghiului este {perimetru}m.')
#         return perimetru

#     def schimba_culoare_dreptunghi(self,noua_culoare):
#         self.culoare = noua_culoare

# masa = Dreptunghi(3,2,'maro') # obiect 1 instantiat
# masa.descrie_dreptunghi()
# masa.aria_dreptunghiului()
# masa.perimetru_dreptunghi()
# masa.schimba_culoare_dreptunghi('alb')
# masa.descrie_dreptunghi()

# perete = Dreptunghi(25.5,11,'verde') # obiect 2 instantiat
# perete.descrie_dreptunghi()
# perete.aria_dreptunghiului()
# perete.perimetru_dreptunghi()
# perete.schimba_culoare_dreptunghi('gri')
# perete.descrie_dreptunghi()

# 3. Clasa Angajat
# Atribute: nume, prenume, salariu
# Constructor pt toate atributele
# Metode:
# ● descrie()
# ● nume_complet()
# ● salariu_lunar()
# ● salariu_anual()
# ● marire_salariu(procent)
# REZOLVARE:
# class Angajat:
#     def __init__(self,nume,prenume,salariu):
#         self.nume = nume
#         self.prenume = prenume
#         self.salariu = salariu
#
#     def descrie_angajat(self):
#         print(f'Salariatul se numeste {self.nume} {self.prenume} si are salariul net {self.salariu} lei.')
#
#     def nume_complet(self,al_doilea_prenume): # CUM PUN OPTIONAL AL 2-LEA PRENUME?
#         print(f'Numele complet al salariatului este: {self.nume} {self.prenume} {al_doilea_prenume}.')
#
#     def salariu_lunar(self,bonus):
#         self.salariu += bonus
#         print(f'Salariul lunar impreuna cu alte bonusuri este {self.salariu}.')
#         return self.salariu
#
#     def salariu_anual(self):
#         print (f'Salariul net anual din CIM este {self.salariu * 12}.')
#         return self.salariu
#
#     def marire_salariu_procentual(self,procent_marire):
#         self.salariu += self.salariu * procent_marire/100
#         print(f'Salariul dupa marire este: {self.salariu}.')
#         return self.salariu
#
# angajat_1  = Angajat('Simionescu','Ionela',4500)
# angajat_1.descrie_angajat()
# angajat_1.nume_complet('Georgiana')
# angajat_1.salariu_lunar(400)
# angajat_1.salariu_anual()
# angajat_1.marire_salariu_procentual(20)
#
# angajat_2 = Angajat('Pop','Gigel',8000)
# angajat_2.descrie_angajat()
# angajat_2.nume_complet('Marcel')
# angajat_2.salariu_lunar(0)
# angajat_2.salariu_anual()
# angajat_2.marire_salariu_procentual(10)

# 4.Clasa Cont
# Atribute: iban, titular_cont, sold
# Constructor pentru toate atributele
# Metode:
# ● afisare_sold() - Titularul x are în contul y suma de n lei
# ● debitare_cont(suma)
# ● creditare_cont(suma)
# REZOLVARE:
# class Cont:
#     def __init__(self,iban,titular_cont,sold):
#         self.iban = iban
#         self.titular_cont = titular_cont
#         self.sold = sold
#
#     def afisare_sold(self):
#         print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei. ')
#
#     def debitare_cont(self,suma_debitata):
#         if suma_debitata <= self.sold:
#             self.sold -= suma_debitata
#             print(f'Soldul dupa debitar este : {self.sold} lei.')
#         else:
#             print('Fonduri insuficiente!')
#         return self.sold
#
#     def creditare_cont(self,suma_creditata):
#         self.sold += suma_creditata
#         print(f'Noul sold dupa creditare este : {self.sold} lei.')
#         return self.sold
#
# titular_1 = Cont('RO0001234567','Cuc Sabina',1400)
# titular_1.afisare_sold()
# titular_1.debitare_cont(650)
# titular_1.creditare_cont(300)
# titular_1.afisare_sold()
#
# titular_2 = Cont('RO0008905664','Georgiu Alexandru',500)
# titular_2.afisare_sold()
# titular_2.debitare_cont(550)
# titular_2.creditare_cont(50)
# titular_2.debitare_cont(550)
# titular_2.afisare_sold()

# Exercitii optionale - grad de dificultate: MEDIU spre greu: may need Google
# 1. Clasa Factura
# Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor
# avea aceeași serie), număr, nume_produs, cantitate, pret_buc
# Constructor: toate atributele, fara serie
# Metode:
# ● schimbă_cantitatea(cantitate)
# ● schimbă_prețul(pret)
# ● schimbă_nume_produs(nume)
# ● generează_factura() - va printa tabelar dacă reușiți
# Factura seria x numar y
# Data: generați automat data de azi
# Produs | cantitate | preț bucată | Total
# Telefon | 7 | 700 | 49000
# REZOLVARE:
# from datetime import date
# from tabulate import tabulate
# class Factura:
#     seria = 'RBZ'
#     data = date.today()
#
#     def __init__(self,numar,nume_produs,cantitate,pret_buc):
#         self.numar = numar
#         self.nume_produs = nume_produs
#         self.cantitate = cantitate
#         self.pret_buc = pret_buc
#
#     def schimba_cantitatea(self,cantitate):
#         self.cantitate = cantitate
#
#     def schimba_pretul(self,pret):
#         self.pret_buc = pret
#
#     def schimba_nume_produs(self,denumire):
#         self.nume_produs = denumire
#
#     def genereaza_factura(self):
#         table = [['Serie','Numar','Data','Nume produs','Cantitate','Pret','Total'],
#             [self.seria,self.numar,self.data,self.nume_produs,self.cantitate,self.pret_buc,self.pret_buc*self.cantitate]]
#         print(tabulate(table, headers='firstrow'))
#
# pelerine = Factura('001','Pelerina',3,100)
# pelerine.genereaza_factura()
#
# carti = Factura('002','Carte',10,68)
# carti.genereaza_factura()


# 2.Clasa Masina
# Atribute: marca, model, viteza maxima, viteza_actuala, culoare,
# culori_disponibile (set), inmatriculata (bool)
# Culoare = gri - toate mașinile cand ies din fabrica sunt gri
# Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrica
# Culori disponibile = alegeți voi 5-7 culori
# Marca = alegeți voi - fabrica produce o singură marca dar mai multe modele
# Inmatriculata = False
# Constructor: model, viteza_maxima
# Metode:
# ● descrie() - se vor printa toate atributele, în afară de culori_disponibile
# ● înmatriculare() - va schimba atributul înmatriculată în True
# ● vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua
# culoare e în opțiunea de culori disponibile, altfel afișați o eroare
# ● accelerează(viteza) - se va accelera la o anumită viteza, dacă viteza e
# negativă-eroare, daca viteza e mai mare decat viteza_max - masina va
# accelera până la viteza maximă
# ● franeaza() - mașina se va opri și va avea viteza 0
# REZOLVARE:
# class Car:
#     marca = 'Audi'
#     model = None
#     viteza_maxima = None
#     viteza_actuala = 0
#     culoare = 'gri'
#     culori_disponibile = {'bleu', 'alb', 'negru', 'rosu', 'roz'}
#     inmatriculata = False
#
#     def __init__(self,model,viteza_maxima):
#         self.model = model
#         self.viteza_maxima = viteza_maxima
#
#     def descrie_masina(self):
#         print(f'Automobilul marca {self.marca} {self.model} este disponibila in culoarea {self.culoare}.')
#         print(f'Viteza maxima a automobilului este {self.viteza_maxima}km/h,'
#               f'iar viteza actuala este {self.viteza_actuala}km/h.')
#         print(f'Inmatriculare {self.inmatriculata}.')
#
#     def inmatriculare(self):
#         if self.inmatriculata == True:
#             print('Masina este deja inmatriculata!')
#         else:
#             self.inmatriculata = True
#             print(f'Masina este inmatriculata cu succes!')
#
#     def vopseste_masina(self,culoare):
#         if culoare in self.culori_disponibile:
#             print(f'Masina e disponibila pe culoarea : {culoare}.')
#         else:
#             self.culori_disponibile.add(self.culoare)
#             print(f'Culoarea {culoare} este indisponibila. '
#                   f'Culorile disponibile pentru acest model sunt: {self.culori_disponibile}. ')
#
#     def accelereaza_masina(self,viteza_accelerare):
#         if viteza_accelerare < 0:
#             print('Eroare!Introduceti o valoare pozitiva!')
#         elif (viteza_accelerare + self.viteza_actuala) > self.viteza_maxima:
#             self.viteza_actuala = self.viteza_maxima
#             print(f'Ati depasit viteza maxima! Puteti accelera pana la {self.viteza_maxima}km/h.'
#                   f'Viteza actuala este {self.viteza_maxima}km/h.')
#         else:
#             self.viteza_actuala += viteza_accelerare
#             print(f'Ati accelerat cu {viteza_accelerare}km/h. Viteza actuala este {self.viteza_actuala} km/h.')
#
#     def franeaza_masina(self):
#         self.viteza_actuala = 0
#         print(f'Ati franat iar masina este oprita. Viteza actuala este {self.viteza_actuala}km/h.')
#
# audi_a4 = Car('A4',190)
# audi_a4.descrie_masina()
# audi_a4.inmatriculare()
# audi_a4.vopseste_masina('alb')
# audi_a4.accelereaza_masina(120)
# audi_a4.accelereaza_masina(80)
# audi_a4.franeaza_masina()
#
# audi_q5 = Car('Q5',223)
# audi_q5.descrie_masina()
# audi_q5.inmatriculare()
# audi_q5.vopseste_masina('violet')
# audi_q5.accelereaza_masina(-30)
# audi_q5.accelereaza_masina(100)
# audi_q5.franeaza_masina()



