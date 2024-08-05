from tkinter import *
import json
from tkinter import messagebox
from PIL import Image, ImageTk
import library
import bcrypt
import base64



def Add():
   
    account_get = Entry.get(account_entry)
    password_get = Entry.get(password_entry)

    if account_get == "" or password_get == "":
        messagebox.showerror(message="表格未完成")
        return

    with open("password.json", "r") as f:
        password_str = f.read()  # 讀取 json 檔案成為 pythob 字串
        if password_str == "":   # 若檔案內容為空則將變數 password_text 設為空字典
            password_text = {}  

        else:  # 若檔案內容非空則將 json 格式字串轉變成 python 字典 
            password_text = json.loads(password_str)  

    with open("password.json", "w") as f:        

        if account_get in password_text:
            messagebox.showerror(message="此帳號已存在")
            account_entry.delete("0", "end")
            password_entry.delete("0", "end")
            return
        else: 
            salt = bcrypt.gensalt()  
            hashed = bcrypt.hashpw(password_get.encode('utf-8'), salt)  # utf-8 將 string (各國語言) 編碼轉成 byte (電腦語言)
            password_text[account_get] = base64.b64encode(hashed).decode('utf-8')  
            # 將密碼用 base64 編碼防止特殊符號問題，在用 utf-8 將 byte 解碼成 string 儲存到字典(salt存在密碼字串中)
            
            print(hashed)
            print(type(hashed))
            print(password_text[account_get] )
            print(type(password_text[account_get]))
            
            json.dump(password_text, f)
            messagebox.showinfo(message="新增完成")        
            account_entry.delete("0", "end")
            password_entry.delete("0", "end")

def Login():    
    try:
        account_get = Entry.get(account_entry)
        password_get = Entry.get(password_entry)
        
        if account_get == "" or password_get == "":
            messagebox.showerror(message="表格未完成")
            return
    
        with open(file="password.json", mode="r") as f:
            password_text = json.loads(f.read()) 
          

        if account_get not in password_text:
            messagebox.showerror(message="此帳號不存在")
            return

        store_hashed = base64.b64decode(password_text[account_get])
        print(store_hashed)
        print(type(store_hashed))
        print(type(password_text[account_get]))
        if bcrypt.checkpw(password_get.encode('utf-8'), store_hashed):  # 比對密碼    
                            
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

        else:
            messagebox.showerror(message="帳號密碼錯誤")
            return
    except:
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