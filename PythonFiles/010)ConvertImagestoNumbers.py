# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 09:43:45 2020
@author:jw
"""
#%%
#Q.lungimages라는 폴더에 있는 사진들을 불러옵니다.
import os
test_image='d:\\lungimages'

def image_load(path):
    file_list=os.listdir(path) #해당 디렉토리의 파일명을 추출한다.
    return file_list

print(image_load(test_image))

#%%
#Q.파일이름을 숫자만 출력되게 바꾸고 ascending하게 정렬하고 다시 png를 추가하시오
import os
import re #데이터 정제 전문 모듈

test_image='d:\\lungimages'

def image_load(path):
    file_list=os.listdir(path) #해당 디렉토리의 파일명을 추출한다.
    file_name=[]
    for i in file_list:
        a=re.sub('[^0-9]','',i) #i의 값 중에서 숫자가 아닌것들은 싱글 두개('')를 붙인 것인 null로 변환해라
        file_name.append(int(a)) #문자 -> 숫자
        file_name.sort() #ascending하게 정렬
        
    file_res=[]
    for j in file_name:
        file_res.append('d:\\lungimages\\'+str(j)+'.png')
    return file_res
        
print(image_load(test_image))
#%%
#Q.이미지를 숫자로 변환하시오
import os
import re #데이터 정제 전문 모듈
import cv2 #opencv 모듈 임포트

test_image='d:\\images'

def image_load(path):
    file_list=os.listdir(path) #해당 디렉토리의 파일명을 추출한다.
    file_name=[]
    for i in file_list:
        a=re.sub('[^0-9]','',i) #i의 값 중에서 숫자가 아닌것들은 싱글 두개('')를 붙인 것인 null로 변환해라
        file_name.append(int(a)) #문자 -> 숫자
        file_name.sort() #ascending하게 정렬
        
    file_res=[]
    for j in file_name:
        file_res.append('d:\\images\\'+str(j)+'.png')
    

    image=[]
    for h in file_res:
        img=cv2.imread(h) #이미지를 숫자로 변환하는 코드
        image.append(img)
    return image

print(image_load(test_image))

#%%
#Q.위에서 출력한 숫자들을 numpy를 이용해서 행렬로 변경하시오
import os
import re #데이터 정제 전문 모듈
import cv2 #opencv 모듈 임포트
import numpy as np #행렬 연산으로 바꿔주는 모듈

test_image='d:\\images'

def image_load(path):
    file_list=os.listdir(path) #해당 디렉토리의 파일명을 추출한다.
    file_name=[]
    for i in file_list:
        a=re.sub('[^0-9]','',i) #i의 값 중에서 숫자가 아닌것들은 싱글 두개('')를 붙인 것인 null로 변환해라
        file_name.append(int(a)) #문자 -> 숫자
        file_name.sort() #ascending하게 정렬
        
    file_res=[]
    for j in file_name:
        file_res.append('d:\\images\\'+str(j)+'.png')
    

    image=[]
    for h in file_res:
        img=cv2.imread(h) #이미지를 숫자로 변환하는 코드
        image.append(img)
    return np.array(image,dtype=object)

print(image_load(test_image))

#%%
#Q.Kaggle에서 개와 고양이 사진을 다운받아서 파일명을 출력하시오
import os
path="d:\\images"

def image_load2(path):
    file_list=os.listdir(path)
    file_name=[]
    for i in file_list:
        a=re.sub('[^0-9]','',i)
        file_name.append(a)
        file_name.sort()
        
    file_res=[]
    for j in file_name:
        file_res.append('d:\\images\\'+str(j)+'.png')
    return file_res

print(image_load2(path))

#%%
#Q.위의 개사진 이미지들을 opencv와 numpy를 이용해서 숫자로 변환하고 numpy array로 반환되게 하시오
import os
path="d:\\images"

def image_load2(path):
    file_list=os.listdir(path)
    file_name=[]
    for i in file_list:
        a=re.sub('[^0-9]','',i)
        file_name.append(a)
        file_name.sort()
        
    file_res=[]
    for j in file_name:
        file_res.append('d:\\images\\'+str(j)+'.png')

    image=[]
    for h in file_res:
        img=cv2.imread(h)
        image.append(img)
    return np.array(image, dtype=object)

print(image_load2(path))

#%%
#Q.두 행렬을 만들고 덧셈 연산을 하시오
import numpy as np

a=[[1,2,3],[0,1,2],[3,0,1]]
b=[[2,0,1],[0,1,2],[1,0,2]]
a2=np.array(a)
b2=np.array(b)
print(a2+b2)

#%%
#Q.두 행렬을 만들고 두 행렬의 원소들의 곱셈 연산을 하시오
import numpy as np

a=[[1,2,3],[0,1,2],[3,0,1]]
b=[[2,0,1],[0,1,2],[1,0,2]]
a2=np.array(a)
b2=np.array(b)
print(a2*b2)

#%%
#Q.위에서 원소들의 곱으로 출력된 3x3 행렬의 요소들을 모두 다 더하시오
import numpy as np

a=[[1,2,3],[0,1,2],[3,0,1]]
b=[[2,0,1],[0,1,2],[1,0,2]]
a2=np.array(a)
b2=np.array(b)
result=a2*b2
print(np.sum(result)) #행렬 안의 원소들의 합 출력

#%%
#Q.4x4 행렬을 만들어서 좌상위 3x3 행렬만 출력하시오
import numpy as np
a=[[1,2,3,0],[0,1,2,3],[3,0,1,2],[2,3,0,1]]
a2=np.array(a)
print(a2[0:3,0:3]) #행을 0이상에서 3미만까지. 열을 0이상에서 3미만까지

#%%
#Q.4x4 행렬을 만들어서 우상위 3x3 행렬만 출력하시오
import numpy as np
a=[[1,2,3,0],[0,1,2,3],[3,0,1,2],[2,3,0,1]]
a2=np.array(a)
print(a2[0:3,1:4])

#%%
#Q.4x4 행렬을 만들어서 우하위 3x3 행렬만 출력하시오
import numpy as np
a=[[1,2,3,0],[0,1,2,3],[3,0,1,2],[2,3,0,1]]
a2=np.array(a)
print(a2[1:4,0:3])

#%%
#Q.4x4 행렬을 만들어서 좌하위 3x3 행렬만 출력하시오
import numpy as np
a=[[1,2,3,0],[0,1,2,3],[3,0,1,2],[2,3,0,1]]
a2=np.array(a)
print(a2[1:4,1:4])

#%%
#Q.위의 4x4 행렬에서 지정된 4개의 영역의 숫자들을 for loop 문을 이용해서 모두 출력되게 하시오
import numpy as np
a=[[1,2,3,0],[0,1,2,3],[3,0,1,2],[2,3,0,1]]
a2=np.array(a)

for i in range(2):
    for j in range(2):
        print(a2[i:i+3,j:j+3])

#%%
#Q.위에서 선택한 4개의 행렬(3x3)과 아래의 filter행렬(3x3) 과의 원소의 곱을 출력하시오
import numpy as np
a=[[1,2,3,0],[0,1,2,3],[3,0,1,2],[2,3,0,1]]
a2=np.array(a)

f=[[2,3,4],[1,2,3],[2,0,1]]
filter=np.array(f)

for i in range(2):
    for j in range(2):
        print((a2[i:i+3,j:j+3])*filter)

#%%
#Q.위에서 출력된 3x3 행렬 4개에 대한 원소들의 합이 각각 출력되게 하시오
import numpy as np
a=[[1,2,3,0],[0,1,2,3],[3,0,1,2],[2,3,0,1]]
a2=np.array(a)

f=[[2,3,4],[1,2,3],[2,0,1]]
filter=np.array(f)

for i in range(2):
    for j in range(2):
        print(np.sum(a2[i:i+3,j:j+3]*filter))

#%%
#Q.위에서 구한 원소들의 합으로만 구성된 행렬을 출력하시오
import numpy as np
a=[[1,2,3,0],[0,1,2,3],[3,0,1,2],[2,3,0,1]]
a2=np.array(a)

f=[[2,3,4],[1,2,3],[2,0,1]]
filter=np.array(f)

result=[]
for i in range(2):
    for j in range(2):
        result.append(np.sum(a2[i:i+3,j:j+3]*filter))
        
result2=np.array(result).reshape(2,2) #numpy array의 2x2 행렬로 변경
print(result2)

#%%
#Q.5x5 행렬들의 리스트와 4x4행렬을 곱하시오 
import numpy as np
a=[[2,3,1,4,7],[3,1,6,4,3],[2,1,5,3,1],[6,2,4,1,2],[7,3,1,2,3]]
a2=np.array(a)

f=[[3,1,4,1],[2,3,3,4],[5,1,2,1],[6,1,3,4]]
filter=np.array(f)

result=[]
for i in range(2):
    for j in range(2):
        result.append(np.sum(a2[i:i+4,j:j+4]*filter))
        
result2=np.array(result).reshape(2,2) #numpy array의 2x2 행렬로 변경
print(result2)

#%%
#Q.아래의 리스트에서 숫자 3이 있는지 순차 탐색으로 구현하시오. 있으면 '숫자 3이 있습니다'라는 메세지를 출력하시오
a=[15,11,1,3,8]

for i in a:
    if 3==i:
        print('숫자 3이 있습니다.')
        break
else:
    print('숫자 3이 없습니다.')

#%%
#Q.이번에는 숫자를 물어보게 하고 해당 숫자가 존재하는지 출력되게하시오
num=input('검색할 숫자를 입력하세요')
a=[15,11,1,3,8]

for i in a:
    if i==num:
        print('숫자 {}이(가) 있습니다.'.format(num))
        break
else:
    print('숫자 {}이(가) 있습니다.'.format(num))
