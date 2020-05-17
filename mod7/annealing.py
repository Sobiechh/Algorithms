#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random, math

#funkcje 
def RandomNumbers(leftend, rightend, n):
    return [random.uniform(leftend, rightend) for i in range(n)]

def Sum_Squares(numberList):
    sum = 0
    for i in range(len(numberList)): sum += (i+1) * numberList[i] ** 2
    return sum

def Weierstrass(numberList):
    sum = 0
    for i in range(len(numberList)): sum += (abs(numberList[i] + 0.5)) ** 2
    return sum


def Annealing(Function, leftEnd, rightEnd, dimension, searchingMinimum = True):
    coolingCoefficient = 0.9      # współczynnik chłodzenia
    absoluteTemperature = 1000    # temperatura startowa
    iterations = 1000             # iteracje

    # Poczatkowy wektor  5 liczb z przedziału [left; right]
    bestVector = RandomNumbers(leftEnd, rightEnd, dimension)
    bestFitness = Function(bestVector)
    currentTemperature = absoluteTemperature

    for i in range(iterations):
        # Powtarzamy do uzyskania dobrego wyniku
        for j in range(50): 
            # Losujemy nowy wektor
            newVector = bestVector[:]
            k = random.randint(0, dimension - 1)
            newVector[k] += 0.001 * random.uniform(leftEnd, rightEnd)
            newVector[k] = max(min(newVector[k], rightEnd), leftEnd)
            newFitness = Function(newVector)

            # Jeśli prawdopodobieństwo jest mniejsz nie zmieniamy nic
            if searchingMinimum == True:
                if newFitness > bestFitness:
                    delta = newFitness - bestFitness
                    probability = math.exp( -delta / currentTemperature)
                    if random.random() > probability: 
                        continue
            else:
                 if newFitness < bestFitness:
                    delta = newFitness - bestFitness
                    probability = math.exp( delta / currentTemperature)
                    if random.random() > probability: 
                        continue

            bestVector = newVector
            bestFitness = Function(bestVector)

        currentTemperature *= coolingCoefficient 

    for x in range (len(bestVector)): bestVector[x] = round(bestVector[x], 5)
    extremum = "Max" if searchingMinimum == False else "Min"
    print("         ### ", str(Function.__name__).upper() + "'S", extremum, " ###\n   x  =", bestVector,         "\n f(x) =", round(bestFitness, 5), "\n")

Annealing(Sum_Squares, -10, 10, 5, True)
Annealing(Weierstrass, -10, 10, 5, True)
Annealing(Sum_Squares, -10, 10, 5, False)
Annealing(Weierstrass, -10, 10, 5, False)

