# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 16:48:58 2020
@author: jw
"""
#step4.네이버 영화에서 영화 하나를 찾고(디지몬 어드벤처) 평점 코멘트만 불러서 digimon.txt로 저장하기
from bs4 import BeautifulSoup
import urllib.request
f=open('d:\\data\\digimon.txt','w',encoding='UTF8')
for j in range(1,62):
    list_url = "https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=192613&page="+str(j)
    url=urllib.request.Request(list_url) 
    result=urllib.request.urlopen(url).read().decode("cp949")
    soup=BeautifulSoup(result,"html.parser") 
    result2=soup.find_all('td',class_ ='title') 
    params=[]
    for i in result2:
        f.write(str(i.get_text(" ", strip=True)[39:-3])+'\n')  #댓글 부분에서 불필요한 부분은 잘라내기

f.close()
