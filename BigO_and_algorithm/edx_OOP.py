class Coordinate(object):
    # how to create an instance
    # typically the first method of a class
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, other):
        # dot notation to access the data
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        distance = (x_diff_sq + y_diff_sq)**0.5
        return distance
    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"
    def __sub__(self, other):
        sub_x = self.x - other.x
        sub_y = self.y - other.y
        # can also return new instances of the class
        return Coordinate(sub_x, sub_y)

class Fraction(object):
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    def __str__(self):
        return "{}/{}".format(self.numerator, self.denominator)
    def __add__(self, other):
        numerator_sum = self.numerator + other.numerator
        denominator_sum = self.denominator + other.denominator
        return "{}/{}".format(numerator_sum, denominator_sum)
    def __sub__(self, other):
        numerator_diff = self.numerator - other.numerator
        denominator_diff = self.denominator - other.denominator
        return "{}/{}".format(numerator_diff, denominator_diff)
    def __float__(self):
        return self.numerator / self.denominator

class IntegerSet(object):
    def __init__(self):
        """ this initialize the object"""
        self.int_list = []
    def __str__(self):
        return str(self.int_list)
    def insert(self, e):
        if e not in self.int_list:
            self.int_list.append(e)
    def member(self, e):
        if e in self.int_list:
            return True
        else:
            return False
    def remove(self, e):
        if e in self.int_list:
            del(self.int_list[self.int_list.index(e)])
        else:
            return "error! element not in set"

class Animal(object):
    # special method to create an instance
    def __init__(self, age):
        self.age = age
        self.name = None
        # name is a data attribute even though
        # an instance is not initialized with it as a parameter
    # getter
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    # setter
    def set_age(self, new_age):
        self.age = new_age
    def set_name(self, new_name=""):
        self.name = new_name
    def __str__(self):
        return "animal:" + str(self.name)+":"+str(self.age)

class Cat(Animal):
    def speak(self):
        print("meow")
    def __str__(self):
        return "cat:{}:{}".format(self.name, self.age)

class Rabbit(Animal):
    tag = 1 # class variable
    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rabbit_id = Rabbit.tag
        Rabbit.tag += 1
        # tag used to give unique id to each new rabbit instance
    # getter methods
    def get_rabbit_id(self):
        return str(self.rabbit_id).zfill(3)
        # zfill fill up the number
    def get_parent1(self):
        return self.parent1
    def get_parent2(self):
        return self.parent2