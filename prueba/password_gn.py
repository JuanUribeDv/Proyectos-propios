import random as rd
import string 
import tkinter as tk 
from tkinter import messagebox
#3
root= tk.Tk()
root.geometry("400x400")
root.title("Password generator")

password=''
length=12

def generate(length):
    global password
    password = string.ascii_letters + string.digits + string.punctuation
    label1.config(text='A value has been created')
    password= ''.join(rd.choice(password) for _ in range(length))
    return password
def show_password():
        messagebox.showinfo("verification",f'{password}')

def delete_password():
    global password
    if password=='':
         messagebox.showinfo("Title",'The password has been already deleted')
    else:
        password=None
        messagebox.showinfo("Title",'The password has been deleted succesfully')
        label1.config(text="There'isnt any value yet")

label1=tk.Label(text="There'isnt any value yet")
label1.grid(row=1, column=1)

btn1=tk.Button(text='Generate', command=lambda: generate(length))
btn1.grid(row=2, column=0)

btn2=tk.Button(text='Show',command=show_password)
btn2.grid(row=2, column=1)

btn3=tk.Button(text='Delete',command=delete_password)
btn3.grid(row=2, column=2)


for i in range(3):
    root.grid_rowconfigure(i, weight=1)
    for j in range(3):
        root.grid_columnconfigure(j, weight=1)





root.mainloop()
