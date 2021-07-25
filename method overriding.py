
class A:

    def show(self):
        print("Hi from class A")


class B(A):

    def show(self):
        print("Hi from class B")


o1 = A()
o1.show()
o2 = B()
o2.show()
