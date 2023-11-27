import tkinter as tk
from tkinter import StringVar, Toplevel
import join_window
import list_window
import dao_student

dao_student.create_table()


def check_data():
    user_id_val = user_id.get()
    password_val = password.get()

    user = dao_student.get_user_by_id(user_id_val)

    if user and user['password'] == password_val:
        newwin = Toplevel()
        tk.Label(newwin, text=f"로그인 성공 {user_id_val}").grid(row=0, column=0, padx=10, pady=10)
        newwin.mainloop()
        print("로그인 성공")

        list_window.show_list()
    else:
        print("다시 시도하세요")
        newwin = Toplevel()
        tk.Label(newwin, text="다시 시도하세요 ").grid(row=0, column=0, padx=10, pady=10)
        newwin.mainloop()

def open_registration_window():
    registration_window = Toplevel()
    join_window.registration(registration_window)
    registration_window.mainloop()

def show_list():
    list_window.show_list()

window = tk.Tk()

user_id, password = StringVar(), StringVar()

tk.Label(window, text="ID : ").grid(row=0, column=0, padx=10, pady=10)
tk.Label(window, text="Password : ").grid(row=1, column=0, padx=10, pady=10)
tk.Entry(window, textvariable=user_id).grid(row=0, column=1, padx=10, pady=10)
tk.Entry(window, textvariable=password, show='*').grid(row=1, column=1, padx=10, pady=10)
tk.Button(window, text="Login", command=check_data).grid(row=2, column=1, padx=10, pady=10)
tk.Button(window, text="회원가입", command=open_registration_window).grid(row=4, column=2, padx=10, pady=10)
tk.Button(window, text="회원 리스트", command=show_list).grid(row=5, column=2, padx=10, pady=10)

window.mainloop()