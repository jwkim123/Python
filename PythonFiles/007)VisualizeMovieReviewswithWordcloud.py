# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 10:07:29 2020
@author: jw
"""
#%%
#Q.조선일보에서 봉사로 검색했을 때 나오는 기사들 중 가장 많이 나오는 단어는?
stev=open("d:\\data\\bongsa.txt",encoding="UTF8")
stev2=stev.read().split() #어절별로 분리해서 stev2라는 리스트에 담는다.
stev2.sort() #stev2 리스트 안의 요소들을 정렬
#print(stev2)

from collections import Counter
count_list=Counter(stev2) #stev2 리스트안의 어절별로 각각 몇건씩 있는지 정리를 합니다.
#print(count_list)
result=count_list.most_common(30) #top 30개만 추출
print(result) #10개

#%%
#Q.조선일보에서 봉사로 검색해서 나오는 기사 30개에서 가장 많이 나오는 단어가 무엇인지 출력하시오
stev=open("d:\\data\\bongsa.txt",encoding="UTF8")
stev2=stev.read().split() #어절별로 분리해서 stev2라는 리스트에 담는다.
stev2.sort() #stev2 리스트 안의 요소들을 정렬
#print(stev2)

from collections import Counter
count_list=Counter(stev2) #stev2 리스트안의 어절별로 각각 몇건씩 있는지 정리를 합니다.
result=count_list.most_common(30) #top 30개만 추출
for i in result:
    print(i[0],i[1]) #10개

#%%
#Q.영화 평가 게시글들 스크롤링했던 txt에서 가장 많이 나오는 어절이 무엇인지 확인하시오
stev=open("d:\\data\\titanic.txt",encoding="UTF8")
stev2=stev.read().split() #어절별로 분리해서 stev2라는 리스트에 담는다.
stev2.sort() #stev2 리스트 안의 요소들을 정렬
#print(stev2)

from collections import Counter
count_list=Counter(stev2) #stev2 리스트안의 어절별로 각각 몇건씩 있는지 정리를 합니다.
result=count_list.most_common(30) #top 30개만 추출
print(result)

#%%
#Q.영화 라라랜드의 리뷰를 txt로 만드시오
stev=open("d:\\data\\lalaland.txt",encoding="UTF8")
stev2=stev.read().split() #어절별로 분리해서 stev2라는 리스트에 담는다.
stev2.sort() #stev2 리스트 안의 요소들을 정렬
#print(stev2)

from collections import Counter
count_list=Counter(stev2) #stev2 리스트안의 어절별로 각각 몇건씩 있는지 정리를 합니다.
result=count_list.most_common(30) #top 30개만 추출
print(result)

#%%
#Q.라라랜드 영화 리뷰 txt에서 긍정단어가 몇개인지 확인하시오
#라라랜드 영화 리뷰를 단어 단위로 끊어서 읽어오기
stev=open("d:\\data\\lalaland.txt",encoding='UTF8')
stev2=stev.read().split()
	
#긍정단어 리스트 불러오기
positive=open("d:\\data\\positive-words2.txt")
pos=positive.read().split('\n')
	
#라라랜드 리뷰에 긍정 단어가 몇개인지 확인하기
cnt=0
for i in stev2:
    if i.lower() in pos:
        cnt+=1
        print(i)
print(cnt)


#%%
#Q.
#라라랜드 영화 리뷰를 단어 단위로 끊어서 읽어오기
stev=open("d:\\data\\lalaland.txt",encoding='UTF8')
stev2=stev.read().split()
	
#긍정단어 리스트 불러오기
negative=open("d:\\data\\negative-words2.txt")
neg=negative.read().split('\n')
	
#라라랜드 리뷰에 긍정 단어가 몇개인지 확인하기
cnt=0
for i in stev2:
    if i.lower() in neg:
        cnt+=1
        print(i)
print(cnt)


#%%
#Q.라라랜드 영화 리뷰를 워드클라우드로 그리기
# 텍스트마이닝 데이터 정제
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt  # 그래프 그리는 모듈
from os import path     #  os 에 있는 파일을 파이썬에서 인식하기 위해서
import re   #  데이터 정제를 위해서 필요한 모듈 
import numpy as np  
from PIL import Image  # 이미지 시각화를 위한 모듈 

# 워드 클라우드의 배경이 되는 이미지 모양을 결정
usa_mask = np.array(Image.open("d://project//usa_im.png"))

# 워드 클라우드를 그릴 스크립트 이름을 물어봅니다. 
script = 'digimon.txt'

# 워드 클라우드 그림이 저장될 작업 디렉토리를 설정 
d = path.dirname("d://project//")

# 기사 스크립트와 os 의 위치를 연결하여 utf8로 인코딩해서 한글 텍스트를
# text 변수로 리턴한다.
text = open(path.join(d, "%s"%script), mode="r", encoding="utf-8").read()


# 파이썬이 인식할 수 있는 한글 단어의 갯수를 늘리기 위한 작업 
file = open('d://project//word.txt', 'r', encoding = 'utf-8') #word.txt는 리뷰에 나올만한 단어들
word = file.read().split(' ') #word.txt를 어절별로 분리하고
for i in word: #분리한 어절들을 하나씩 불러온다.
    text = re.sub(i,'',text) #re.sub('있다','','있다') <-라라랜드 리뷰의 '있다'를 ''으로 대체하겠다 라는 뜻 
    print(text)
    #*일반적인 문장에서 자주나오는 단어들을 일일히 손으로 다 할 수는 없으니까 for문으로 전부 ''으로 대체

# 워드 클라우드를 그린다. 
wordcloud = WordCloud(font_path='d://Windows//Fonts//gulim', # 글씨체
                      stopwords=STOPWORDS,   # 마침표, 느낌표,싱글 쿼테이션 등을 정제
                      max_words=1000, # 워드 클라우드에 그릴 최대 단어갯수
                      background_color='white', # 배경색깔
                      max_font_size = 100, # 최대 글씨 크기 
                      min_font_size = 1, # 최소 글씨 
                      mask = usa_mask, # 배경 모양 
                      colormap='jet').generate(text).to_file('d://project//digimon_cloud.png')
                  # c 드라이브 밑에 project 폴더 밑에 생성되는 워드 클라우드 이미지 이름
  
plt.figure(figsize=(15,15)) #가로x세로 15x15
plt.imshow(wordcloud, interpolation='bilinear')  # 글씨가 퍼지는 스타일 
plt.axis("off")

#%%
#Q.라라랜드 리뷰 txt에서 평가 점수가 6점 이상인 리뷰들만 출력하시오
stev=open("d:\\data\\lalaland.txt",encoding="UTF8")
stev2=stev.readlines()#어절별로 분리해서 stev2라는 리스트에 담는다.

for i in stev2:
    if int(i[6:8])>=6: #리뷰에서 평점들만 출력하고 평점을 str->int로 바꿔준다
        print(i,end="")
        
#%%
#Q.평점이 6점 이상이면 pos, 미만이면 neg라는 비어있는 리스트에 추가하시오
stev=open("d:\\data\\lalaland.txt",encoding="UTF8")
stev2=stev.readlines()#어절별로 분리해서 stev2라는 리스트에 담는다.
pos=[]
neg=[]
for i in stev2:
    if int(i[6:8])>=6: #리뷰에서 평점들만 출력하고 평점을 str->int로 바꿔준다
        pos.append(i[8:]) #엔터 빼려면 .strip("\n")하면 됨
    else:
        neg.append(i[8:])
        
print(pos)
print(neg)

#%%
#Q.위의 pos의 데이터들을 pos_lala.txt, neg는 neg_lala.txt로 저장하시오
stev=open("d:\\data\\lalaland.txt",encoding="UTF8")
stev2=stev.readlines()#어절별로 분리해서 stev2라는 리스트에 담는다.

pos=[]
neg=[]

for i in stev2:
    if int(i[6:8])>=6: #리뷰에서 평점들만 출력하고 평점을 str->int로 바꿔준다
        pos.append(i[8:]) #엔터 빼려면 .strip("\n")하면 됨
    else:
        neg.append(i[8:])
        
f=open("d:\\project\\pos_lala.txt","w",encoding="UTF8")
f.writelines(pos)
f.close()

f2=open("d:\\project\\neg_lala.txt","w",encoding="UTF8")
f2.writelines(neg)
f2.close()

#%%
#Q.pos_lala.txt를 워드클라우드로 시각화하기
# 텍스트마이닝 데이터 정제
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt  # 그래프 그리는 모듈
from os import path     #  os 에 있는 파일을 파이썬에서 인식하기 위해서
import re   #  데이터 정제를 위해서 필요한 모듈 
import numpy as np  
from PIL import Image  # 이미지 시각화를 위한 모듈 

# 워드 클라우드의 배경이 되는 이미지 모양을 결정
usa_mask = np.array(Image.open("d://project//usa_im.png"))

# 워드 클라우드를 그릴 스크립트 이름을 물어봅니다. 
script = 'pos_lala.txt'

# 워드 클라우드 그림이 저장될 작업 디렉토리를 설정 
d = path.dirname("d://project//")

# 기사 스크립트와 os 의 위치를 연결하여 utf8로 인코딩해서 한글 텍스트를
# text 변수로 리턴한다.
text = open(path.join(d, "%s"%script), mode="r", encoding="utf-8").read()


# 파이썬이 인식할 수 있는 한글 단어의 갯수를 늘리기 위한 작업 
file = open('d://project//word.txt', 'r', encoding = 'utf-8') #word.txt는 리뷰에 나올만한 단어들
word = file.read().split(' ') #word.txt를 어절별로 분리하고
for i in word: #분리한 어절들을 하나씩 불러온다.
    text = re.sub(i,'',text) #re.sub('있다','','있다') <-라라랜드 리뷰의 '있다'를 ''으로 대체하겠다 라는 뜻 
    print(text)
    #*일반적인 문장에서 자주나오는 단어들을 일일히 손으로 다 할 수는 없으니까 for문으로 전부 ''으로 대체

# 워드 클라우드를 그린다. 
wordcloud = WordCloud(font_path='d://Windows//Fonts//gulim', # 글씨체
                      stopwords=STOPWORDS,   # 마침표, 느낌표,싱글 쿼테이션 등을 정제
                      max_words=1000, # 워드 클라우드에 그릴 최대 단어갯수
                      background_color='white', # 배경색깔
                      max_font_size = 100, # 최대 글씨 크기 
                      min_font_size = 1, # 최소 글씨 
                      mask = usa_mask, # 배경 모양 
                      colormap='jet').generate(text).to_file('d://project//pos_lala_cloud.png')
                  # c 드라이브 밑에 project 폴더 밑에 생성되는 워드 클라우드 이미지 이름
  
plt.figure(figsize=(15,15)) #가로x세로 15x15
plt.imshow(wordcloud, interpolation='bilinear')  # 글씨가 퍼지는 스타일 
plt.axis("off")

#%%
#Q.neg_lala.txt를 워드 클라우드로 시각화하기
# 텍스트마이닝 데이터 정제
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt  # 그래프 그리는 모듈
from os import path     #  os 에 있는 파일을 파이썬에서 인식하기 위해서
import re   #  데이터 정제를 위해서 필요한 모듈 
import numpy as np  
from PIL import Image  # 이미지 시각화를 위한 모듈 

# 워드 클라우드의 배경이 되는 이미지 모양을 결정
usa_mask = np.array(Image.open("d://project//usa_im.png"))

# 워드 클라우드를 그릴 스크립트 이름을 물어봅니다. 
script = 'neg_lala.txt'

# 워드 클라우드 그림이 저장될 작업 디렉토리를 설정 
d = path.dirname("d://project//")

# 기사 스크립트와 os 의 위치를 연결하여 utf8로 인코딩해서 한글 텍스트를
# text 변수로 리턴한다.
text = open(path.join(d, "%s"%script), mode="r", encoding="utf-8").read()


# 파이썬이 인식할 수 있는 한글 단어의 갯수를 늘리기 위한 작업 
file = open('d://project//word.txt', 'r', encoding = 'utf-8') #word.txt는 리뷰에 나올만한 단어들
word = file.read().split(' ') #word.txt를 어절별로 분리하고
for i in word: #분리한 어절들을 하나씩 불러온다.
    text = re.sub(i,'',text) #re.sub('있다','','있다') <-라라랜드 리뷰의 '있다'를 ''으로 대체하겠다 라는 뜻 
    print(text)
    #*일반적인 문장에서 자주나오는 단어들을 일일히 손으로 다 할 수는 없으니까 for문으로 전부 ''으로 대체

# 워드 클라우드를 그린다. 
wordcloud = WordCloud(font_path='d://Windows//Fonts//gulim', # 글씨체
                      stopwords=STOPWORDS,   # 마침표, 느낌표,싱글 쿼테이션 등을 정제
                      max_words=1000, # 워드 클라우드에 그릴 최대 단어갯수
                      background_color='white', # 배경색깔
                      max_font_size = 100, # 최대 글씨 크기 
                      min_font_size = 1, # 최소 글씨 
                      mask = usa_mask, # 배경 모양 
                      colormap='jet').generate(text).to_file('d://project//neg_lala_cloud.png')
                  # c 드라이브 밑에 project 폴더 밑에 생성되는 워드 클라우드 이미지 이름
  
plt.figure(figsize=(15,15)) #가로x세로 15x15
plt.imshow(wordcloud, interpolation='bilinear')  # 글씨가 퍼지는 스타일 
plt.axis("off")
