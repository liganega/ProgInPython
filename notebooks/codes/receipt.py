# 주문내역을 영수증 파일에 저장하는 함수
def saveReceipt(items, selections, price):
    with open("./codes/receipt.txt", "w") as receipt:
        for item in selections:                             # 선택된 항목 나열
            receipt.write(f'{item:>10}\t{items[item]:5}\t{selections[item]:2}\n')
            
        receipt.write("==========\n")
        receipt.write(f'     Total\t{price}\n')             # 가격 합계 표시

# 멤버십 할인 함수
def discount(price):
    return price * 0.9          # 10% 할인
