# najprostszy sposób definiowania obiektu
# pass jest to po prostu miejsce dla funkcjonalności, która będzie dodana później
# pass może być użyte w ciele (a body, które nic nie robi)
# def odejmij(a, b):
#     pass
# self reprezentuje instancję klasę. Dzięki użyciu self my możemy mieć dostęp do właściwości i metod klasy w Pythonie.
# Tworzenie obiektu realizujmey przez tzw. konstruktor - jest to specjalna metoda, która jest wykonywana, kiedy tworzymy nasz obiekt. W Pythonie taką funkcję pełni metoda __init__.
class Rakietka:
    def __init__(self, kolor):
        self.kolor_obiektu = kolor
        print(f"Utworzyliśmy obiekt o kolorze: {self.kolor_obiektu} - ID: {id(self)}")

#  tworzymy obiekt na podstawie klasy, podajeemy nazwę obiektu (rakietka_a) i wywołujemy konstruktor klasy (Rakietka())
# f-string
# val = 'Python course'
# print(f"Rezultat zwracany przez naszą zmienną to {val}")

# name = 'Daniel'
# age = 28
# print(f"Hello, my name is {name} nad I am {age} years old")
def testklasy():
    rakietka_a = Rakietka("czerwony")
    rakietka_b = Rakietka("niebieski")
    print("*****************************")
    print(f"Obiekt typu {type(rakietka_a)} zawiera od razu pewne właściwości i metody:")
    print(dir(rakietka_a))
    print("*****************************")
    print(f"Obiekt typu {type(rakietka_b)} zawiera od razu pewne właściwości i metody:")
    print(dir(rakietka_b))
    print("*****************************")
    print(f"Kolor dla rakietka_a: {rakietka_a.kolor_obiektu}")
    print(f"Kolor dla rakietka_b: {rakietka_b.kolor_obiektu}")
