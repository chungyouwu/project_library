from tkinter import *
from tkinter import ttk
import pandas



def Collection():

    lib_win = Toplevel()
    lib_win.title("Library")
    lib_win.geometry("1200x700+100+100")

    # add some style
    style = ttk.Style()
    # pick a theme
    style.theme_use("default")

    # configure the treeview colors
    style.configure("Treeview",
    background="#BEBEBE",
    foreground="black",
    rowheight=30,
    fieldbackground="#BEBEBE")

    # change selected color
    style.map("Treeview", background=[("selected", "#FFAD86")]) #347083

    # creat a treeview fram
    tree_frame = Frame(lib_win)
    tree_frame.pack(pady=10)

    #creat a treeview scrollbar
    tree_scroll = Scrollbar(tree_frame)    # scrollbar 放到 frame
    tree_scrollx = Scrollbar(tree_frame, orient=HORIZONTAL) # x軸的 scrollbar 要呈水平方向
    tree_scroll.pack(side=RIGHT, fill=Y)   # 垂直填滿
    tree_scrollx.pack(side=BOTTOM, fill=X) # 水平填滿

    # creat the treeview  ( treeview 放到 frame
    my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, xscrollcommand=tree_scrollx.set, selectmode="extended",height=20) # 顯示20筆
    my_tree.pack()

    # configuare the scrollbar
    tree_scroll.config(command=my_tree.yview)  # 設定 scrollbar 綁定 treeview 的 y 軸
    tree_scrollx.config(command=my_tree.xview)

    # define our columns
    items =  ("題名", "作者_創建者", "所屬期刊", "主題", "識別號", "叢書", "學位論文", "類型", "摘要", "內容", "其他題名", "相關題名", "版本", "出版者", "建立日期", "附註", "得獎註", "適用對象_影視分級", "語文註", "格式", "刊期", "醫學主題", "政府出版品主題", "合訂", "課程資訊", "架號", "權利聲明", "資源來源", "永久連結")
    my_tree["columns"] = items

    # format our columns
    def columns_formate(item):
        my_tree.column(item, anchor=CENTER, width=200)


    my_tree.column("#0", width=0, stretch=NO)
    for item in items:
        columns_formate(item)

    # create headings
    def headings_create(item):
        my_tree.heading(item, text=item, anchor=CENTER)

    my_tree.heading("#0", text="", anchor=CENTER)
    for item in items:
        headings_create(item)

    # data
    library_df = pandas.read_excel("./data/library_data.xlsx")

    # creat striped row tags
    my_tree.tag_configure("oddrow", background="white")
    my_tree.tag_configure("evenrow", background="lightblue")

    # add our data
    # global count
    count = 0

    for record in library_df.values.tolist():
        if count % 2 == 0:        
            my_tree.insert(parent="", index="end", iid=count, text="", values=(record[0:28]), tags=("evenrow"))
        else:
            my_tree.insert(parent="", index="end", iid=count, text="", values=(record[0:28]), tags=("oddrow"))
        count += 1




    lib_win.mainloop()