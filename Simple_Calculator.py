from ast import Delete
from distutils.cmd import Command
from logging.config import valid_ident
import tkinter
from tkinter import DISABLED, RIGHT, END
from tkinter.font import NORMAL
from tkinter.ttk import Button

#Define color and fonts
black_clr = "#000000"
oxford_blue = '#14213D'
yellow_clr = "#FCA311"
platinum = "#E5E5E5"
icon_green = "#93af22"
buttons_font = ('Arial', 18)
display_font = ("Arial", 30)

# Define Windows
root = tkinter.Tk()
root.title("Calculator")
root.iconbitmap("calc.ico")
root.geometry("300x400")
root.resizable(0,0)
root.config(bg = black_clr)


#Define functions

def submit_number(number):
    if display.get() == "0":
         display.delete(0,END)
    display.insert(END, number)

# Lock decimal button if clicked before
    if "." in display.get():
        decimal_button.config(state=DISABLED)


def operate(operator):
    global first_number
    global operation
    operation = operator
    first_number = display.get()
    display.delete(0,END)

    
    add_button.config(state=DISABLED)
    square_button.config(state=DISABLED)
    multiply_button.config(state=DISABLED)
    subtract_button.config(state=DISABLED)
    exponent_button.config(state=DISABLED)
    divide_button.config(state=DISABLED)
    inverse_button.config(state=DISABLED)

    decimal_button.config(state=NORMAL)

def equal():

    if operation == "add":
        value = float(first_number) + float(display.get())

    elif operation == "subtract":
        value = float(first_number) - float(display.get())
    
    elif operation == "multiply":
        value = float(first_number) * float(display.get())
    
    elif operation == "exponent":
        value = float(first_number) ** float(display.get())
    
    elif operation == "divide":
        if display.get() == "0":
            value = "ERROR"
        else:
            value = float(first_number) / float(display.get())
    
    display.delete(0,END)
    display.insert(0, value)
    if "." in display.get():
        decimal_button.config(state=DISABLED)

    enable_button()

def enable_button():
    
    add_button.config(state=NORMAL)
    square_button.config(state=NORMAL)
    multiply_button.config(state=NORMAL)
    subtract_button.config(state=NORMAL)
    exponent_button.config(state=NORMAL)
    divide_button.config(state=NORMAL)
    inverse_button.config(state=NORMAL)


def clear():
    display.delete(0,END)
    display.insert(0, int(0))
    decimal_button.config(state=NORMAL)
    enable_button()

def inverse():
    if display.get() == "0":
        value = "ERROR"
    else:
        value = 1/float(display.get())
    display.delete(0,END)
    display.insert(0,value)

def square():
    value = float(display.get())**2
    display.delete(0,END)
    display.insert(0,value)

def negate():
    value = float(display.get())*-1
    display.delete(0,END)
    display.insert(0,value)

#GUI layout
# Define frames
display_frame = tkinter.LabelFrame(root)
button_frame = tkinter.LabelFrame(root)

display_frame.pack()
button_frame.pack()

#Layout for display frame
display = tkinter.Entry(display_frame, width= 50, font = display_font, bg=platinum, borderwidth=5, justify= RIGHT)
display.insert(0, int(0))
display.pack(padx=5,pady=5)

# Layout for buuton frame
clear_button = tkinter.Button(button_frame, text = "Clear", font= buttons_font, bg = platinum, fg = oxford_blue, command= clear)
quit_button = tkinter.Button(button_frame, text = "Quit", font= buttons_font, bg = platinum,fg = oxford_blue, command=root.destroy)

inverse_button = tkinter.Button(button_frame, text = "1/x", font = buttons_font,bg = yellow_clr, fg = oxford_blue, command=inverse )
square_button = tkinter.Button(button_frame, text = "x^2", font = buttons_font, bg = yellow_clr, fg = oxford_blue, command=square)
exponent_button = tkinter.Button(button_frame, text = "x^n", font = buttons_font, bg = yellow_clr, fg = oxford_blue, command= lambda:operate("exponent"))
divide_button = tkinter.Button(button_frame, text = " / ", font = buttons_font, bg = yellow_clr, fg = oxford_blue, command= lambda:operate("divide"))
multiply_button = tkinter.Button(button_frame, text = " * ", font = buttons_font, bg = yellow_clr, fg = oxford_blue, command= lambda:operate("multiply"))
subtract_button = tkinter.Button(button_frame, text = " - ", font = buttons_font,  bg = yellow_clr, fg = oxford_blue, command= lambda:operate("subtract"))
add_button = tkinter.Button(button_frame, text = " + ", font = buttons_font,  bg = yellow_clr, fg = oxford_blue, command= lambda:operate("add"))
equal_button = tkinter.Button(button_frame, text = " = ", font = buttons_font,  bg = icon_green, fg = oxford_blue, command = equal)
decimal_button = tkinter.Button(button_frame, text = ".", font = buttons_font,  bg = yellow_clr, fg = oxford_blue, command= lambda:submit_number("."))
negate_button = tkinter.Button(button_frame, text = "+/-", font = buttons_font, bg = yellow_clr, fg = oxford_blue, command=negate)

nine_button = tkinter.Button(button_frame, text = "9", font=buttons_font, fg = yellow_clr, bg = oxford_blue, command= lambda:submit_number(9))
eight_button = tkinter.Button(button_frame, text = "8", font=buttons_font, fg = yellow_clr, bg = oxford_blue, command= lambda:submit_number(8))
seven_button = tkinter.Button(button_frame, text = "7", font=buttons_font, fg = yellow_clr, bg = oxford_blue, command= lambda:submit_number(7))
six_button = tkinter.Button(button_frame, text = "6", font=buttons_font, fg = yellow_clr, bg = oxford_blue, command= lambda:submit_number(6))
five_button = tkinter.Button(button_frame, text = "5", font=buttons_font, fg = yellow_clr, bg = oxford_blue, command= lambda:submit_number(5))
four_button = tkinter.Button(button_frame, text = "4", font=buttons_font, fg = yellow_clr, bg = oxford_blue, command= lambda:submit_number(4))
three_button = tkinter.Button(button_frame, text = "3", font=buttons_font, fg = yellow_clr, bg = oxford_blue, command= lambda:submit_number(3))
two_button = tkinter.Button(button_frame, text = "2", font=buttons_font, fg = yellow_clr, bg = oxford_blue, command= lambda:submit_number(2))
one_button = tkinter.Button(button_frame, text = "1", font=buttons_font, fg = yellow_clr, bg = oxford_blue, command= lambda:submit_number(1))
zero_button = tkinter.Button(button_frame, text = "0", font=buttons_font, fg = yellow_clr, bg = oxford_blue, command= lambda:submit_number(0))

# First row
clear_button.grid(row=0,column=0, columnspan = 2,sticky = "WE", pady = 1)
quit_button.grid(row=0,column= 2, columnspan = 2,sticky = "WE", pady = 1)

# Second row
inverse_button.grid(row=1,column=0, sticky = "WE", pady = 1)
square_button.grid(row=1,column=1, sticky = "WE", pady = 1)
exponent_button.grid(row=1,column=2,sticky = "WE", pady = 1)
divide_button.grid(row=1,column=3, sticky = "WE", pady = 1)

# Thrid row
seven_button.grid(row=2,column=0, pady = 1, sticky = "WE", ipadx = 20)
eight_button.grid(row=2,column=1, pady = 1, sticky = "WE", ipadx = 20)
nine_button.grid(row=2,column=2, pady = 1, sticky = "WE", ipadx = 20)
multiply_button.grid(row=2,column=3,pady = 1, sticky = "WE" )

# Fourth row
four_button.grid(row=3,column=0, pady = 1, sticky = "WE", ipadx = 20)
five_button.grid(row=3,column=1, pady = 1, sticky = "WE", ipadx = 20)
six_button.grid(row=3,column=2, pady = 1, sticky = "WE", ipadx = 20)
subtract_button.grid(row=3,column=3, pady = 1, sticky = "WE")

# Fifth row
one_button.grid(row=4,column=0, pady = 1, sticky = "WE", ipadx = 20)
two_button.grid(row=4,column=1, pady = 1, sticky = "WE", ipadx = 20)
three_button.grid(row=4,column=2, pady = 1, sticky = "WE", ipadx = 20)
add_button.grid(row=4,column=3,pady = 1, sticky = "WE")

# Sixth
negate_button.grid(row=5,column=0,pady = 1, sticky = "WE", ipadx = 20)
zero_button.grid(row=5,column=1, pady = 1, sticky = "WE", ipadx = 20)
decimal_button.grid(row=5,column=2, pady = 1, sticky = "WE", ipadx = 20)
equal_button.grid(row=5,column=3, pady = 1, sticky = "WE")


# Root main loop
root.mainloop()