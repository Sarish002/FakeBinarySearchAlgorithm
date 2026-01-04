from ttkbootstrap import *
import tkinter
import math
import time

root = Window(themename="superhero")
root.geometry("800x500")
root.title("number.ai")
img = tkinter.PhotoImage(file="Game.png")
root.iconphoto(False, img)

number = 50
class Fract:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.val = numerator / denominator
        self.lowFract = ((2 * numerator) - 1, (2 * numerator))
        self.highFract = ((2 * numerator) + 1, (2 * numerator))
mainFract = Fract(1, 2)

style = Style()
style.configure("success.TButton", font=("Agency FB", 40), padding=10,
                borderwidth=2, relief="solid", bordercolor="white") #NEW!!

label = Label(root, text="Think of a number between 1 and 100",
              font=("Agency FB", 30, "bold"))
label.place(relx=0.5, rely=0.1, anchor=CENTER)

labelNum = Label(root, text=number,
                 font=("Agency FB", 40, "bold"))
labelNum.place(relx=0.5, rely=0.35, anchor=CENTER)

labelAsk = Label(root, text="Is this number: ",
                 font=("Agency FB", 25, "bold"))
labelAsk.place(relx=0.5, rely=0.5, anchor=CENTER)

def SayYes():
    global labelNum, labelAsk, number, mainFract
    labelNum.config(text="👍🏼")
    labelAsk.config(text="Yay! Let's go! 🙂")
    labelNum.update_idletasks()
    labelAsk.update_idletasks()
    for i in range(100000000):
        pass
    number = 50
    labelNum.config(text=number)
    labelAsk.config(text="Is this number: ")
    mainFract = Fract(1, 2)

def SayHigh():
    global mainFract, number
    mainFract = Fract(mainFract.lowFract[0], mainFract.lowFract[1])
    num = number
    number *= mainFract.val
    number = int(number)
    if int(num) == number:
        number -= 1
    labelNum.config(text=number)

def SayLow():
    global mainFract, number
    mainFract = Fract(mainFract.highFract[0], mainFract.highFract[1])
    num = number
    number *= mainFract.val
    number = int(number)
    if int(num) == number:
        number += 1

    labelNum.config(text=number)

buttonYes = Button(root, text="Equal?", command=SayYes, style="success.TButton")
buttonHigh = Button(root, text="High?", command=SayHigh, style="success.TButton")
buttonLow = Button(root, text="Low?", command=SayLow, style="success.TButton")

buttonYes.place(relx=0.5, rely=0.75, anchor=CENTER)
buttonHigh.place(relx=0.75, rely=0.75, anchor=CENTER)
buttonLow.place(relx=0.25, rely=0.75, anchor=CENTER)

root.mainloop()