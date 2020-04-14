from tkinter import *


def btnClick(numbers):
	global operator
	operator = operator + str(numbers)
	text_input.set(operator) 

def btnClearDisplay():
    global operator
    operator = ""
    text_input.set("")

def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    #operator = "" #Sem essa linha consigo reaproveitar o resultado da equação anterior para realizar uma nova
    

cal = Tk()
cal.title("Calculator")
operator=""
text_input = StringVar()


textDisplay = Entry(cal, font=('arial', 20, 'bold'), textvariable = text_input, bd=30, insertwidth=4, bg="ghost white", justify='center').grid(columnspan=4)


btn7 = Button(cal, padx=16, bd=8, fg="light slate gray", font=('arial', 20, 'bold'), text="7", bg="ghost white", command=lambda:btnClick(7)).grid(row=1, column=0)
btn8 = Button(cal, padx=16, bd=8, fg="light slate gray", font=('arial', 20, 'bold'), text="8", bg="ghost white", command=lambda:btnClick(8)).grid(row=1, column=1)
btn9 = Button(cal, padx=16, bd=8, fg="light slate gray", font=('arial', 20, 'bold'), text="9", bg="ghost white", command=lambda:btnClick(16)).grid(row=1, column=2)
addition = Button(cal, padx=12, bd=8, fg="light slate gray", font=('arial', 20, 'bold'), text="+", bg="ghost white", command=lambda:btnClick("+")).grid(row=1, column=3)


btn4 = Button(cal, padx=16, bd=8, fg="light slate gray", font=('arial', 20, 'bold'), text="4", bg="ghost white", command=lambda:btnClick(4)).grid(row=2, column=0)
btn5 = Button(cal, padx=16, bd=8, fg="light slate gray", font=('arial', 20, 'bold'), text="5", bg="ghost white", command=lambda:btnClick(5)).grid(row=2, column=1)
btn6 = Button(cal, padx=16, bd=8, fg="light slate gray", font=('arial', 20, 'bold'), text="6", bg="ghost white", command=lambda:btnClick(6)).grid(row=2, column=2)
subtraction = Button(cal, padx=16, bd=8, fg="light slate gray", font=('arial', 20, 'bold'), text="-", bg="ghost white", command=lambda:btnClick("-")).grid(row=2, column=3)


btn1 = Button(cal, padx=16, bd=8, fg="light slate gray", font=('arial', 20, 'bold'), text="1", bg="ghost white", command=lambda:btnClick(1)).grid(row=3, column=0)
btn2 = Button(cal, padx=16, bd=8, fg="light slate gray", font=('arial', 20, 'bold'), text="2", bg="ghost white", command=lambda:btnClick(2)).grid(row=3, column=1)
btn3 = Button(cal, padx=16, bd=8, fg="light slate gray", font=('arial', 20, 'bold'), text="3", bg="ghost white", command=lambda:btnClick(3)).grid(row=3, column=2)
multiply = Button(cal, padx=15, bd=8, fg="light slate gray", font=('arial', 20, 'bold'), text="*", bg="ghost white", command=lambda:btnClick("*")).grid(row=3, column=3)


btn0 = Button(cal, padx=16, bd=8, fg="light slate gray", font=('arial', 20, 'bold'), text="0", bg="ghost white", command=lambda:btnClick(0)).grid(row=4, column=0)
btnClear = Button(cal, padx=16, bd=8, fg="light slate gray", font=('arial', 20, 'bold'), text="c", bg="ghost white", command=btnClearDisplay).grid(row=4, column=1)
btnEquals = Button(cal, padx=16, bd=8, fg="light slate gray", font=('arial', 20, 'bold'), text="=", bg="ghost white", command=btnEqualsInput).grid(row=4, column=2)
division = Button(cal, padx=15.5, bd=8, fg="light slate gray", font=('arial', 20, 'bold'), text="/", bg="ghost white", command=lambda:btnClick("/")).grid(row=4, column=3)


cal.mainloop()
