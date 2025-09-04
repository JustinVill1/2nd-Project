import tkinter as tk

calculation = ""

#function that adds the button that I am pressing into the result box
def AddtoCalculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0,calculation)

#function that evaluates what is in the result box
#if whats in the text box doesnt make sense, an error is returned
def evaluateCalculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0,"end")
        text_result.insert(1.0, calculation)
    except:
        clearField()
        text_result.insert(1.0,"Error")

#this function clears the result box when it is called
#usually cleared with AC button
def clearField():
    global calculation
    calculation = ""
    text_result.delete(1.0,"end")

def Pos_to_Neg():
    current = text_result.get()
    if current:
        if current.startswith('-'):
            text_result.delete(0,tk.END)
            text_result.insert(0,current[1:])
        else:
            text_result.delete(0,tk.END)
            text_result.insert(0, '-' + current)

def Percentage():
    global calculation
    calculation = calculation * .01
    text_result.delete(0,tk.END)
    text_result.insert(0,calculation)


#This is assigned the object Tk to root
#this is the size of the pop up that shows up when the code is ran
root = tk.Tk()
root.geometry("300x275")

#this controls how big the result box is 
text_result = tk.Text(root, height=2, width=16, font=("Arial",24))
text_result.grid(columnspan=5)

#This is the button that clears the result box of calling the previous field
#the functions is not called it is assigned to command so there are no parameters after clearField
#This also controls where the AC button goes on our calculator
buttonAC = tk.Button(root,text="AC",command=clearField,width=5,font=("Arial",14))
buttonAC.grid(row=1,column=1)




button1 = tk.Button(root,text="1",command=lambda: AddtoCalculation(1),width=5,font=("Arial",14))
button1.grid(row=3,column=1)

button2 = tk.Button(root,text="2",command=lambda: AddtoCalculation(2),width=5,font=("Arial",14))
button2.grid(row=3,column=2)

button3 = tk.Button(root,text="3",command=lambda: AddtoCalculation(3),width=5,font=("Arial",14))
button3.grid(row=3,column=3)

button4 = tk.Button(root,text="4",command=lambda: AddtoCalculation(4),width=5,font=("Arial",14))
button4.grid(row=4,column=1)

button5 = tk.Button(root,text="5",command=lambda: AddtoCalculation(5),width=5,font=("Arial",14))
button5.grid(row=4,column=2)

button6 = tk.Button(root,text="6",command=lambda: AddtoCalculation(6),width=5,font=("Arial",14))
button6.grid(row=4,column=3)

button7 = tk.Button(root,text="7",command=lambda: AddtoCalculation(7),width=5,font=("Arial",14))
button7.grid(row=5,column=1)

button8 = tk.Button(root,text="8",command=lambda: AddtoCalculation(8),width=5,font=("Arial",14))
button8.grid(row=5,column=2)

button9 = tk.Button(root,text="9",command=lambda: AddtoCalculation(9),width=5,font=("Arial",14))
button9.grid(row=5,column=3)

button0 = tk.Button(root,text="0",command=lambda: AddtoCalculation(0),width=5,font=("Arial",14))
button0.grid(row=6,column=2)

buttonPlus = tk.Button(root,text="+",command=lambda: AddtoCalculation("+"),width=5,font=("Arial",14))
buttonPlus.grid(row=5,column=4)

buttonMinus = tk.Button(root,text="-",command=lambda: AddtoCalculation("-"),width=5,font=("Arial",14))
buttonMinus.grid(row=4,column=4)

buttonMult = tk.Button(root,text="x",command=lambda: AddtoCalculation("*"),width=5,font=("Arial",14))
buttonMult.grid(row=3,column=4)

buttonDivide = tk.Button(root,text="/",command=lambda: AddtoCalculation("/"),width=5,font=("Arial",14))
buttonDivide.grid(row=1,column=4)

buttonDot = tk.Button(root,text=".",command=lambda: AddtoCalculation("."),width=5,font=("Arial",14))
buttonDot.grid(row=6,column=3)

buttonEquals = tk.Button(root,text="=",command=evaluateCalculation,width=5,font=("Arial",14))
buttonEquals.grid(row=6,column=4)




root.mainloop()