# https://www.youtube.com/watch?v=zg4c92pNFeo&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=9
import pandas
import sqlite3


df = pandas.read_excel("library_data.xlsx")

conn = sqlite3.connect('library_data.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE if not exists library_data(
               題名, 作者_創建者, 所屬期刊, 主題, 識別號, 叢書, 學位論文, 類型, 摘要, 內容, 其他題名, 相關題名, 版本, 出版者, 建立日期, 附註, 得獎註, 適用對象_影視分級, 語文註, 格式, 刊期, 醫學主題, 政府出版品主題, 合訂, 課程資訊, 架號, 權利聲明, 資源來源, 永久連結)
               ''')
conn.commit()
df.to_sql('library_data', conn, if_exists='append', index=False)
conn.close()
# 1.connect()-同時建立資料庫與連線
# 2.cursor()-建立資料庫操作指標
# 3.execute()-執行新增資料表的SQL指令
# 4.commit()-確認完成
