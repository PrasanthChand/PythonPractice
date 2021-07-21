# inheritance


# parent class
class A:
    def feature1(self):
        print("feature 1 from A")


# child class - single level inheritance
class B(A):
    def feature2(self):
        print("feature 2 from B")


# child class - multi level inheritance
class C(B):
    def feature3(self):
        print("feature 3 from C")


class D:
    def feature4(self):
        print("feature 4 from D")


# multiple inheritance
class E(A, D):
    def feature5(self):
        print("feature 5 from E")


a1 = A()
b1 = B()
c1 = C()
d1 = D()
e1 = E()

a1.feature1()
b1.feature2()
b1.feature1()
c1.feature3()
d1.feature4()
e1.feature1()
e1.feature4()




