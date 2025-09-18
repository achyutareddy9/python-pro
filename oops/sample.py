#single responsibility Paradigm

class EmailService:

    def send_email(self, user):
        return f"Welcome to Python world {user.name}"

class User:

    def __init__(self,name,email):
        self.name = name
        self.email = email


class UserService:

    def register(self):
        pass


user = User("achyuta", "achyuta.ai@outlook.com")
mail = EmailService()
print(mail.send_email(user))