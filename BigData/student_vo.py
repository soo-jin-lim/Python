class StudentVO:
    def __init__(self, name, phone, email, user_id, password):
        self.name = name
        self.phone = phone
        self.email = email
        self.user_id = user_id
        self.password = password

    def __str__(self):
        return f"StudentVO(name={self.name}, phone={self.phone}, email={self.email}, user_id={self.user_id}, password={self.password})"
