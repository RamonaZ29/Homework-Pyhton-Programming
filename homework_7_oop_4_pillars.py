# 2. Rezolvă exercițiul după ce ai urcat proiectul (tot ce am facut până acum
# împreună).

# ABSTRACTION
# Clasa abstractă FormaGeometrica
# Conține un field PI=3.14
# Conține o metodă abstractă aria (opțional)
# Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai
# probabil am colturi’

# INHERITANCE
# Clasa Pătrat - moștenește FormaGeometrica
# constructor pentru latură

# ENCAPSULATION
# latura este proprietate privată
# Implementează getter, setter, deleter pentru latură
# Implementează metoda cerută de interfață (opțional, doar dacă ai ales să implementezi metoda abstractă aria)
# Clasa Cerc - moștenește FormaGeometrica
# constructor pentru rază
# raza este proprietate privată
# Implementează getter, setter, deleter pentru rază
# Implementează metoda cerută de interfață - în calcul folosește field PI mostenit din clasa părinte (opțional,
# doar dacă ai ales să implementezi metoda abstractă aria)
# POLYMORPHISM
# Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
# Creează un obiect de tip Patrat și joacă-te cu metodele lui
# Creează un obiect de tip Cerc și joacă-te cu metodele lui

from abc import ABC, abstractmethod
class Forma_geometrica(ABC): # aceasta este clasa abstracta
    PI = 3.14
    @abstractmethod
    def calculeaza_aria(self):
        pass
    def descriere_forma(self):
        print ('Cel mai probabil am colturi.')

class Patrat(Forma_geometrica): #clasa copil care mosteneste clasa abstracta
    def __init__(self, latura):
        self.__latura = latura # "__latura" este proprietate privata

    def get__latura(self):  # getter
        return self.__latura
    def set__latura(self): # setter
        self.__latura = latura
    def delete__latura(self): #deleter
        del self.__latura
        print('Latura a fost stearsa.')
    def calculeaza_aria(self):
        return self.__latura **2

class Cerc(Forma_geometrica): #o alta clasa copil care mosteneste clasa abstracta
    def __init__(self, raza_cerc):
        self.__raza_cerc = raza_cerc  # "__raza_cerc" este proprietate privata
    def get__raza_cerc(self):  # getter
        return self.__raza_cerc
    def set__raza_cerc(self): # setter
        self.__raza_cerc = raza_cerc
    def delete__raza_cerc(self): #deleter
        del self.__raza_cerc
        print('Raza a fost stearsa.')
    def calculeaza_aria(self):
        return self.__raza_cerc ** 2 * self.PI
    def descriere_forma(self):
        print('Eu nu am colturi!')

masuta_patrata = Patrat(10)
masuta_patrata.descriere_forma()
masuta_patrata.calculeaza_aria()
print (f'Aria masutei este {masuta_patrata.calculeaza_aria()}')
masuta_patrata.get__latura()
print (f'Latura masutei este {masuta_patrata.get__latura()}')
masuta_patrata.delete__latura()

hula_hop = Cerc(25)
hula_hop.descriere_forma()
hula_hop.calculeaza_aria()
print (f'Aria cercului hula hop este {hula_hop.calculeaza_aria()}')
hula_hop.get__raza_cerc()
print (f'Raza cercului hula hop {hula_hop.get__raza_cerc()}')
hula_hop.delete__raza_cerc()
