# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 09:37:24 2020
@author: jw
"""
#%%
#조선일보에서 '봉사' 검색 후 크롤링하기. 기사 페이지들
from bs4 import BeautifulSoup
import urllib.request
def bs_scroll():
    params=[]
    for h in range(1,4):
        list_url = 'https://futurechosun.com/page/'+str(h)+'?s=%EB%B4%89%EC%82%AC'
        url=urllib.request.Request(list_url) 
        result=urllib.request.urlopen(url).read().decode("utf-8")
        soup=BeautifulSoup(result,"html.parser") 
        result1=soup.find_all('div',class_ ='elementor-post__title')
        for i in result1:
            params.append(i.find_all('a')[0].get('href'))
    return len(params)   #36

print(bs_scroll())
#%%
#조선일보에서 '봉사' 검색 후 크롤링하기. 기사 본문
from bs4 import BeautifulSoup
import urllib.request
    
def bs_detail_scroll():
    list_url = "https://futurechosun.com/archives/52491"
    url=urllib.request.Request(list_url) 
    result=urllib.request.urlopen(url).read().decode("utf-8")
    soup=BeautifulSoup(result,"html.parser") 
    result1=soup.find_all('div',class_ ='elementor-element elementor-element-24e82692 elementor-widget__width-initial elementor-widget elementor-widget-theme-post-content')
    
    params2=[]
    for i in result1: 
        params2.append(i.get_text(" ",strip=True))
    return params2

print(bs_detail_scroll())

#%%
#조선일보에서 '봉사' 검색 후 3페이지 까지의 기사 본문 가져오기
from bs4 import BeautifulSoup 
import urllib.request 

def bs_scroll():     
    params1 = [] 
    for i in range(1,4): 
        list_url = 'https://futurechosun.com/page/'+str(i)+'?s=%EB%B4%89%EC%82%AC' 
        url = urllib.request.Request(list_url)  
        result = urllib.request.urlopen(url).read().decode("utf-8")  
        stuff = BeautifulSoup( result, "html.parser") 
        res1 = stuff.find_all('div',class_ ="elementor-post__title") 
        for i in res1: 
            params1.append(i.find_all('a')[0].get('href'))         
    return(params1) 

def bs_detail_scroll(): 
    list_url = bs_scroll() 
    for  i  in  list_url: 
        url = urllib.request.Request(i)  
        result = urllib.request.urlopen(url).read().decode("utf-8")  
        soup=BeautifulSoup(result,"html.parser") 
        result=soup.find_all('div', class_ ='elementor-element elementor-element-24e82692 elementor-widget__width-initial elementor-widget elementor-widget-theme-post-content') 
        for i in result: 
            print(i.find_all('p')) 

print( bs_detail_scroll()) 

#%%
#조선일보에서 '봉사' 검색 후 2페이지 까지의 기사 본문 가져오는데 기사들을 params2라는 리스트에 넣기
#params2 리스트의 내용들을 bongsa.txt로 저장하기
from bs4 import BeautifulSoup 
import urllib.request 

def bs_scroll():     
    params1 = [] 
    for i in range(1,2):       
        list_url = 'https://futurechosun.com/page/'+str(i)+'?s=%EB%B4%89%EC%82%AC' 
        url = urllib.request.Request(list_url)  
        result = urllib.request.urlopen(url).read().decode("utf-8")  
        stuff = BeautifulSoup( result, "html.parser")       
        res1 = stuff.find_all('div',class_ ="elementor-post__title")          
        for i in res1: 
            params1.append(i.find_all('a')[0].get('href'))          
    return(params1) 

def bs_detail_scroll(): 
    list_url = bs_scroll() 
    f = open('d:\\data\\bongsa.txt', 'w', encoding="UTF-8") 
    for  i  in  list_url: 
        url = urllib.request.Request(i)  
        result = urllib.request.urlopen(url).read().decode("utf-8")  
        soup=BeautifulSoup(result,"html.parser") 
        result=soup.find_all('div', class_ ='elementor-element elementor-element-24e82692 elementor-widget__width-initial elementor-widget elementor-widget-theme-post-content') 
        for i in result: 
            for j in i.find_all('p'): 
                f.write(str(j.get_text()) + "\n")   
    f.close() 

print( bs_detail_scroll()) 

#%%
#이데일리에서 '첫눈' 검색하고 크롤링하기. 기사 페이지들
from bs4 import BeautifulSoup
import urllib.request
def eda_scroll():
    params=[]
    for h in range(1,4):
        list_url = 'https://www.edaily.co.kr/search/news/?keyword=%ec%b2%ab%eb%88%88&page='+str(h)
        url=urllib.request.Request(list_url) 
        result=urllib.request.urlopen(url).read().decode("utf-8")
        soup=BeautifulSoup(result,"html.parser") 
        result1=soup.find_all('div',class_ ='newsbox_04')
        for i in result1:
            params.append('http://edaily.co.kr'+i.find_all('a')[0].get('href'))
    return params  #36

print(len(eda_scroll()))

#%%
#이데일리에서 '첫눈' 검색하고 크롤링하기. 기사 페이지들
from bs4 import BeautifulSoup
import urllib.request
   
def eda_detail_scroll():
    list_url = "https://www.edaily.co.kr/news/read?newsId=01423526625998520&mediaCodeNo=258"
    url=urllib.request.Request(list_url) 
    result=urllib.request.urlopen(url).read().decode("utf-8")
    soup=BeautifulSoup(result,"html.parser") 
    result1=soup.find_all('div',class_ ='news_body')
    params2=[]
    for i in result1: 
        params2.append(i.get_text(" ",strip=True)) 
    return params2

print(eda_detail_scroll())

#%%
#이데일리에서 '첫눈' 검색 후 2페이지 까지의 기사 본문 가져오는데 기사들을 params2라는 리스트에 넣기
#params2 리스트의 내용들을 firstsnow1.txt로 저장하기
from bs4 import BeautifulSoup
import urllib.request

def eda_scroll():
    params=[]
    for  i  in  range(1, 4):
        list_url = 'https://www.edaily.co.kr/search/news/?keyword=%ec%b2%ab%eb%88%88&page=' + str(i)
        url = urllib.request.Request(list_url) 
        result = urllib.request.urlopen(url).read().decode("utf-8") 
        soup = BeautifulSoup( result, "html.parser")
        result1=soup.find_all('div', class_ ='newsbox_04')
        for i in result1:
             params.append("http://edaily.co.kr/"+i.find_all('a')[0].get("href"))
    return params

def  eda_detail_scroll():
    list_url= eda_scroll()
    f=open("d:\\data\\firstsnow1.txt","w",encoding="UTF-8")
    for  i  in  list_url:
        url = urllib.request.Request(i) 
        result = urllib.request.urlopen(url).read().decode("utf-8") 
        soup=BeautifulSoup(result,"html.parser")
        result1 = soup.find_all('div', class_ ='news_body')
        for  i  in   result1:
            f.write(str( i.get_text() ))
    f.close()


eda_detail_scroll()  
