# 첫번째 도구 사용방법

import urllib.request
import time

# 반복적으로 가격 정보 확인하기

def get_price():
    page = urllib.request.urlopen("http://beans-r-us.appspot.com/prices-loyalty.html")
    text = page.read().decode("utf8")

    where = text.find('>$')
    return float(text[where+2 : where+6])

answer = input("지금 살까요? ")

if answer == 'yes':
    price = get_price()
    print(price, "지금사세요")
    
else:
    price = 5.0

    while price > 4.1:
        time.sleep(1)
        price = get_price()
        
    print(price, "지금 사세요")
