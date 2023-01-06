# self như this trong java
# Regular method được ngầm gửi vào, chính là đối tượng gọi phương thức và sử dụng self để xử lý
 
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def setAge(self, age):
        if age >= 1:
            self.age = age
        else:
            self.age = 1

    @classmethod
    def createUser(self, name, age):
        if age >= 1:
            return self(name, age)
        else:
            return self(name, 1)
    
    @staticmethod
    def Hello ():
        print("Hello ...!")


VANHIEN = User('Van Hien', 20)
print(VANHIEN.__dict__)

VANHIEN1 = User.createUser('Hiền', -1)
print(VANHIEN1.__dict__)

VANHIEN1.Hello()