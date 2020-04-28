#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import math
import matplotlib.pyplot as plt
import time
import datetime


# In[2]:


def heapify(arr, n, i): 
    largest = i
    l = 2 * i + 1 
    r = 2 * i + 2 
    
    if l < n and arr[i] < arr[l]: 
        largest = l 
    
    if r < n and arr[largest] < arr[r]: 
        largest = r 
    
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] #zamiana
        heapify(arr, n, largest) 
  

def heapSort(arr): 
    n = len(arr) 
  

    for i in range(n//2 - 1, -1, -1): 
        heapify(arr, n, i) 
   
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] #zamiana
        heapify(arr, i, 0) 


# In[3]:


#tests
time1 = [] #male testy czas
time2 = [] #duze testy czas
elem1 = [] #male testy liczba el tablicy
elem2 = [] #duze testy liczba el tablicy

for i in range(100): #10 testow
    temp1 = []
    temp2 = []
    
    num_of_elem1 = np.random.randint(10, 1000) #small/med range
    num_of_elem2 = np.random.randint(1000, 100000) #large range
    
    #dodanie il elementow
    elem1.append(num_of_elem1)
    elem2.append(num_of_elem2)
    
    for j in range(num_of_elem1):  #med loop
        temp1.append( round(np.random.uniform(-100, 100),3) )
    
    #print(f'Nieposortowana tablica {temp1}')
    start = datetime.datetime.now()
    heapSort(temp1) #odwolanie do glownego alg
    end = datetime.datetime.now()
    time1.append(float((f'{(end-start).seconds}.{(end-start).microseconds}')))
    
    #print(f'Posrtowana tablica {temp1} \nw czasie: {end-start}s')
    #print('*'*100)
    #print(temp1)
    
    for j in range(num_of_elem2):  #large lopop
        temp2.append( round(np.random.uniform(-100, 100),3) )
    
    start = datetime.datetime.now()
    heapSort(temp2) #odwolanie do glownego alg
    end = datetime.datetime.now()
    time2.append(float((f'{(end-start).seconds}.{(end-start).microseconds}')))
    
    temp1 = []
    temp2 = []


#posrtowane względem liczby elementow tablicy, dopasowanie do nich czasu
zipped_list1 = zip(elem1, time1)
zipped_list2 = zip(elem2, time2)
sorted_pairs1, sorted_pairs2 = sorted(zipped_list1), sorted(zipped_list2)
tuples1, tuples2 = zip(*sorted_pairs1), zip(*sorted_pairs2)
elem1, time1 = [list(tuple) for tuple in tuples1]
elem2, time2 = [list(tuple) for tuple in tuples2]


# In[4]:


plt.plot(elem1, time1)
plt.xlabel('Liczba elementów tablicy')
plt.ylabel('Czas wykonania sortowania [s]')
plt.title(f'Analiza wyników (małe/średnie ilości)')
plt.show


# In[5]:


plt.plot(elem2, time2)
plt.xlabel('Liczba elementów tablicy')
plt.ylabel('Czas wykonania sortowania [s]')
plt.title(f'Analiza wyników (duże ilości)')
plt.show

