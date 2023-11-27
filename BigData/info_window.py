import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

def show_info_window(selected_user):
    info_window = tk.Tk()
    info_window.title("사용자 정보 수정 및 삭제")

    tk.Label(info_window, text="이름:").grid(row=0, column=0, padx=10, pady=10)
    tk.Label(info_window, text="폰번호:").grid(row=1, column=0, padx=10, pady=10)
    tk.Label(info_window, text="이메일:").grid(row=2, column=0, padx=10, pady=10)
    tk.Label(info_window, text="아이디:").grid(row=3, column=0, padx=10, pady=10)

    name_var, phone_var, email_var, id_var = tk.StringVar(value=selected_user[1]), tk.StringVar(value=selected_user[2]), tk.StringVar(value=selected_user[3]), tk.StringVar(value=selected_user[4])

    name_entry = tk.Entry(info_window, textvariable=name_var)
    phone_entry = tk.Entry(info_window, textvariable=phone_var)
    email_entry = tk.Entry(info_window, textvariable=email_var)
    id_entry = tk.Entry(info_window, textvariable=id_var)  # 아이디도 수정 가능으로 변경

    name_entry.grid(row=0, column=1, padx=10, pady=10)
    phone_entry.grid(row=1, column=1, padx=10, pady=10)
    email_entry.grid(row=2, column=1, padx=10, pady=10)
    id_entry.grid(row=3, column=1, padx=10, pady=10)

    def update_user():
        conn = sqlite3.connect('user_database.db')
        c = conn.cursor()

        updated_name = name_var.get()
        updated_phone = phone_var.get()
        updated_email = email_var.get()

        c.execute('''
            UPDATE users
            SET name=?, phone=?, email=?
            WHERE id=?
        ''', (updated_name, updated_phone, updated_email, selected_user[0]))

        conn.commit()
        conn.close()

        messagebox.showinfo("성공", "사용자 정보가 업데이트되었습니다.")
        info_window.destroy()

    def delete_user():
        conn = sqlite3.connect('user_database.db')
        c = conn.cursor()

        c.execute('DELETE FROM users WHERE id=?', (selected_user[0],))

        conn.commit()
        conn.close()

        messagebox.showinfo("성공", "사용자 정보가 삭제되었습니다.")
        info_window.destroy()

    tk.Button(info_window, text="수정하기", command=update_user).grid(row=4, column=0, columnspan=2, pady=10)
    tk.Button(info_window, text="삭제하기", command=delete_user).grid(row=5, column=0, columnspan=2, pady=10)

    info_window.mainloop()

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

    c.execute("SELECT * FROM users")
    users = c.fetchall()
    for user in users:
        tree.insert("", "end", values=user[1:5])

    tree.pack(padx=10, pady=10)

    # 수정 버튼
    edit_button = tk.Button(list_window, text="수정", command=lambda: show_info_window(tree.item(tree.selection(), 'values')))
    edit_button.pack(side=tk.LEFT, padx=10)

    # 삭제 버튼
    delete_button = tk.Button(list_window, text="삭제", command=lambda: show_info_window(tree.item(tree.selection(), 'values')))
    delete_button.pack(side=tk.LEFT, padx=10)

    list_window.mainloop()

# show_list 함수 호출
show_list()
