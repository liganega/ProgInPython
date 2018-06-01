'''
* 참조: 다음 사이트의 코드를 파이썬 3에 맞추어 수정하였음.
	* http://christianthompson.com/node/41
* 3단계: 게임 무대 추가
* 게임 무대 설정 클래서 선언: Stage
* Character 클래스 move 메소드 기능 제한: 모든 게임 캐릭터가 무대 못 벗어나게 하기
'''

# turtle 모듈 별칭으로 불러오기
import turtle as t

# 윈도우 창 생성 및 설정
wn = t.Screen()
wn.bgcolor("black")							# 창 배경 색깔
# wn.tracer(1)								# 거북이의 움직임: 큰 숫자 빨라짐

# 기본 캐릭터 설정: Turtle 클래스 상속
class Character(t.Turtle):
	def __init__(self, characterShape, color, startX, startY):
		super().__init__(shape = characterShape)

		# 거북이 초기 설정
		super().hideturtle()				# 지정 좌표로 이동 전 숨김
		super().speed(0)					# 최고 속도 설정
		super().penup()						# 선 숨김
		super().color(color)				# 색 지정
		super().setundobuffer(1)			# undo 사용 횟수 설정
		super().goto(startX, startY)		# 지정 좌표로 이동
		super().showturtle()				# 지정 좌료로 이동 후 출현

		# 새로운 인스턴스 변수
		self.step = 1						# 이동 속도 조절용

	# 새로운 인스턴스 메소드
	def move(self):							# 지정 속도 이동 메소드
		self.fd(self.step)

		# 캐릭터들이 스테이지 경계에서 튕겨서 되 돌아가게 만들기
		if self.xcor() > 290:
			self.setx(290)
			self.rt(60)

		if self.xcor() < -290:
			self.setx(-290)
			self.rt(60)

		if self.ycor() > 290:
			self.sety(290)
			self.rt(60)

		if self.ycor() < -290:
			self.sety(-290)
			self.rt(60)

# 주인공 캐릭터 클래스: 기본 캐릭터 상속
class MainPlayer(Character):
	def __init__(self, characterShape, color, startX, startY):
		Character.__init__(self, characterShape, color, startX, startY)
		self.step = 4						# 이동 속도 조절용
		self.lives = 3						# 생명 카운트

	# 기능 추가
	def turn_left(self):					# 왼쪽으로 회전
		self.lt(45)

	def turn_right(self):					# 오른쪽으로 회전
		self.rt(45)

	def accelerate(self):					# 가속
		self.step += 1

	def decelerate(self):					# 감속
		self.step -= 1

# 게임 무대 클래스
class Stage():
	def __init__(self):
		# 무대 표시 사항: 레벨(level), 점수(score), 생명 횟수(lives)
		self.level = 1
		self.score = 0
		self.lives = 3

		# 게임상태 지정: splash, setup, playing, restart, gameover
		self.state = "playing"

		# 펜 기능 터틀 인스턴스 생성
		self.pen = t.Turtle()

	# 스테이지 경계 그리기
	def draw_border(self):
		self.pen.speed(0)
		self.pen.color("white")
		self.pen.pensize(3)
		self.pen.penup()
		self.pen.goto(-300, 300)
		self.pen.pendown()
		for side in range(4):
			self.pen.fd(600)
			self.pen.rt(90)
		self.pen.penup()
		self.pen.ht()

################
### 게임 테스트 ###
################

# 게임 무대 생성
stage = Stage()
stage.draw_border()

# 주인공 생성
mPlayer = MainPlayer("triangle", "white", 0, 0)

# 키보드와 메소드 연동하기
wn.onkey(mPlayer.turn_left, "Left")			# 왼쪽 방향기 설정
wn.onkey(mPlayer.turn_right, "Right")		# 오른쪽 방향키 설정
wn.onkey(mPlayer.accelerate, "Up")			# 위쪽 방향키 설정
wn.onkey(mPlayer.decelerate, "Down")		# 아래쪽 방향키 설정
wn.listen()									# 화면 위 이벤트 감지

# 주인공 움직임 테스트: 계속 움직임. 방향키 사용하여 조정 가능
while True:
	mPlayer.move()

wn.mainloop()
