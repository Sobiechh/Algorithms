#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

#funkcje
def RandomNumbers(leftend, rightend, n):
    return [random.uniform(leftend, rightend) for number in range(n)]

def GenerateMutatedVector(mutationControlParam, population, i, leftEnd, rightEnd):
    tmp = population[:i]                     # 3 losowe wektory
    tmp.extend(population[(i+1):])           # nowy wektor
    mutationPool = random.sample(tmp, 3)
    mutatedVector = []
    for j in range (len(mutationPool[0])):
        number = mutationPool[0][j] + mutationControlParam * (mutationPool[1][j] - mutationPool[2][j])
        number = max(min(number, rightEnd), leftEnd)
        mutatedVector.append(number)
    return mutatedVector

def Sum_Squares(numberList):
    sum = 0
    for i in range(len(numberList)): sum += (i+1) * numberList[i] ** 2
    return sum

def Weierstrass(numberList):
    sum = 0
    for i in range(len(numberList)): sum += (abs(numberList[i] + 0.5)) ** 2
    return sum

def DifferentialEvolution(Function, leftEnd, rightEnd, dimension, searchingMinimum = True):
    #dane poczatkowe
    generationCount = 150   
    populationCount = 100          
    mutationControlParam = 0.4     
    crossoverProbability = 0.8     

    population = [RandomNumbers(leftEnd, rightEnd, dimension) for i in range(populationCount)] # populacja początkowa
    t = 0
    while t <= generationCount:
        # Mutacja:
        mutatedVectors = []
        for i in range (populationCount):
            mutatedVectors.append(GenerateMutatedVector(mutationControlParam, population, i, leftEnd, rightEnd))
        
        # Krzyżowanie:
        crossoveredVectors = []
        for i in range (populationCount):
            crossVec = []
            for j in range(dimension):
                r = random.random()
                di = random.randint(0, dimension - 1)
                if r > crossoverProbability and j != di: 
                    crossVec.append(population[i][j])
                else:
                    crossVec.append(mutatedVectors[i][j])
            crossoveredVectors.append(crossVec)
        
        # Optymalizacja:
        for i in range (populationCount):
            if searchingMinimum == True:
                if Function(crossoveredVectors[i]) < Function(population[i]):
                    population[i] = crossoveredVectors[i]
            else:
                if Function(crossoveredVectors[i]) > Function(population[i]):
                    population[i] = crossoveredVectors[i]
        t += 1

    # Rozwiazanie
    population.sort(key=lambda x: Function(x))
    if searchingMinimum == False: population.reverse()
    bestVector = population[0]
    for x in range (len(bestVector)): bestVector[x] = round(bestVector[x], 5)
    extremum = "Max" if searchingMinimum == False else "Min "
    print("         ~~~~ ", str(Function.__name__).upper() + "'S", extremum, " ~~~\n   x  =", bestVector,         "\n f(x) =", round(Function(bestVector), 5), "\n")

DifferentialEvolution(Sum_Squares, -10, 10, 5, True)
DifferentialEvolution(Weierstrass, -10, 10, 5, True)
DifferentialEvolution(Sum_Squares, -10, 10, 5, False)
DifferentialEvolution(Weierstrass, -10, 10, 5, False)

