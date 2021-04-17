from tkinter import *
from tkinter.ttk import *
import tkinter.font as tkFont

window = Tk()

window.geometry("430x520")
window.configure(bg="#383838")
window.resizable(False, False)
window.title("Calculator")

keyColor = '#202020'

equation = ''
operation = ''
rez = None
floatNumber = False

# Button themes

s = Style(window)
s.theme_use('clam')
s.configure('flat.TButton', borderwidth=0, background=keyColor, foreground='white')

sPressed = Style(window)
sPressed.theme_use('clam')
sPressed.configure('flatPressed.TButton', borderwidth=0, background='#b36200', foreground='white')

# Clears the label or everything if the label is empty

def clearButtonFunc():
	global equation
	global floatNumber
	global rez
	global rezultLabel
	global bClear
	floatNumber = False
	print(equation)
	if bClear.cget('text') == 'C' and rez != '':
		print(bClear.cget('text'))
		bClear.configure(text="AC")
		resetEquation()
		buttonReset()
		sign = ''
	elif bClear.cget('text') == 'AC':
		rez = None
	elif equation == '':
		bClear.configure(text="C")
	rezultLabel['text'] = equation

# When a key on the calculator is pressed it adds it to the label and to the number

def numberCreate(x):
	global equation
	global floatNumber
	buttonReset()
	if floatNumber:
		if x != '.':
			equation = equation + str(x)
			bClear.configure(text="C")
	else:
		if x == '.' and equation == '':
			equation = '0.'
			floatNumber = True
			bClear.configure(text="C")
		elif x == '.':
			equation = equation + '.'
			floatNumber = True
		else:
			print(x)
			equation = equation + str(x)
			bClear.configure(text="C")
	print(equation)
	rezultLabel['text'] = equation

# Deletes one character

def backspaceFunction():
	global equation
	global floatNumber
	if len(equation) >= 1:
		equation = equation[:-1]
		size = len(equation)
		if size > 1 and equation[-1] == '.':
			floatNumber = False
			equation = equation[:-1]
		rezultLabel['text'] = equation

# Resets the buttons to the initial state

def buttonReset():
	bAdd.configure(style='flat.TButton')
	bSub.configure(style='flat.TButton')
	bDiv.configure(style='flat.TButton')
	bMul.configure(style='flat.TButton')

def resetEquation():
	global equation
	global floatNumber
	equation = ''
	floatNumber = False

def enterFunction():
	global operation
	global rez
	global equation
	global floatNumber
	buttonReset()
	if operation == '+':
		if equation != '':
			rez = rez + float(equation)
			resetEquation()
	if operation == '-':
		if equation != '':
			rez = rez - float(equation)
			resetEquation()
	if operation == '*':
		if equation != '':
			rez = rez * float(equation)
			resetEquation()
	if operation == '/':
		if equation != '':
			rez = rez / float(equation)
			resetEquation()
	if rez == None:
		rezultLabel['text'] = 0
	else:
		rezultLabel['text'] = str(rez)
	operation = ''

def plusFunction():
	global equation
	global rez
	global operation
	global floatNumber
	if equation != '':
		enterFunction()
	operation = '+'
	buttonReset()
	bAdd.configure(style='flatPressed.TButton')
	if operation == '':
		rez = float(equation)
	elif rez == None:
		if equation == '':
			rez = 0
		else: 
			rez = float(equation)
		rezultLabel['text'] = ''
		resetEquation()
	else:
		if equation != '':
			rez = float(equation) + rez

def minusFunction():
	global equation
	global rez
	global operation
	global floatNumber
	if equation != '':
		enterFunction()
	operation = '-'
	buttonReset()
	bSub.configure(style='flatPressed.TButton')
	if operation == '':
		rez = float(equation)
	elif rez == None:
		if equation == '':
			rez = 0
		else: 
			rez = float(equation)
		rezultLabel['text'] = ''
		resetEquation()
	else:
		if equation != '':
			rez = float(equation) + rez

def divideFunction():
	global equation
	global rez
	global operation
	global floatNumber
	if equation != '':
		enterFunction()
	operation = '/'
	buttonReset()
	bDiv.configure(style='flatPressed.TButton')
	if operation == '':
		rez = float(equation)
	elif rez == None:
		if equation == '':
			rez = 0
		else: 
			rez = float(equation)
		rezultLabel['text'] = ''
		resetEquation()
	else:
		if equation != '':
			rez = float(equation) + rez

def multiplyFunction():
	global equation
	global rez
	global operation
	global floatNumber
	if equation != '':
		enterFunction()
	operation = '*'
	buttonReset()
	bMul.configure(style='flatPressed.TButton')
	if operation == '':
		rez = float(equation)
	elif rez == None:
		if equation == '':
			rez = 0
		else: 
			rez = float(equation)
		rezultLabel['text'] = ''
		resetEquation()
	else:
		if equation != '':
			rez = float(equation) + rez

  
# Text
fontStyle = tkFont.Font(family="Lucida Grande", size=30)
rezultLabel = Label(window, text = '', font=fontStyle, background='#383838', foreground='white', justify='right')
rezultLabel.pack(side = RIGHT, anchor=NW, pady=60)

# Buttons
b1 = Button(window, style='flat.TButton', text='1', command = lambda: numberCreate(1))
b2 = Button(window, style='flat.TButton', text='2', command = lambda: numberCreate(2))
b3 = Button(window, style='flat.TButton', text='3', command = lambda: numberCreate(3))
b4 = Button(window, style='flat.TButton', text='4', command = lambda: numberCreate(4))
b5 = Button(window, style='flat.TButton', text='5', command = lambda: numberCreate(5))
b6 = Button(window, style='flat.TButton', text='6', command = lambda: numberCreate(6))
b7 = Button(window, style='flat.TButton', text='7', command = lambda: numberCreate(7))
b8 = Button(window, style='flat.TButton', text='8', command = lambda: numberCreate(8))
b9 = Button(window, style='flat.TButton', text='9', command = lambda: numberCreate(9))
b0 = Button(window, style='flat.TButton', text='0', command = lambda: numberCreate(0))
bClear = Button(window, style='flat.TButton', text='C', command = clearButtonFunc)
bDot = Button(window, style='flat.TButton', text='.', command = lambda: numberCreate('.'))
bAdd = Button(window, style='flat.TButton', text='+', command = plusFunction)
bSub = Button(window, style='flat.TButton', text='-', command = minusFunction)
bMul = Button(window, style='flat.TButton', text='*', command = multiplyFunction)
bDiv = Button(window, style='flat.TButton', text='/', command = divideFunction)
bEqu = Button(window, style='flat.TButton', text='=', command = enterFunction)
bBck = Button(window, style='flat.TButton', text='<--', command = backspaceFunction)

gapx = 10
gapy = 120

def placeButtons():
	b1.place(height=70, width=80, x=gapx+0, y=gapy+240)
	b2.place(height=70, width=80, x=gapx+90, y=gapy+240)
	b3.place(height=70, width=80, x=gapx+180, y=gapy+240)
	b4.place(height=70, width=80, x=gapx+0, y=gapy+160)
	b5.place(height=70, width=80, x=gapx+90, y=gapy+160)
	b6.place(height=70, width=80, x=gapx+180, y=gapy+160)
	b7.place(height=70, width=80, x=gapx+0, y=gapy+80)
	b8.place(height=70, width=80, x=gapx+90, y=gapy+80)
	b9.place(height=70, width=80, x=gapx+180, y=gapy+80)
	b0.place(height=70, width=170, x=gapx+0, y=gapy+320)
	bClear.place(height=70, width=80, x=gapx+0, y=gapy+0)
	bDot.place(height=70, width=80, x=gapx+180, y=gapy+320)
	bEqu.place(height=70, width=140, x=gapx+270, y=gapy+320)
	bAdd.place(height=70, width=140, x=gapx+270, y=gapy+240)
	bSub.place(height=70, width=140, x=gapx+270, y=gapy+160)
	bMul.place(height=70, width=140, x=gapx+270, y=gapy+80)
	bDiv.place(height=70, width=170, x=gapx+90, y=gapy+0)
	bBck.place(height=70, width=140, x=gapx+270, y=gapy+0)



def main():
	placeButtons()
	window.mainloop()

if __name__ == "__main__":
	main()