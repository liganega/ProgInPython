from tkinter import *
import pygame.mixer

class PackTogether(Frame):
    def __init__(self, app, lab1, lab2):
        Frame.__init__(self, app)

        self.lab1 = lab1
        self.lab1.pack(side = LEFT)

        self.lab2 = lab2
        self.lab2.pack(side = RIGHT)
