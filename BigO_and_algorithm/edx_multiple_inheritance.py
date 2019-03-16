class A(object):
    def __init__(self):
        self.a = 1
    def x(self):
        print("A.x")
    def y(self):
        print("A.y")
    def z(self):
        print("A.z")

class B(A):
    def __init__(self):
        A.__init__(self)
        self.a = 2
        self.b = 3
    def y(self):
        print("B.y")
    def z(self):
        print("B.z")

class C:
    def __init__(self):
        self.a = 4
        self.c = 5
    def y(self):
        print("C.y")
    def z(self):
        print("C.z")

class D(C, B):
    def __init__(self):
        C.__init__(self)
        B.__init__(self)
        self.d = 6
    def z(self):
        print("D.z")

# Python first searches the object's instance variables
# then uses a simple left-to-right, depth first search 
# through the class hierarchy

obj = D()

print(obj.a) # 2
print(obj.b) # 3
print(obj.c) # 5
print(obj.d) # 6
obj.x() # A.x
obj.y() # C.y
obj.z() # D.z