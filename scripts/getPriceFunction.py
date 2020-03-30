import urllib.request
import time

price_url_loyal = "http://beans.itcarlow.ie/prices-loyalty.html"
price_url_general = "http://beans.itcarlow.ie/prices.html"

# price_url 매개변수 활용
def getPrice(price_url):
    price_page = urllib.request.urlopen(price_url)
    page_text = price_page.read().decode("utf8")
    price_location = page_text.find('>$') + 2
    price = float(page_text[price_location : price_location + 4])

    return price

print("지금 가격을 비교합니다.")    

# getPrice 함수를 인자를 달리하여 두 번 실행
bean_price_loyal = getPrice(price_url_loyal)
bean_price_general = getPrice(price_url_general)
# abs 함수는 절댓값을 계산하는 함수. 가격의 차이를 나타내기 위해 사용
price_difference = abs(bean_price_general - bean_price_loyal)

print(f"충성고객용 가격이 일반고객용 가격보다 {price_difference:.2f} 달러 저렴합니다.")