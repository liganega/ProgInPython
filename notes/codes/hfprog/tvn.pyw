from tkinter import *
import pygame.mixer
from packTogether import *

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
app.geometry('600x110+200+100')
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

lab = Label(app, text='정답 또는 오답 버튼을 누르세요.', height = 3)
lab0 = Label(app, textvariable = num_total)

two_labs = PackTogether(app, lab, lab0)
two_labs.pack()

lab1 = Label(app, textvariable = num_good)
lab1.pack(side = 'left')

lab2 = Label(app, textvariable = num_bad)
lab2.pack(side = 'right')

b1 = Button(app, text = "정답", width = 7, command = play_correct_sound)
b1.pack(side = 'left',  padx = 10, pady = 10)

b2 = Button(app, text = "오답", width = 7, command = play_wrong_sound)
b2.pack(side = 'right', padx = 10, pady = 10)

app.mainloop()
