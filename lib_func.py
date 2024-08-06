
from tkinter import messagebox
from tkinter import *
from lib_service import service
import json
import base64
import bcrypt




def Add(account_entry, password_entry):
   
    account_get = Entry.get(account_entry)
    password_get = Entry.get(password_entry)

    if account_get == "" or password_get == "":
        messagebox.showerror(message="表格未完成")
        return

    with open("./data/password.json", "r") as f:
        password_str = f.read()  # 讀取 json 檔案成為 pythob 字串
        if password_str == "":   # 若檔案內容為空則將變數 password_text 設為空字典
            password_text = {}  

        else:  # 若檔案內容非空則將 json 格式字串轉變成 python 字典 
            password_text = json.loads(password_str)  

    with open("./data/password.json", "w") as f:        

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

            print(type(hashed))
            print(type(password_text[account_get]))
            
            json.dump(password_text, f)
            messagebox.showinfo(message="新增完成")        
            account_entry.delete("0", "end")
            password_entry.delete("0", "end")




def Login(account_entry, password_entry):    
    try:
        account_get = Entry.get(account_entry)
        password_get = Entry.get(password_entry)
        
        if account_get == "" or password_get == "":
            messagebox.showerror(message="表格未完成")
            return
    
        with open(file="./data/password.json", mode="r") as f:
            password_text = json.loads(f.read()) 
          

        if account_get not in password_text:
            messagebox.showerror(message="此帳號不存在")
            return

        store_hashed = base64.b64decode(password_text[account_get])

        print(type(store_hashed))
        print(type(password_text[account_get]))

        if bcrypt.checkpw(password_get.encode('utf-8'), store_hashed):  # 比對密碼    
            service()                      


        else:
            messagebox.showerror(message="帳號密碼錯誤")
            return
    except:
        messagebox.showerror(message="不明錯誤")