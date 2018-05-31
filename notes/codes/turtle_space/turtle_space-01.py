# 1단계: 시작하기

import os
import random

# t.모듈 불러오기
import turtle as t

# 윈도우 창 생성
wn = t.Screen()
# 배경 색깔 변경
wn.bgcolor("black")
# 거북이의 움직임을 보다 빠르게 설정함: 숫자 커질 수록 빨라짐
wn.tracer(1)

class Sprite(t.Turtle):
	def __init__(self, spriteshape, color, startx, starty):
		t.Turtle.__init__(self, shape = spriteshape)
		self.hideturtle()
		self.speed(0)					# 최고 속도 설정
		self.penup()					# 선 숨기기
		self.color(color)				# 색 지정
		self.setundobuffer(1)			# undo 사용 횟수 설정
		self.goto(startx, starty)		# 지정 좌표로 이동
		self.showturtle()				# 지정 좌료로 이동 후 출현
#		self.speed = 1

#Create my sprites
player = Sprite("triangle", "white", 0, 0)

wn.mainloop()
