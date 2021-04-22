# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 19:42:27 2020
@author: jw
"""
def cacheProcess(cities,cacheSize):
    city=[i.upper() for i in cities]
    
    #check cache size
    if cacheSize>30:
        print('CacheSize must be less than 30')
    
    #check City character length
    city_length=[print('City must be less than 20 characters') for i in cities if len(i)>20]
    
    #cache memory
    cache=[None for i in range(cacheSize)]
    
    #check whether the city is in cache memory, count processing time
    cnt=0
    for i in range(len(city)):
        if city[i] in cache:
            cnt+=1 #count time
        else:
            cnt+=5
            cache.append(city[i]) #if the city is not in cache memory, append it
            del cache[0] #and delete first element in cache
    return cnt   

check = []
a = cacheProcess(["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"],3)
check.append(a)
a = cacheProcess(["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"],3)
check.append(a)
a = cacheProcess(["Jeju","Pangyo","Seoul","NewYork","LA","SanFrancisco","Seoul","Rome","Paris","Jeju","NewYork","Rome"],2)
check.append(a)
a = cacheProcess(["Jeju","Pangyo","Seoul","NewYork","LA","SanFrancisco","Seoul","Rome","Paris","Jeju","NewYork","Rome"],5)
check.append(a)
a = cacheProcess(["Jeju","Pangyo",'NewYork','newyork'],2)
check.append(a)
a = cacheProcess(["Jeju","Pangyo","Seoul","NewYork","LA"],0)
check.append(a)
a = cacheProcess(['Jeju', 'Jeju','Jeju'],3)
check.append(a)

print(check)
correct = [50,21,60,52,16,25,7] #the result should be this

for i in range(len(check)) :
    if check[i] != correct[i] :
        print("%i번째 경우가 틀립니다."%i)
