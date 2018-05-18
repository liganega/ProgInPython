import turtle

wn = turtle.Screen()
wn.bgcolor("lightyellow")      # 배경화면 색깔 정하기
wn.title("Hello, Bob!")      # 그래픽 제목 정하기

bob = turtle.Turtle()
bob.color("blue")            # 화살표 색깔 정하기
bob.pensize(3)               # 선 두께 정하기

for i in range(3):
    bob.fd(100)
    bob.lt(120)

wn.mainloop()
