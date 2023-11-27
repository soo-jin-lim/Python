import tkinter as tk
from tkinter import ttk
import sqlite3

def show_list():
    def edit_selected():
        # 선택된 행의 정보 가져오기
        selected_item = tree.selection()
        if selected_item:
            item_values = tree.item(selected_item, 'values')
            print("수정할 아이템:", item_values)
            # 여기에 수정 코드 추가

    def delete_selected():
        # 선택된 행의 정보 가져오기
        selected_item = tree.selection()
        if selected_item:
            item_values = tree.item(selected_item, 'values')
            print("삭제할 아이템:", item_values)
            # 여기에 삭제 코드 추가

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

    c.execute("SELECT * FROM users")
    users = c.fetchall()
    for user in users:
        tree.insert("", "end", values=user[1:5])

    tree.pack(padx=10, pady=10)

    # 수정 버튼
    edit_button = tk.Button(list_window, text="수정", command=edit_selected)
    edit_button.pack(side=tk.LEFT, padx=10)

    # 삭제 버튼
    delete_button = tk.Button(list_window, text="삭제", command=delete_selected)
    delete_button.pack(side=tk.LEFT, padx=10)

    list_window.mainloop()
