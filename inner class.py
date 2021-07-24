# Outer class
class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.laptop = self.Laptop()

    def show(self):
        print("Name : ", self.name, " - Roll No: ", self.rollno)
        self.laptop.show()

# Inner class
    class Laptop:

        def __init__(self):
            self.brand = "Dell"
            self.ram = "8 GB"

        def show(self):
            print("Laptop configurations are ", self.brand, self.ram, "\n")


s1 = Student('Mike', 12323)
s2 = Student('Sam', 33420)

s1.show()
s2.show()


