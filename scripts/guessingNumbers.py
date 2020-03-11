from random import randint

print("숫자맞추기 게임에 환영합니다.")

secret = randint(0,20)
guess = -1

while guess != secret:
    guess = int(input("0부터 20 사이의 숫자 하나를 입력하세요: "))
    if guess == secret:
        print("맞았습니다!")
    else:
        if guess > secret:
            print("너무 커요!")
        else:
            print("너무 작아요!")

print("게임 종료!")