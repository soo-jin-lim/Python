import tkinter as tk
from tkinter import ttk


def show_list(member_list):
    list_window = tk.Tk()
    list_window.title("회원 목록")

    tree = ttk.Treeview(list_window, columns=("Name", "Phone Number", "Email", "ID"), show="headings")

    tree.heading("Name", text="이름")
    tree.heading("Phone Number", text="폰번호")
    tree.heading("Email", text="이메일")
    tree.heading("ID", text="아이디")

    for member in member_list:
        tree.insert("", "end", values=member)

    tree.pack(padx=10, pady=10)

    list_window.mainloop()