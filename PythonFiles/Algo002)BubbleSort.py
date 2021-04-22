# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 09:36:06 2020
@author: jw
"""
버블정렬
#%%
#Q.리스트를 만들고 첫번쨰 요소와 두번쨰 요소의 순서를 변경하시오
a=[10,5,20,9,8]
temp=a[1] #1번쨰 요소를 temp 변수에 임시저장하고
a[1]=a[0] #1번째 요소를 0번째 요소로 변경한 후에
a[0]=temp #0번쨰 요소를 1번쨰 요소로 변경합니다.
print(a)

#%%
#Q.아래의 a 리스트를 만들고 첫번째 요소와 두번째 요소의 크기를 비교한 후 첫번째 요소의 크기가 
#더 크다면 두번째 요소와 자리를 바꾸시오
a=[10,5,20,9,8]
temp=[]
if a[0]>a[1]:
    temp=a[1] #1번쨰 요소를 temp 변수에 임시저장하고
    a[1]=a[0] #1번째 요소를 0번째 요소로 변경한 후에
    a[0]=temp
else:
    pass
print(a)
#%%
#Q.버블정렬하시오
a=[5,4,3,2,1,8,7,10]

def bubble_sort(a):
    cnt=0
    for k in range(1,len(a)):
        for i in range(0,len(a)-1):
            if a[i]>a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]
                cnt+=1       
    return a

print(bubble_sort(a))
