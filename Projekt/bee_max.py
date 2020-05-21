#Zmaksymalizuje funkcję f(x, y)=(Sin[x^2]+Cos[y^2]-10)^2+5(x-y)^2 w zbiorze [-50, 50]^2 przy pomocy Algorytmu Pszczelego

import random
from math import sin, cos

# funkcje
def random_(left, right, n):
    return [random.uniform(left, right) for x in range(n)]

#funkcja z zadania
def f(values): 
    return ((float(sin(values[0])**2)+cos(float(values[1])**2)-10)**2 + 5*(values[0]-values[1])**2)

#tutaj przechowuyjemy pozycje kazdej pszczoly
class Bee(object):
    def __init__(self, x):
        self.x = x

def BeeAlgorithm(f, left, right, n):
    count_of_generation = 100   # liczba generacji
    count_of_population = 50   # liczba pszczół

    # poczatkowa polulacja
    population = [Bee(random_(left, right, n)) for i in range(count_of_population)]
    
    for generation in range(count_of_generation): #pszczoly pracujace
        for bee in population:
            for i in range(20): #wielokrotne szukanie przed zakonczeniem, w naszym przypadku 20 razy
                alfa = random.uniform(-1, 1)  # losowa alfa z zakresu [-1,1]

                scoutPos = bee.x[:] #pozycja zwiadowcy

                randomBee = Bee(bee.x) #ranodmowa pszczola

                while randomBee.x == bee.x:
                    randomBee = random.choice(population) #ustawianie losowej pszczoly dla kazdej poszczoly w populacji

                k = random.randint(0, 1)  # zmienna 'x' albo 'y' mozliwa

                scoutPos[k] += alfa *(bee.x[k] - randomBee.x[k]) #algorytm glowna czesc

                best = max(min(scoutPos[k], right), left) #wyszukiwanie najlepszego
                scoutPos[k] = best

                if f(scoutPos) > f(bee.x): #jezeli zwiadowca ma wieksza wartosc
                    bee.x = scoutPos[:]

        # sortowanie i wybór najlepszej pozycji
        population.sort(key=lambda x: f(x.x))
        population = population[:(count_of_population//2)]
        # nowe jedzenie
        population.extend([Bee(random_(left, right, n)) for i in range(count_of_population - len(population) + 1)])


    # rozwiazaniem jest najlepszy z populacji czyli ten na indexie = 0
    bestValues = population[0].x
    for x in range(len(bestValues)):
        bestValues[x] = round(bestValues[x], 2)

    print(f"### f(x,y) MAX ###\nx= {bestValues}\nf(x)= {round(f(bestValues), 3)}") #wynik
    print(f"### f(x,y) MAX ###\nx= {[-20, 30]}\nf(x)= {round(f([-20, 30]), 3)}") #wynik z wolfram alpha


BeeAlgorithm(f, -50, 50, 2) #wlaczenie algorytmu