class UserInfo:
    def __init__(self, name, age, year, email):
        self.name = name
        self.age = age
        self.year = year
        self.email = email
        self.info = ""

    def __str__(self):
        return f"UserInfo(name={self.name}, age={self.age}, year={self.year}, email={self.email})"    

    def set_info(self, info):
        self.info = info

    def get_info(self):
        return self.info
