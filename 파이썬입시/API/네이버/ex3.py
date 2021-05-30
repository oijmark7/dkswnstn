



import os
import sys
import urllib.request
import json

client_id = "2NhHqjjdzUXHBrl_BL33"
client_secret = "ZRy9I7CWeC"

url = "https://openapi.naver.com/v1/datalab/shopping/categories";

body = {
    "startDate" : "2019-05-30" ,
    "endDate"   : "2021-05-30" ,
    "timeUnit"  :"date",
    "category" : [{"name":"면세점","param":["50000010"]} ] ,
    "device" : " ",
    "gender" : "",
    "ages" : [ ]
}
body = json.dumps(body,ensure_ascii=False)


request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
request.add_header("Content-Type","")

