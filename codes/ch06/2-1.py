'''
컴피숍2의 POS(Point-of-Sale) 계산대에 사용되는 프로그램 구현하기

- 카드 정보를 알고 있을 때 카드 정보와 물품 가격 및 정보를 파일에 저장하는 프로그램을 구현하고자 함
- 사용할 정보: 카드 번호 16자리, 물품 가격 7자리, 물품 내용 6자리
'''

# 모듈 불러오기: transactions와 special
# 커피숍과 커피숍1의 두 POS에서 공유하는 모듈 두 개임.
from transactions import *
import special

# 커피숍1의 상품 리스트
items = ["Donut1", "Latte1", "Filter1", "Muffin1", "Espresso1", "Bagle1"]

# 각 상품들의 가격 (단위: 달러)
prices = [1.40, 2.6, 1.90, 1.10, 1.20, 1.5]

# 매장에서 파는 물품 목록 알려주기
print("점원: 주문 하실래요?")
print("손님: 뭐가 있나요?")
print("점원: 아래 항목들을 보시고 원하시는 번호를 기억하세요.")

print("============")
option = 1
for item in items:
    print(str(option)+". "+item)
    option += 1

print(str(option)+". "+ "이상입니다.")
print("============")

# 손님이 주문하기
running = True                          # 아래 while 문이 실행되는 조건
while running:
    choice = int(input("점원: 몇 번 선택하실래요? "))

    if choice >= option:                # 주의: 현재 option = len(items) + 1
        running = False                 # 물품 개수보다 큰 번호를 선택하면 주문 종료
    else:                               # 특정 물품을 선택한 경우
        item = items[choice -1]
        price = prices[choice-1]

        '''
        # 중복할인 없음
        if input("특별한 날 확인: ") == "Y":
            price = special.discount(price)
        elif input("점원: 멤버십 카드 있으세요? ") == "Y":
            price = discount(price)
        '''

        # 중복할인 적용
        if input("특별한 날 확인: ") == "Y":
            price = special.discount(price)
        if input("점원: 멤버십 카드 있으세요? ") == "Y":
            price = discount(price)

        card_number = input("점원: 신용카드 번호 알려주세요! ")

        # 주문내역 파일에 저장하기
        save_transaction(card_number, price, item)
