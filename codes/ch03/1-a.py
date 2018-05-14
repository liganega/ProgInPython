# 첫번째 도구 사용방법

import urllib.request
import time

# 반복적으로 가격 정보 확인하기

def get_price():
    page = urllib.request.urlopen("http://beans-r-us.appspot.com/prices-loyalty.html")
    text = page.read().decode("utf8")

    where = text.find('>$')
    price = float(text[where+2 : where+6])
    # 여기서 price 는 지역변수
    
answer = input("지금 살까요? ")

# 전역변수
price = 0

if answer == 'yes':
    get_price()
    print(price)
    print("지금사세요")
    
else:
    price = 5.0

    while price > 4.1:
        time.sleep(1)
        get_price()
        
    print(price)    
    print("지금 사세요")
