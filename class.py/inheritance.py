class dad:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)

class son(dad):
    def __init__(self,name,age,degree):
        self.degree = degree
        dad().__init__(name,age)  

    def display(self):
        print(self.name, self.age, self.degree)
    obj1 = dad("Muhammed", 14)    
    obj1.display()
    obj2 = son("Muhammed", 14, "B.E")
    obj2.display()