class Student:
    def __init__(self,rno,name):
        self.rno=rno
        self.name=name
    def setAge(self):
        self.age = int(input("Enter age:"))
    def setMarks(self):
        self.marks = int(input("Enter marks:"))
    def display(self):
        print("Roll no. is:",self.rno)
        print("Name is:",self.name)
        print("Age is:",self.age)
        print("Marks is:",self.marks)

s1 = Student(10,"John")
s1.setAge()
s1.setMarks()
s1.display()
s2 = Student(12,"Jacob")
s2.setAge()
s2.setMarks()
s2.display()
