
# 네이버 함수
import urllib.parse
import re
import json

# 네이버 함수 만들기
def 네이버검색(카테고리,검색결과수) :
    client_id = "2NhHqjjdzUXHBrl_BL33"
    client_secret = "ZRy9I7CWeC"
    #검색결과를 json 으로 가져오기
    url = "https://openapi.naver.com/v1/search/"+카테고리+"json"
    option ="&display="+검색결과수 + "&sort=count" # display : 출력 갯수 : 검색결과 수
    query = "?query="+urllib.parse.quote(   input(카테고리+"의 검색 정보 입력 :"))
    url_query= url + query + option

    request = urllib.request.Request(url_query)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)

    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
    else:
        print("Error Code:" + rescode)

    검색 = response_body.decode('utf-8')    #'utf-8' : 한글 지원
    print("Error code:" + rescode)

while True : # 무한반복하기 : 0번을 입력하면 종료 된다
    print("검색[naverAPI]프로그램")
    print("카테고리[1.뉴스 2. 쇼핑 3.도서 4. 영화 5.백과사전]0.종료")
    선택 = int( input("선택 : ") ) # 입력받아 선택변수에 저장
    #선택 제어
    if 선택 == 1 :
        카테고리 = "news"
        검색결과수 = input("-->뉴스 선택 했습니다. 몇게 출력할까요?")
        네이버검색(카테고리,검색결과수 ) # 함수 불러내기
    if 선택 == 2:
        카테고리 = "shop"
        검색결과수 = input("-->쇼핑 선택 했습니다. 몇게 출력할까요?")
        네이버검색(카테고리, 검색결과수)  # 함수 불러내기
    if 선택 == 3:
        카테고리 = "book"
        검색결과수 = input("-->도서 선택 했습니다. 몇게 출력할까요?")
        네이버검색(카테고리, 검색결과수)  # 함수 불러내기
    if 선택 == 4:
        카테고리 = "movie"
        검색결과수 = input("-->도서 선택 했습니다. 몇게 출력할까요?")
        네이버검색(카테고리, 검색결과수)  # 함수 불러내기
    if 선택 == 5:
        카테고리1 = "encyc"
        검색결과수 = input("-->도서 선택 했습니다. 몇게 출력할까요?")
        네이버검색(카테고리, 검색결과수)  # 함수 불러내기
    if 선택 == 0:
        print("--> 이용해주셔서 감사합니다")
    break









