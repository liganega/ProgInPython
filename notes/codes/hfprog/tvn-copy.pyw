from tkinter import *
import pygame.mixer

def play_correct_sound():
    num_good.set(num_good.get() + 1)
    num_total.set(num_total.get() + 1)
    correct_s.play()

def play_wrong_sound():
    num_bad.set(num_bad.get() + 1)
    num_total.set(num_total.get() + 1)
    wrong_s.play()

app = Tk()
app.title("TVN Game Show")
app.geometry('300x110+200+100')

frame1 = Frame(app)
frame1.pack()

frame2 = Frame(app)
frame2.pack(side = BOTTOM)

frame3 = Frame(app)
frame3.pack(side = BOTTOM)

sounds = pygame.mixer
sounds.init()

correct_s = sounds.Sound("sounds/correct.wav")
wrong_s   = sounds.Sound("sounds/wrong.wav")

num_good = IntVar()
num_good.set(0)
num_bad = IntVar()
num_bad.set(0)
num_total = IntVar()
num_total.set(0)

lab01 = Label(frame1, text = "정답 또는 오답을 누르세요!", fg='blue', height=3)
lab01.pack(side = BOTTOM)

lab = Label(frame3, text='총 문제 개수:')
lab.pack(side='left')
lab0 = Label(frame3, textvariable = num_total)
lab0.pack(side = 'left')

lab1 = Label(frame2, textvariable = num_good)
lab1.pack(side = 'left')

lab2 = Label(frame2, textvariable = num_bad)
lab2.pack(side = 'right')

b1 = Button(frame2, text = "정답", width = 7, command = play_correct_sound)
b1.pack(side = 'left',  padx = 10, pady = 10)

b2 = Button(frame2, text = "오답", width = 7, command = play_wrong_sound)
b2.pack(side = 'right', padx = 10, pady = 10)

app.mainloop()
