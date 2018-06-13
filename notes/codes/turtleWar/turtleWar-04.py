'''
* 참조: 다음 사이트의 코드를 파이썬 3에 맞추어 수정 및 정리하였음.
	* http://christianthompson.com/node/41
* 4단계: 충돌 테스트
* 추가 내용
	* random 모듈 추가: 임의로 위치 및 방향 전환하기
	* Character 클래스 기능 추가
		* 캐릭터 충돌 확인 기능: isCollision
		* 캐릭터 충돌 후 임의 위치로 이동 기능: afterCollision
	* 적군 캐릭터 클래스 추가: Enemy
'''

# turtle 모듈 별칭으로 불러오기
import turtle as t
# 캐릭터가 무작위로 방향 바꾸는 용도
import random

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

	# 두 캐릭터의 충돌여부 확인용
	def isCollision(self, other):
		if abs(self.xcor() - other.xcor()) <= 20 and \
		   abs(self.ycor() - other.ycor()) <= 20:
			return True
		else:
			return False

	# 충돌시 임의 위치로 이동하기
	def afterCollision(self):
		x = random.randint(-250, 250)
		y = random.randint(-250, 250)
		self.goto(x, y)


# 주인공 캐릭터 클래스: 기본 캐릭터 상속
class MainPlayer(Character):
	def __init__(self, characterShape, color, startX, startY):
		super().__init__(characterShape, color, startX, startY)
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

# 적군 캐릭터 클래스: 기본 캐릭터 상속
class Enemy(Character):
	def __init__(self, characterShape, color, startx, starty):
		super().__init__(characterShape, color, startx, starty)
		self.step = 6						# 기본 속도
		# 초기 진행 방향 무작위 지정
		self.setheading(random.randint(0,360))

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
# 적군 생성
enemy = Enemy("circle", "yellow", -100, 0)

# 키보드와 메소드 연동하기
wn.onkey(mPlayer.turn_left, "Left")			# 왼쪽 방향기 설정
wn.onkey(mPlayer.turn_right, "Right")		# 오른쪽 방향키 설정
wn.onkey(mPlayer.accelerate, "Up")			# 위쪽 방향키 설정
wn.onkey(mPlayer.decelerate, "Down")		# 아래쪽 방향키 설정
wn.listen()									# 화면 위 이벤트 감지

# 주인공과 적군의 충돌 테스트
while True:
	mPlayer.move()
	enemy.move()

	# 주인공과 적군이 충돌하면 적군을 임의의 위치로 보내기
	if mPlayer.isCollision(enemy):
		enemy.afterCollision()

wn.mainloop()
