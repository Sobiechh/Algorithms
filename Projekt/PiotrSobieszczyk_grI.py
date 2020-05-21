import random
from math import sin, cos

#funkcje
def RandomNumbers(leftend, rightend, n):
    return [random.uniform(leftend, rightend) for number in range(n)]

def f(numberList):
    sum = 0
    for i in range(len(numberList)): 
        sum += (sin(numberList[0]**2)+cos(numberList[1]*2)-10)**2 + 5*(numberList[0]-numberList[1])**2
    return sum

class Bee(object):
    def __init__(self, position):
        self.position = position

def BeeAlgorithm(Function, leftEnd, rightEnd, dimension, searchingMinimum = True):
    generationCount = 100    # liczba generacji
    populationCount = 50    # liczba pszczół
    population = [Bee(RandomNumbers(leftEnd, rightEnd, dimension)) for i in range(populationCount)] #poczatek
    
    t = 0

    while t <= generationCount:
        for bee in population:
            for i in range(15):
                alfa = random.uniform(-1,1)
                candidatePosition = bee.position[:]
                randomBee = Bee(bee.position)
                while randomBee.position == bee.position: 
                    randomBee = random.choice(population)
                k = random.randint(0, dimension - 1)
                candidatePosition[k] += alfa * (bee.position[k] - randomBee.position[k])
                candidatePosition[k] = max(min(candidatePosition[k], rightEnd), leftEnd)
                
                if searchingMinimum == False and Function(candidatePosition) > Function(bee.position):
                    bee.position = candidatePosition[:]
                elif searchingMinimum == True and Function(candidatePosition) < Function(bee.position): 
                    bee.position = candidatePosition[:]

        #sortowanie i wybór najlepszej pozycji
        population.sort(key=lambda x: Function(x.position))
        if searchingMinimum == False: population.reverse()
        population = population[:(populationCount // 3)]

        #nowe jedzenie
        population.extend([Bee(RandomNumbers(leftEnd, rightEnd, dimension)) \
                         for i in range(populationCount - len(population) + 1)])

        t += 1

    #rozwiazanie
    bestVector = population[0].position
    for x in range (len(bestVector)): bestVector[x] = round(bestVector[x], 5)
    extremum = "Max" if searchingMinimum == False else "Min"
    print("###", str(Function.__name__).upper() + "'S", extremum, "###\n   x  =", bestVector, "\n f(x) =", round(Function(bestVector),5), "\n")


BeeAlgorithm(f, -50, 50, 2, False)