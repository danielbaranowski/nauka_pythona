# najprostszy sposób definiowania obiektu
# pass jest to po prostu miejsce dla funkcjonalności, która będzie dodana później
# pass może być użyte w ciele (a body, które nic nie robi)
# def odejmij(a, b):
#     pass

class Rakietka:
    pass

# tworzymy obiekt na podstawie klasy, podajemy nazwę obiektu (rakietka_a) i wywołujemy konstruktor klasy (Rakietka())

def testklasy():
    rakietka_a = Rakietka()
    print(f"Obiekt typu {type(rakietka_a)} zawiera od razu pewne właściwości i metody:")
    print(dir(rakietka_a))
