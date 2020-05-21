import random
from math import sin, cos


# funkcje
def RandomNumbers(left, right, n):
    return [random.uniform(left, right) for x in range(n)]


#funkcja z zadania
def f(values): 
    return (((float(sin(values[0]))**2)+cos(float((values[1]))**2)-10)**2 + 5*(values[0]-values[1])**2)

#tutaj przechowuyjemy pozycje kazdej pszczoly
class Bee(object):
    def __init__(self, position):
        self.position = position


def BeeAlgorithm(Function, left, right, n):
    generationCount = 100   # liczba generacji
    populationCount = 100    # liczba pszczół

    # poczatkowa polulacja
    population = [Bee(RandomNumbers(left, right, n)) for i in range(populationCount)]
    
    for generation in range(generationCount):
        for bee in population:
            for i in range(20): #rozmiar losowy
                alfa = random.uniform(-1, 1)  # losowa alfa

                candidatePosition = bee.position[:]

                randomBee = Bee(bee.position)

                while randomBee.position == bee.position:
                    randomBee = random.choice(population)

                k = random.randint(0, 1)  # zmienna 'x' albo 'y' mozliwa

                candidatePosition[k] += alfa *(bee.position[k] - randomBee.position[k])

                best = max(min(candidatePosition[k], right), left)
                candidatePosition[k] = best

                if Function(candidatePosition) > Function(bee.position):
                    bee.position = candidatePosition[:]

        # sortowanie i wybór najlepszej pozycji
        population.sort(key=lambda x: Function(x.position))
        population.reverse()
        population = population[:(populationCount)]
        # nowe jedzenie
        population.extend([Bee(RandomNumbers(left, right, n)) for i in range(populationCount - len(population) + 1)])


    # rozwiazanie
    bestVector = population[0].position
    for x in range(len(bestVector)):
        bestVector[x] = round(bestVector[x], 2)

    print(f"### f(x,y) MAX ###\nx= {bestVector}\nf(x)= {round(Function(bestVector), 3)}") #wynik


BeeAlgorithm(f, -50, 50, 2)