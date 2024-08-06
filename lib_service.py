from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import lib_collection

def service():
    win_login = Toplevel()
    win_login.geometry("350x400+500+300")
    win_login.configure(padx=80, pady=40)
    win_login.resizable(False, False)
    win_login.title("Library")

    img2 = Image.open("./fig/books.png")
    img2 = img2.resize((100, 100))
    img2 = ImageTk.PhotoImage(img2)
    img_book2 = Label(win_login, image=img2)
    img_book2.grid(column=0, row=0, columnspan=2, pady=25)

    button_record = Button(win_login, text="Record", width=8, command=lambda: messagebox.showinfo(message="未建立"))
    button_record.grid(column=1, row=1, padx=10, pady=5)

    button_collection = Button(win_login, text="Collection", width=8, command=lambda: lib_collection.Collection())
    button_collection.grid(column=0, row=1, padx=10, pady=5)

    button_checkout = Button(win_login, text="Checkout", width=8, command=lambda: messagebox.showinfo(message="未建立")) # 借書
    button_checkout.grid(column=0, row=2, padx=10, pady=5)

    button_checkin = Button(win_login, text="Return", width=8, command=lambda: messagebox.showinfo(message="未建立")) # 還書
    button_checkin.grid(column=1, row=2, padx=10, pady=5)

    win_login.mainloop()