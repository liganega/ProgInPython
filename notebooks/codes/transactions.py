# 주문내역 저장하는 함수
def save_transaction(card_number, price, item):
    file = open("codes/transactions.txt", "a")
    file.write("%16s%07d%10s\n" % (card_number, price * 100, item))
    file.close()

# 멤버십 할인 함수
def discount(price):
    return price * 0.9          # 10% 할인
