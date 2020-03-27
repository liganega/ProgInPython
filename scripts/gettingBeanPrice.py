import urllib.request
import time

price_basis = 6.0     # 기준가
bean_price = 5.0      # while 문이 작동하도록 임의로 지정된 현재 원두 가격

price_url = "http://beans.itcarlow.ie/prices.html"

while bean_price < price_basis:     # 기준가보다 커질 때까지 가격 확인

    # 30초 기다리기
    time.sleep(30)

    price_page = urllib.request.urlopen(price_url)
    page_text = price_page.read().decode("utf8")

    price_location = page_text.find('>$') + 2

    # float로 변환해서 원두 가격 업데이트
    bean_price = float(page_text[price_location : price_location + 4])

    # 확인된 가격 보여주기
    print("현재 가격:", bean_price)

# 기준가보다 높을 때 가격 인상 권유    
print("커피 원두 현재 가격이", bean_price, "입니다. 아메리카노 가격을 인상하세요!")