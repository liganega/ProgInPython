from tkinter import *
# pygame.mixer를 sounds라는 애칭으로 불러오기
# 애칭은 임의로 지정 가능
import pygame.mixer as sounds

# 정답/오답 소리 지정하기
sounds.init()
correct_s = sounds.Sound("codes/sounds/correct.wav")
wrong_s   = sounds.Sound("codes/sounds/wrong.wav")

app = Tk()
app.title("파이썬 퀴즈!")
app.geometry('300x140+700+100')

num_good = IntVar()
num_good.set(0)    

num_bad = IntVar() 
num_bad.set(0)     

num_total = IntVar()
num_total.set(0)    

# 정답/오답 버튼을 누를 때 실행되는 함수에 소리기능 추가
def play_correct_sound():
    num_good.set(num_good.get() + 1)
    num_total.set(num_total.get() + 1)
    correct_s.play()

def play_wrong_sound():
    num_bad.set(num_bad.get() + 1)
    num_total.set(num_total.get() + 1)
    wrong_s.play()

frame1 = Frame(app)
frame1.pack()
frame2 = Frame(app)
frame2.pack()
frame3 = Frame(app)
frame3.pack()

lab1 = Label(frame1, text = "정답 또는 오답 버튼을 누르세요!", fg='red', height=3)
lab1.pack()

lab2 = Label(frame2, text='총 문제 개수:')
lab2.pack(side='left')

lab3 = Label(frame2, textvariable = num_total)
lab3.pack(side='right')

lab4 = Label(frame3, textvariable = num_good)
lab4.pack(side = 'left')

lab5 = Label(frame3, textvariable = num_bad)
lab5.pack(side = 'right')

# command 키워드 매개 변수에 특정 기능 추가하기
b1 = Button(frame3, text = "정답", width = 8, command = play_correct_sound)
b1.pack(side = 'left',  padx = 10, pady = 10)

b2 = Button(frame3, text = "오답", width = 8, command = play_wrong_sound)
b2.pack(side = 'right', padx = 10, pady = 10)

app.mainloop()