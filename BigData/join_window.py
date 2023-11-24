from tkinter import *
import tkinter as tk

def registration(registration_window):
    def validate_input():
        # Entry 위젯에서 값을 가져옴
        user_id = user_id_var.get()
        password = password_var.get()
        confirm_password = confirm_password_var.get()
        name = name_var.get()
        phone_number = phone_number_var.get()
        email = email_var.get()

        # 모든 필드가 비어 있지 않고 비밀번호가 일치할 때
        if all([user_id_var, password_var, confirm_password_var, name_var, phone_number_var, email_var]) and password_var == confirm_password_var:
            # 성공 메시지 표시
            success_label.config(text="가입 성공", fg="green")
            # 여기에 데이터베이스에 가입 정보를 저장하거나 다른 동작을 수행하는 코드를 삽입할 수 있습니다.
        else:
            # 실패 메시지 표시
            if not all([user_id, password, confirm_password, name, phone_number, email]):
                success_label.config(text="모든 정보를 다 입력하세요", fg="red")
            else:
                success_label.config(text="비밀번호가 일치하지 않습니다", fg="red")

    registration_window.title("회원가입 창")

    # Entry 위젯의 값을 저장할 변수들
    user_id_var, password_var, confirm_password_var = StringVar(), StringVar(), StringVar()
    name_var, phone_number_var, email_var = StringVar(), StringVar(), StringVar()

    tk.Label(registration_window, text="아이디 : ").grid(row=1, column=0, padx=10, pady=10)
    tk.Entry(registration_window, textvariable=user_id_var).grid(row=1, column=1, padx=10, pady=10)

    tk.Label(registration_window, text="비밀번호 : ").grid(row=2, column=0, padx=10, pady=10)
    tk.Entry(registration_window, show='*', textvariable=password_var).grid(row=2, column=1, padx=10, pady=10)

    tk.Label(registration_window, text="비밀번호 확인 : ").grid(row=3, column=0, padx=10, pady=10)
    tk.Entry(registration_window, show='*', textvariable=confirm_password_var).grid(row=3, column=1, padx=10, pady=10)

    tk.Label(registration_window, text="이름 : ").grid(row=4, column=0, padx=10, pady=10)
    tk.Entry(registration_window, textvariable=name_var).grid(row=4, column=1, padx=10, pady=10)

    tk.Label(registration_window, text="폰번호 : ").grid(row=5, column=0, padx=10, pady=10)
    tk.Entry(registration_window, textvariable=phone_number_var).grid(row=5, column=1, padx=10, pady=10)

    tk.Label(registration_window, text="이메일 : ").grid(row=6, column=0, padx=10, pady=10)
    tk.Entry(registration_window, textvariable=email_var).grid(row=6, column=1, padx=10, pady=10)

    # 가입 검증을 실행할 버튼
    tk.Button(registration_window, text="가입하기", command=validate_input).grid(row=7, column=1, padx=10, pady=10)

    # 성공 또는 에러 메시지를 표시할 라벨
    success_label = tk.Label(registration_window, text="", fg="green")
    success_label.grid(row=8, column=0, columnspan=2, pady=10)

if __name__ == "__main__":
    window = Tk()

    tk.Label(window, text="ID : ").grid(row=0, column=0, padx=10, pady=10)
    tk.Label(window, text="Password : ").grid(row=1, column=0, padx=10, pady=10)
    tk.Entry(window).grid(row=0, column=1, padx=10, pady=10, textvariable=StringVar())
    tk.Entry(window, show='*').grid(row=1, column=1, padx=10, pady=10, textvariable=StringVar())
    tk.Button(window, text="Login", command=lambda: print("로그인 성공" if all([widget.get() for widget in (entry1, entry2)]) else "로그인 실패")).grid(row=2, column=1, padx=10, pady=10)
    tk.Button(window, text="회원가입", command=lambda: registration(Toplevel())).grid(row=4, column=2, padx=10, pady=10)

    window.mainloop()
