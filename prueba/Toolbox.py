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
    menu.withdraw()
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
    def Division():
        try:
            a = int(entry_value1.get())
            b = int(entry_value2.get())
            result = a / b
            label_result.config(text=f"Result: {result}")
        except ValueError:
            messagebox.showerror("Error", "please, select correct values")
    def returnmenu():
        calc.destroy()
        menu.deiconify()

    label_value1=tk.Label(calc, text="Insert the firts value")
    label_value1.grid(row=0, column=0)
    entry_value1=tk.Entry(calc)
    entry_value1.grid(row=1,column=0)
    label_value2=tk.Label(calc,text="Insert the second value")
    label_value2.grid(row=0, column=2)
    entry_value2=tk.Entry(calc)
    entry_value2.grid(row=1,column=2)
    label_result=tk.Label(calc,text="Result")
    label_result.grid(row=0, column=1)
    #frame_button = tk.Frame(calc)
    #frame_button.grid(row=2, column=1)
    btn_sum=tk.Button(calc,text="Suma", command=suma)
    btn_sum.grid(row=2,column=0)
    btn_Resta=tk.Button(calc,text="Resta", command=Resta)
    btn_Resta.grid(row=2,column=1)
    btn_Multiplication=tk.Button(calc,text="Multiplication", command=Multiplication)
    btn_Multiplication.grid(row=2,column=2)
    btn_Divition=tk.Button(calc,text="Divition", command=Division)
    btn_Divition.grid(row=1,column=1)
    btn_backmenu=tk.Button(calc,text="Return to the menu", command=returnmenu)
    btn_backmenu.grid(padx=10, pady=10)

    for i in range(3):
        calc.grid_rowconfigure(i, weight=1)
    for j in range(3):
        calc.grid_columnconfigure(j, weight=1)

def Click_counter():
    global count
    menu.withdraw()
    click=tk.Tk()
    click.geometry("400x400")
    click.title("Click counter")
    count=0
    def counter():
        global count
        count += 1
        label_count.config(text=f"Clicks: {count}")
    def returnmenu2():
        click.destroy()
        menu.deiconify()

    label_count=tk.Label(click,text="Clicks")
    label_count.grid(row=1, column=1)
    btn_click=tk.Button(click,text="Click here", command=counter)
    btn_click.grid(row=2,column=1)
    btn_returnmenu2=tk.Button(click,text="Return to the menu", command=returnmenu2)
    btn_returnmenu2.grid(row=0, column=1)

    for i in range(3):
        click.grid_rowconfigure(i, weight=1)
    for j in range(3):
        click.grid_columnconfigure(j, weight=1)
def united_converted():
    menu.withdraw()
    converter=tk.Tk()
    converter.geometry("400x400")
    converter.title("United converter")
    
    def convert():

        return 

    def backmenu3():
        converter.destroy()
        menu.deiconify()

    label_value=tk.Label(converter, text="Insert the value to convert")
    label_value.grid(row=0, column=0)
    entry_value=tk.Entry(converter)
    entry_value.grid(row=1, column=0)
    label_result2=tk.Label(converter, text="Result")
    label_result2.grid(row=1, column=1)
    btn_convert=tk.Button(converter, text="Convert", command=convert)
    btn_convert.grid(row=2, column=0)
    btn_backmenu3=tk.Button(converter, text="Return to the menu", command=backmenu3)
    btn_backmenu3.grid(row=2,column=1)
    for i in range(3):
        converter.grid_rowconfigure(i, weight=1)
    for j in range(3):
        converter.grid_columnconfigure(j, weight=1)
def letter_counter():
    menu.withdraw()
    lcounter=tk.Tk()
    lcounter.geometry("400x400")
    lcounter.title("Letter counter")

    def count ():
        count=len(str(entry_word.get()))
        labelcount.config(text=f"This word has {count} letters")

    def backmenu4():
        lcounter.destroy()
        menu.deiconify()
    btn_backmenu4=tk.Button(lcounter, text="back to the menu", command= backmenu4)
    btn_backmenu4.grid(row=2, column=0)
    btn_count=tk.Button(lcounter,text="counter", command= count)
    btn_count.grid(row=1, column=1)
    entry_word =tk.Entry(lcounter)
    entry_word.grid(row=0, column=1)
    labelcount=tk.Label(lcounter,text="There is not a word yet")
    labelcount.grid(row=2, column=1)

    for i in range(3):
        lcounter.grid_rowconfigure(i, weight=1)
    for j in range(3):
        lcounter.grid_columnconfigure(j, weight=1)
    
btn_letter_counter=tk.Button(text="Letter counter", command=letter_counter)
btn_letter_counter.grid(row=2, column=2)
btn_calc=tk.Button(text="Calculator", command=calculator)
btn_calc.grid(row=2, column=0)
btn_Click_counter=tk.Button(text="Click counter", command=Click_counter)
btn_Click_counter.grid(row=2, column=1)
#btn_converter=tk.Button(text="United converter", command=united_converted)
#btn_converter.grid(row=2, column=2)
btn_color=tk.Button(text="New color", command=ColorChange)
btn_color.grid(row=0, column=1)
labelmenu=tk.Label(text="WELCOME TO THE TOOLBOX!")
labelmenu.grid(row=1,column=1)




for i in range(3):
    menu.grid_rowconfigure(i, weight=1)
    for j in range(3):
        menu.grid_columnconfigure(j, weight=1)



menu.mainloop()