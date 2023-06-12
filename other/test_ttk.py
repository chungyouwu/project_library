import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.title('Library')
root.configure(bg="#D0D0D0")
root.geometry('500x100')

Nov={"國慶日":"10/10"}
Dec={"聖誕節":"12/25"}
Jen={"元旦":"1/1"}
Mar={"生日":"3/29"}
Apr={"愚人節":"4/1","兒童節":"4/4"}

tree=ttk.Treeview(root, columns=("books"))

yscrollbar=tk.Scrollbar(root)  #卷軸
yscrollbar.pack(side="right",fill='y')
yscrollbar.config(command=tree.yview)
tree.configure(yscrollcommand=yscrollbar.set)

for i in range(4):
    tree.column(ac[i],width=70,anchor='e')
    tree.heading(ac[i],text=area[i])
tree.pack()
for i in range(3):
    tree.insert('','end',values=data[i])

# tree.heading ("#0",text="題名")
# tree.heading ("#1",text="作者")


tree.insert("", index="end", text="123")

# idNov = tree.insert("", index="end", text="Nov")
# idDec = tree.insert("", index="end", text="Dec")
# idJen = tree.insert("", index="end", text="Jen")
# idMar = tree.insert("", index="end", text="Mar")
# idApr = tree.insert("", index="end", text="Apr")

# for festival in Nov.keys():
#     tree.insert(idNov, index="end", text=festival, values=Nov[festival])
# for festival in Dec.keys():
#     tree.insert(idDec, index="end", text=festival, values=Dec[festival])
# for festival in Jen.keys():
#     tree.insert(idJen, index="end", text=festival, values=Jen[festival])
# for festival in Mar.keys():
#     tree.insert(idMar, index="end", text=festival, values=Mar[festival])
# for festival in Apr.keys():
#     tree.insert(idApr, index="end", text=festival, values=Apr[festival])

tree.pack()
root.mainloop()