import turtle
wn = turtle.Screen()
wn.bgcolor("lightyellow")
bob = turtle.Turtle()
bob.shape("turtle")        # 화살표 대신 거북이 모양 선택
bob.color("blue")

bob.penup()                # 펜 들기 (이동할 때 선을 그리지 않게 됨)
size = 20
for i in range(30):
   bob.stamp()             # 거북이 모양 도장 찍기
   size = size + 3         # 회전을 점차 크게 돌도록 만들기
   bob.forward(size)       # size 크기만큼 전진하기
   bob.right(24)           # 24도 우회전하기

wn.mainloop()
