from tkinter import *

class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'arial 20 bold')
        self.pack(expand = YES, fill =BOTH)
        self.master.title('계산기')

        display = StringVar()
        Entry(self, relief=RIDGE, textvariable=display, justify='right', 
              bd=30, bg="powder blue").pack(side=TOP, expand=YES, fill=BOTH)


calculator = app()
calculator.mainloop()