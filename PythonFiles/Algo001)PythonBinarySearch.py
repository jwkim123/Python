# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 16:27:39 2020
@author: jw
"""
#%%
#Q.아래의 a리스트에서 중앙값을 찾으시오
import numpy as np

a=[1,7,11,12,14,23,33,47,51,64,67,77,139,672,871]
a_n=np.array(a)
print(np.median(a_n))

#%%
#Q.a리스트에서 첫번쨰 숫자부터 중앙값에 해당하는 숫자까지만 검색하시오
import numpy as np

a=[1,7,11,12,14,23,33,47,51,64,67,77,139,672,871]
a_n=np.array(a)
med=np.median(a_n)

print(a[:a.index(med)+1])

#%%
#Q.위의 리스트에서 선택된 숫자들을 중앙값까지 포함해서 다 지우시오
import numpy as np

a=[1,7,11,12,14,23,33,47,51,64,67,77,139,672,871]
a_n=np.array(a)
med=np.median(a_n)

del(a[:a.index(med)+1])

#%%
#Q.위의 결과로 출력된 아래의 리스트에서 중앙값을 출력하시오
import numpy as np

a=[1,7,11,12,14,23,33,47,51,64,67,77,139,672,871]
a_n=np.array(a)
med=np.median(a_n)

del(a[:a.index(med)+1])
a_m2=np.median(a)
print(a_m2)

#%%
#Q.위에서 출력된 중앙값 77이 내가 검색하고자 하는 67보다 크면 아래의 결과 리스트만 출력되게 하시오
import numpy as np 

a=[1,7,11,12,14,23,33,47,51,64,67,77,139,672,871]
num=int(input('검색할 숫자를 입력하세요')) 

if num in a:
    for i in range(10): 
        med=np.median(a)
        if med>num: 
            del(a[a.index(med):]) 
             
        elif med<num: 
            del(a[:a.index(med)+1]) 
         
        elif med==num: 
            break 
    print('{}은 이진탐색 {}번만에 검색되었습니다'.format(num,i+1)) 
         
elif num not in a: 
    print('{}은 a리스트에 없습니다'.format(num))
