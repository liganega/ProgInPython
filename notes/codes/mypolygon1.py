import turtle

# turtle 모듈에서 정의된 Screen 클래스의 인스턴스(객체) 생성
# Screen 클래스의 인스턴스: 그림을 그릴 수 있는 한 장의 도화지 역할 수행
wn = turtle.Screen()

# turtle 모듈에서 정의된 Turtle 클래스의 인스턴스(객체) 생성
# Turtle 클래스의 인스턴스: 그림을 그리는 펜 역할 수행 (화살표 모양)
bob = turtle.Turtle()

bob.forward(100)       # 전진하기
bob.left(90)           # 왼쪽으로 90도 회전하기
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)

wn.mainloop()           # X 버튼을 누를 때까지 Screen 객체 계속 유지 기능 수행
