from tkinter import *

def iCalc(source, side):
    storeObj = Frame(source, borderwidth=4, bd=4, bg="powder blue")
    storeObj.pack(side=side, expand =YES, fill =BOTH)
    return storeObj

def button(source, side, text, command=None):
    storeObj = Button(source, text=text, command=command)
    storeObj.pack(side=side, expand = YES, fill=BOTH)
    return storeObj

class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'arial 20 bold')
        self.pack(expand = YES, fill =BOTH)
        self.master.title('Calculator')

        # geometry 불필요. pack의 설정으로 인해 신축성 있게 크기 조정됨.
        # self.master.geometry('300x140+700+100')

        # display 변수 생성
        #   - 눌리는 버튼들을 모두 입력 받음.
        #   - 등호(=)가 눌릴 경우 계산 결과가 저장됨.
        display = StringVar()

        # 디스플레이 창(Entry) 생성
        #   - display에 저장된 값을 보여줌.
        Entry(self, relief=RIDGE, textvariable=display, justify='right', bd=30, bg="powder blue").pack(side=TOP, expand=YES, fill=BOTH)

        # 캔슬 버튼: C
        # 먼저 프레임 생성 후 버튼 추가
        erase = iCalc(self, TOP)
        button(erase, LEFT, 'C', lambda storeObj=display, q='C': storeObj.set(''))

        # for clearButton in (["C"]):
        #     erase = iCalc(self, TOP)
        #     for ichar in clearButton:
        #         button(erase, LEFT, ichar, lambda storeObj=display, q=ichar: storeObj.set(''))

        for numButton in ("789/", "456*", "123-", "0.+"):
            FunctionNum = iCalc(self, TOP)
            for iEquals in numButton:
                button(FunctionNum, LEFT, iEquals, lambda storeObj=display, q=iEquals: storeObj.set(storeObj.get() + q))

        EqualButton = iCalc(self, TOP)
        btniEquals = button(EqualButton, LEFT, '=')
        # '+'가 왜 필요한지 모르겠음.
        btniEquals.bind('<ButtonRelease-1>', lambda event,s=self, storeObj=display: s.calc(storeObj), '+')

        # for iEquals in "=":
        #     if iEquals == '=':
        #         btniEquals = button(EqualButton, LEFT, iEquals)
        #         btniEquals.bind('<ButtonRelease-1>', lambda e,s=self, storeObj=display: s.calc(storeObj), '+')
        #     else:
        #         btniEquals = button(EqualButton, LEFT, iEquals, lambda storeObj=display, s=' %s ' % iEquals: storeObj.set(storeObj.get() + s))

    def calc(self, display):
            try:
                display.set(eval(display.get()))
            except:
                display.set("ERROR")

if __name__=='__main__':
    app().mainloop()