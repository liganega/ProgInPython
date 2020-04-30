import turtle

wn = turtle.Screen()
wn.bgcolor("lightyellow")               # 배경화면 색깔 정하기
wn.title("Hello, Bob and Alice!")       # 그래픽 제목 정하기

# bob 생성
bob = turtle.Turtle()

# alice 생성
alice = turtle.Turtle()
alice.shape("turtle")
alice.color("red")

alice.penup()
alice.backward(100)
alice.pendown()

# bob 으로 사각형 그리기
for i in range(4):
    bob.forward(100)
    bob.left(90)

# alice로 삼각형 그리기
for i in range(3):
    alice.forward(100)
    alice.right(120)

wn.mainloop()
