'''
* 참조: 다음 사이트의 코드를 파이썬 3에 맞추어 수정하였음.
	* http://christianthompson.com/node/41
* 2단계: 플레이어 추가 및 움직이기
* 기본 Character 클래스에 기능 추가
	* 움직임 기능 추가: move 메소드
	* 움직임 기본 속도 지정 변수 선언: step 인스턴스 변수
* 주인공 클래스 선언: MainPlayer
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

################
### 게임 테스트 ###
################

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
