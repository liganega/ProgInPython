import turtle   # turtle 모듈

wn = turtle.Screen()        # Screen은 클래스의 인스턴스(객체) 생성
wn.bgcolor("lightyellow")   # 배경화면 지정

wn2 = turtle.Screen()       # Screen 클래스는 인스턴스를 하나만 허용
                            # 따라서 둘째 인스턴스는 만들어지지 않음
                            # 싱글톤 클래스 라고 함.

bob = turtle.Turtle()       # Turtle 클래스의 인스턴스(객체) 생성
bob.shape("turtle")         # 거북이 모양 사용
#bob.pensize("3")
bob.color("blue")

alice = turtle.Turtle()
alice.penup()
alice.backward(100)
alice.pendown()
alice.right(90)

for item in range(4):
    bob.forward(100)
    bob.left(90)          

for item in range(3):
    alice.forward(100)
    alice.left(120)          


wn.mainloop()      
