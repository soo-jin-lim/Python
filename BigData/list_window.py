import tkinter as tk
from tkinter import ttk
import sqlite3

def show_list():
    conn = sqlite3.connect('user_database.db')
    c = conn.cursor()

    list_window = tk.Tk()
    list_window.title("회원 리스트")

    # TreeView 생성
    tree = ttk.Treeview(list_window)
    tree["columns"] = ("이름", "폰번호", "이메일", "아이디")
    tree.heading("#0", text="이름")
    tree.heading("이름", text="이름")
    tree.heading("폰번호", text="폰번호")
    tree.heading("이메일", text="이메일")
    tree.heading("아이디", text="아이디")

    # 데이터베이스에서 회원 데이터를 검색하고 TreeView에 삽입
    c.execute("SELECT * FROM users")
    users = c.fetchall()
    for user in users:
        tree.insert("", "end", values=user[1:5])  # Adjusted to display only name, phone, email, and user_id

    tree.pack(padx=10, pady=10)
    list_window.mainloop()

# Uncomment the following line if you want to test the function independently
# show_list()
