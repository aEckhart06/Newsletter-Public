class UserInfo:
    def __init__(self, name: str, interest: str, email: str =""):
        self.name = name
        self.email = email
        self.interest = interest

    def __str__(self):
        return f"UserInfo(name={self.name}, email={self.email})"    
    
    def get_interest(self):
        return self.interest
