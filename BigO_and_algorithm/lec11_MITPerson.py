import datetime

class Person(object):
    def __init__(self, name):
        self.birthday = None
        # create a person with name: name
        self.name = name
        try:
            # if the name entered has space
            first_blank = name.rindex(" ")
            self.last_name = name[first_blank+1:]
        except:
            self.last_name = name

    def get_last_name(self):
        # return instance last name
        return self.last_name

    def set_birthday(self, birth_date):
        # assume birth date is of type datetime.date
        # set instance birthday to birth date
        assert(type(birth_date) == datetime.date)
        self.birthday = birth_date

    def get_age(self):
        # assumes that instance birthday has been set
        # returns instance current age in days
        assert(self.birthday != None)
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        # return True if instance name is lexico-graphically greater than other
        if self.name < other.name:
            return True
        else:
            False

    def __str__(self):
        return self.name

class MITPerson(Person):
    next_Id_Num = 0
    def __init__(self, name):
        Person.__init__(self, name)
        self.Id_Num = MITPerson.next_Id_Num
        MITPerson.next_Id_Num += 1
    def get_Id_Num(self):
        return self.Id_Num
    def __lt__(self, other):
        return self.Id_Num < other.Id_Num
    def is_Student(self):
        return type(self) == UnderGraduate or type(self) == Graduate

class UnderGraduate(MITPerson):
    def __init__(self, name):
        MITPerson.__init__(self, name)
        self.year = None
    def set_Year(self, year):
        if year > 5:
            raise OverflowError("Too many years...")
        self.year = year
    def get_Year(self):
        return self.year

class Graduate(MITPerson):
    pass
