import tkinter as tk
from tkinter import messagebox 
import random as rd
#3
#PARTE DEL MENÚ
menu=tk.Tk()
menu.geometry("400x400")
menu.title("TOOLBOX")


def ColorChange():
    colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'pink']
    new_color = rd.choice(colors)
    menu.config(bg=new_color)

def calculator():
    menu.destroy()
    calc=tk.Tk()
    calc.geometry("400x400")
    calc.title("calculadora")
    

    def suma():
        try:
            a = int(entry_value1.get())
            b = int(entry_value2.get())
            result = a + b
            label_result.config(text=f"Result: {result}")
        except ValueError:
            messagebox.showerror("Error", "please, select correct values")

    def Resta():
        try:
            a = int(entry_value1.get())
            b = int(entry_value2.get())
            result = a - b
            label_result.config(text=f"Result: {result}")
        except ValueError:
            messagebox.showerror("Error", "please, select correct values")

    def Multiplication():
        try:
            a = int(entry_value1.get())
            b = int(entry_value2.get())
            result = a * b
            label_result.config(text=f"Result: {result}")
        except ValueError:
            messagebox.showerror("Error", "please, select correct values")
    def Divition():
        try:
            a = int(entry_value1.get())
            b = int(entry_value2.get())
            result = a / b
            label_result.config(text=f"Result: {result}")
        except ValueError:
            messagebox.showerror("Error", "please, select correct values")

    #def back_menu():
       # calc.destroy()

 
    label_value1=tk.Label(text="Insert the firts value")
    label_value1.grid(row=0, column=0)
    entry_value1=tk.Entry(calc)
    entry_value1.grid(row=1,column=0)
    label_value2=tk.Label(text="Insert the second value")
    label_value2.grid(row=0, column=2)
    entry_value2=tk.Entry(calc)
    entry_value2.grid(row=1,column=2)
    label_result=tk.Label(text="Result")
    label_result.grid(row=0, column=1)
    #frame_button = tk.Frame(calc)
    #frame_button.grid(row=2, column=1)
    btn_sum=tk.Button(text="Suma", command=suma)
    btn_sum.grid(row=2,column=0)
    btn_Resta=tk.Button(text="Resta", command=Resta)
    btn_Resta.grid(row=2,column=1)
    btn_Multiplication=tk.Button(text="Multiplication", command=Multiplication)
    btn_Multiplication.grid(row=2,column=2)
    btn_Divition=tk.Button(text="Divition", command=Divition)
    btn_Divition.grid(row=1,column=1)


    for i in range(3):
        calc.grid_rowconfigure(i, weight=1)
    for j in range(3):
        calc.grid_columnconfigure(j, weight=1)

"""def Click_counter():
    calc.destroy()
    click=tk.Tk()
    click.geometry("400x400")
    click.title("Click counter")"""


btn_calc=tk.Button(text="Calculator", command=calculator)
btn_calc.grid(row=2, column=0)
btn_Click_counter=tk.Button(text="Click counter")
btn_Click_counter.grid(row=2, column=1)
btn_converter=tk.Button(text="United converter")
btn_converter.grid(row=2, column=2)
btn_color=tk.Button(text="New color", command=ColorChange)
btn_color.grid(row=0, column=1)
labelmenu=tk.Label(text="WELCOME TO THE TOOLBOX!")
labelmenu.grid(row=1,column=1)




for i in range(3):
    menu.grid_rowconfigure(i, weight=1)
    for j in range(3):
        menu.grid_columnconfigure(j, weight=1)



menu.mainloop()