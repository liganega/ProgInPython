import turtle

# turtle 모듈에서 정의된 TurtleScreen 클래스의 인스턴스(객체) 생성
# TurtleScreen 클래스의 인스턴스: 그림을 그릴 수 있는 한 장의 도화지 역할 수행
wn = turtle.Screen()
wn.title("Hello, Turtle!")          # 도화지 타이틀 설정
wn.bgcolor("lightyellow")           # 도화지 배경색 설정

# 타이틀 확인
print(wn._title)

# turtle 모듈에서 정의된 Turtle 클래스의 인스턴스(객체) 생성
# Turtle 클래스의 인스턴스: 그림을 그리는 펜 역할 수행 (화살표 모양)
bob = turtle.Turtle()

# 펜 색깔 지정
bob.pencolor("red")

bob.forward(100)                    # 전진하기
bob.left(90)                        # 왼쪽으로 90도 회전하기
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)

# 펜 색깔 확인
print(bob._pencolor)

# X 버튼을 누를 때까지 Screen 객체 계속 유지 기능 수행
wn.mainloop()           
