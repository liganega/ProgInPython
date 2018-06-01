# 1단계: 시작하기

# turtle 모듈 별칭으로 불러오기
import turtle as t

# 윈도우 창 생성
wn = t.Screen()
wn.bgcolor("black")							# 창 배경 색깔
# wn.tracer(0)								# 거북이의 움직임: 큰 숫자 빨라짐

# 캐릭터 기본 설정: Turtle 클래스 상속
class Character(t.Turtle):
	def __init__(self, characterShape, color, startx, starty):
		super().__init__(shape = characterShape)
		super().hideturtle()				# 지정 좌표로 이동 전 숨김
		super().speed(0)					# 최고 속도 설정
		super().penup()						# 선 숨김
		super().color(color)				# 색 지정
		super().setundobuffer(1)			# undo 사용 횟수 설정
		super().goto(startx, starty)		# 지정 좌표로 이동
		super().showturtle()				# 지정 좌료로 이동 후 출현

# 기본 캐릭터 하나 생성: 시작 지점 위로 약간 이동
triTurtle = Character("triangle", "white", 0, 80)

# 기본 설정 확인
wn.tracer(1)								# 숫자를 수정하며 실험할 것
triTurtle.pd()

step= 2
for i in range(200):
    triTurtle.fd(step)
    triTurtle.rt(120)
    step += 3

wn.mainloop()
