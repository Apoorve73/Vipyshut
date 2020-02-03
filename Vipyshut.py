import tkinter
from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("200x200")
def hello():
   messagebox.showinfo("Say Hello", "Hello World")
   hello()
B1 = Button(root, text = "Say Hello", command = hello,activebackground="green",font="Arial",height="1",justify="left")
B1.invoke()
B2=Button(root,text="Ready", fg= 'red',activeforeground="blue",bd="5",bg="black")
B2.place(x=35,y=150)
B3=Button(root,text="Go",relief="ridge",state="disabled")
B3.pack()

B1.place(x=15,y=35)
root.mainloop()
