import tkinter as tk
from tkinter import StringVar
import dao_student

def registration(registration_window):
    name_var, phone_var, email_var, id_var, password_var, confirm_password_var = StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar()

    def validate_input():
        name = name_var.get()
        phone_number = phone_var.get()
        email = email_var.get()
        user_id = id_var.get()
        password = password_var.get()
        confirm_password = confirm_password_var.get()

        if name and phone_number and email and user_id and password and confirm_password:
            if password == confirm_password:
                # 유효성 검사 통과 시 사용자 정보를 추가
                new_user = {'name': name, 'phone': phone_number, 'email': email, 'user_id': user_id, 'password': password}
                dao_student.add_user(new_user)
                tk.Label(registration_window, text="회원가입 성공", fg="green").grid(row=8, column=0, columnspan=2, pady=10)
            else:
                tk.Label(registration_window, text="비밀번호가 일치하지 않습니다", fg="red").grid(row=8, column=0, columnspan=2, pady=10)
        else:
            tk.Label(registration_window, text="모든 정보를 다 입력하세요", fg="red").grid(row=8, column=0, columnspan=2, pady=10)

    def close_window():
        registration_window.destroy()

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
    tk.Button(registration_window, text="닫기", command=close_window).grid(row=7, column=1, columnspan=2, pady=10)
