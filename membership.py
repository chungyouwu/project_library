from tkinter import *
import json
from tkinter import messagebox
from PIL import Image, ImageTk
import library
import bcrypt




def Add():
   
    account_get = Entry.get(account_entry)
    password_get = Entry.get(password_entry)
    with open("password.json", "r") as f:
        password_str = f.read()
        if password_str == "":
            password_text = {}


        else:
            password_text = json.loads(password_str)  
            if account_get == "" or password_get == "":
                messagebox.showerror(message="表格未完成")
                return

            elif account_get in password_text:
                messagebox.showerror(message="此帳號已存在")

                account_entry.delete("0", "end")
                password_entry.delete("0", "end")
                return

    with open("password.json", "w") as f:
        # 加密版本
        salt = bcrypt.gensalt()  # 加鹽
        hashed = bcrypt.hashpw(password_get.encode('utf-8'), salt)
        password_text[account_get] = str(hashed)
        #password_text[account_get] = str(password_get) 不加密版本
        
        json.dump(password_text, f)
        messagebox.showinfo(message="新增完成")        
        account_entry.delete("0", "end")
        password_entry.delete("0", "end")

def Login():    
    account_get = Entry.get(account_entry)
    password_get = Entry.get(password_entry)

    with open(file="password.json", mode="r") as f:

        password_text = json.loads(f.read())

        
        salt = bcrypt.gensalt()  # 加鹽
        hashed = bcrypt.hashpw(password_get.encode('utf-8'), salt)
        password_text[account_get] = str(hashed)
        
        if account_get == "" or password_get == "":
            messagebox.showerror(message="表格未完成")
            return
        elif account_get not in password_text:
            messagebox.showerror(message="此帳號不存在")
            return

        # elif account_get in password_text and password_get == password_text[account_get]:
        elif account_get in password_text and bcrypt.checkpw(password_get.encode('utf-8'), hashed):   # 解碼     
                            

            win_login = Toplevel()
            win_login.geometry("350x400+500+300")
            win_login.configure(padx=80, pady=40)
            win_login.resizable(False, False)
            win_login.title("Library")

            img2 = Image.open("books.png")
            img2 = img2.resize((100, 100))
            img2 = ImageTk.PhotoImage(img2)
            img_book2 = Label(win_login, image=img2)
            img_book2.grid(column=0, row=0, columnspan=2, pady=25)

            button_record = Button(win_login, text="Record", width=8, command=lambda: messagebox.showinfo(message="未建立"))
            button_record.grid(column=1, row=1, padx=10, pady=5)

            button_collection = Button(win_login, text="Collection", width=8, command=lambda: library.Collection())
            button_collection.grid(column=0, row=1, padx=10, pady=5)

            button_checkout = Button(win_login, text="Checkout", width=8, command=lambda: messagebox.showinfo(message="未建立")) # 借書
            button_checkout.grid(column=0, row=2, padx=10, pady=5)

            button_checkin = Button(win_login, text="Checkin", width=8, command=lambda: messagebox.showinfo(message="未建立")) # 還書
            button_checkin.grid(column=1, row=2, padx=10, pady=5)

            win_login.mainloop()

        elif account_get in password_text and password_get != password_text[account_get]:
            messagebox.showerror(message="帳號密碼錯誤")
            return
        else:
            messagebox.showerror(message="不明錯誤")
     


win_home = Tk()
win_home.geometry("350x400+400+200")
win_home.configure(padx=35, pady=18)
win_home.resizable(False, False)
win_home.title("Welcome")

img1 = Image.open("book.png")
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

button_add = Button(win_home, text="Add", width=8, command=Add)
button_add.grid(column=2, row=5, pady=5)

button_login = Button(win_home, text="Login", width=8, command=Login)
button_login.grid(column=1, row=5, pady=5)



win_home.mainloop()