from tkinter import *
from PIL import Image, ImageTk
from lib_func import *
from lib_service import *


win_home = Tk()
win_home.geometry("350x400+400+200")
win_home.configure(padx=35, pady=18)
win_home.resizable(False, False)
win_home.title("Welcome")

img1 = Image.open("./fig/book.png")
img1 = img1.resize((150, 150))
img1 = ImageTk.PhotoImage(img1)
img_book1 = Label(win_home, image=img1)
img_book1.grid(column=1, row=0, columnspan=2, pady=25)

account = Label(win_home, text="Account")
account.grid(column=0, row=2, sticky="e")
account_entry = Entry(win_home, width=18)
account_entry.grid(column=1, row=2, columnspan=2, padx=12)

password = Label(win_home, text="Password")
password.grid(column=0, row=3, sticky="e")
password_entry = Entry(win_home, width=18)
password_entry.grid(column=1, row=3, columnspan=2, padx=12, pady=3)

button_add = Button(win_home, text="Add", width=8, command=lambda:Add(account_entry, password_entry ))
button_add.grid(column=2, row=5, pady=5)

button_login = Button(win_home, text="Login", width=8, command=lambda:Login(account_entry, password_entry ))
button_login.grid(column=1, row=5, pady=5)

win_home.mainloop()