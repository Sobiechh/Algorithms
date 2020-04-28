#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import math
import matplotlib.pyplot as plt
import time
import datetime


# In[2]:


def shellSort(seq):
    inc = len(seq) // 2
    while inc:
        for i, el in enumerate(seq[inc:], inc):
            while i >= inc and seq[i - inc] > el:
                seq[i] = seq[i - inc]
                i -= inc
            seq[i] = el
        inc = 1 if inc == 2 else inc * 5 // 11


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
    shellSort(temp1) #odwolanie do glownego alg
    end = datetime.datetime.now()
    time1.append(float((f'{(end-start).seconds}.{(end-start).microseconds}')))
    
    #print(f'Posrtowana tablica {temp1} \nw czasie: {end-start}s')
    #print('*'*100)
    #print(temp1)
    
    for j in range(num_of_elem2):  #large lopop
        temp2.append( round(np.random.uniform(-100, 100),3) )
    
    start = datetime.datetime.now()
    shellSort(temp2) #odwolanie do glownego alg
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


# In[ ]:


plt.plot(elem2, time2)
plt.xlabel('Liczba elementów tablicy')
plt.ylabel('Czas wykonania sortowania [s]')
plt.title(f'Analiza wyników (duże ilości)')
plt.show

