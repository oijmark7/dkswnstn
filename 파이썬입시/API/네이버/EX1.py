
# API : 미리 만들어진 코드 [프로그램]
    # 네이버 APIen

# 발급 받은 애플리케이션 정보를 변수에 저장

# 직접 입력해서 검색하기
검색어 = input("블로그 검색 :")
import os
import sys
import urllib.request
import json
import re

# 발급 받은 애플리케이션 정보를 변수에 저장
client_id = "2NhHqjjdzUXHBrl_BL33"
client_secret = "ZRy9I7CWeC"
encText = urllib.parse.quote("검색어")
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)

# 책 검색
검색어 = input("책 검색 :")
encText = urllib.parse.quote(검색어)
url = "https://openapi.naver.com/v1/search/book.json?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    검색결과 = response_body.decode('utf-8')
    # 검색결과 가공 하기
    json결과 = json.loads(검색결과)
    for i in json결과['items'] :
        타이틀 = re.sub('<.+?>','',i['title'],0,re.I | re.S)
        print( 타이틀 )
else:
    print("Error Code:"+rescode)
