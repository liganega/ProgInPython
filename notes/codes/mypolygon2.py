import turtle

wn = turtle.Screen()

# bob 생성
bob = turtle.Turtle()

# alice 생성
alice = turtle.Turtle()
alice.shape("turtle")       # 펜 모양을 거북이로 변경
alice.color("red")          # 선 색깔을 빨강으로 변경

alice.penup()               # 펜 들기: 선 그리지 않음
alice.backward(120)         # 뒤로 120픽셀 이동
alice.pendown()             # 펜 내리기: 선 그리기 시작함

# bob 으로 사각형 그리기
for i in range(4):
    bob.forward(100)
    bob.left(90)

# alice로 삼각형 그리기
for i in range(3):
    alice.forward(100)
    alice.right(120)        # 시계방향으로 회전

wn.mainloop()
