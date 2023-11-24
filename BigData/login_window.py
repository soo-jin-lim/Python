from tkinter import *
import tkinter as tk
import join_window

def check_data():
    if (user_id.get() == "aaa" and password.get() == "aaa",user_id.get() == "bbb" and password.get() == "bbb",
            user_id.get() == "ccc" and password.get() == "ccc"):
        newwin = Tk()
        tk.Label(newwin, text="로그인 성공 " + user_id.get()).grid(row=0, column=0, padx=10, pady=10)
        newwin.mainloop()
        print("로그인 성공")
    else:
        print("다시 시도하세요")
        newwin = Tk()
        tk.Label(newwin, text="다시 시도하세요 ").grid(row=0, column=0, padx=10, pady=10)
        newwin.mainloop()

def open_registration_window():
    registration_window = Tk()
    join_window.registration(registration_window)
    registration_window.mainloop()

window = Tk()

user_id, password = StringVar(), StringVar()

tk.Label(window, text="ID : ").grid(row=0, column=0, padx=10, pady=10)
tk.Label(window, text="Password : ").grid(row=1, column=0, padx=10, pady=10)
tk.Entry(window, textvariable=user_id).grid(row=0, column=1, padx=10, pady=10)
tk.Entry(window, textvariable=password, show='*').grid(row=1, column=1, padx=10, pady=10)
tk.Button(window, text="Login", command=check_data).grid(row=2, column=1, padx=10, pady=10)
tk.Button(window, text="회원가입", command=open_registration_window).grid(row=4, column=2, padx=10, pady=10)

window.mainloop()