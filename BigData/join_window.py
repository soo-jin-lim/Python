from tkinter import *
import tkinter as tk

def registration(registration_window):
    name_var, phone_var, email_var, id_var, password_var, confirm_password_var = StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar()

    def validate_input():
        # 입력 필드에서 값 가져오기
        name = name_var.get()
        phone_number = phone_var.get()
        email = email_var.get()
        user_id = id_var.get()
        password = password_var.get()
        confirm_password = confirm_password_var.get()

        # 모든 필드가 채워져 있는지 확인
        if name and phone_number and email and user_id and password and confirm_password:
            if password == confirm_password:
                # 모든 정보가 입력되고 비밀번호도 일치하는 경우
                tk.Label(registration_window, text="회원가입 성공", fg="green").grid(row=8, column=0, columnspan=2, pady=10)
                # 여기에 추가적인 처리를 할 수 있습니다.
            else:
                # 비밀번호가 일치하지 않는 경우
                tk.Label(registration_window, text="비밀번호가 일치하지 않습니다", fg="red").grid(row=8, column=0, columnspan=2, pady=10)
        else:
            # 빈 칸이 있는 경우
            tk.Label(registration_window, text="모든 정보를 다 입력하세요", fg="red").grid(row=8, column=0, columnspan=2, pady=10)

    registration_window.title("회원가입 창")

    tk.Label(registration_window, text="이름 : ").grid(row=1, column=0, padx=10, pady=10)
    tk.Entry(registration_window, textvariable=name_var).grid(row=1, column=1, padx=10, pady=10)

    tk.Label(registration_window, text="폰번호 : ").grid(row=2, column=0, padx=10, pady=10)
    tk.Entry(registration_window, textvariable=phone_var).grid(row=2, column=1, padx=10, pady=10)

    tk.Label(registration_window, text="이메일 : ").grid(row=3, column=0, padx=10, pady=10)
    tk.Entry(registration_window, textvariable=email_var).grid(row=3, column=1, padx=10, pady=10)

    tk.Label(registration_window, text="아이디 : ").grid(row=4, column=0, padx=10, pady=10)
    tk.Entry(registration_window, textvariable=id_var).grid(row=4, column=1, padx=10, pady=10)

    tk.Label(registration_window, text="비밀번호 : ").grid(row=5, column=0, padx=10, pady=10)
    tk.Entry(registration_window, textvariable=password_var, show='*').grid(row=5, column=1, padx=10, pady=10)

    tk.Label(registration_window, text="비밀번호 확인 : ").grid(row=6, column=0, padx=10, pady=10)
    tk.Entry(registration_window, textvariable=confirm_password_var, show='*').grid(row=6, column=1, padx=10, pady=10)

    tk.Button(registration_window, text="가입하기", command=validate_input).grid(row=7, column=0, columnspan=2, pady=10)
    tk.Button(registration_window, text="최소").grid(row=8, column=0, columnspan=2, pady=10)

window = Tk()

tk.Label(window, text="ID : ").grid(row=0, column=0, padx=10, pady=10)
tk.Label(window, text="Password : ").grid(row=1, column=0, padx=10, pady=10)
tk.Entry(window).grid(row=0, column=1, padx=10, pady=10)
tk.Entry(window, show='*').grid(row=1, column=1, padx=10, pady=10)
tk.Button(window, text="Login").grid(row=2, column=1, padx=10, pady=10)
tk.Button(window, text="회원가입", command=lambda: registration(Toplevel())).grid(row=4, column=2, padx=10, pady=10)

window.mainloop()
