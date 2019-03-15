class CourseList(object):
    def __init__(self, number):
        # assign the course number
        self.number = number
        # initialize the students with empty list
        self.students = []
    def add_student(self, who):
        # start of defensive programming
        if not who.is_Student():
            raise TypeError("Not a student")
        if who in self.students:
            raise ValueError("Duplicate student")
        # end of defensive programming
        self.students.append(who)
    def remove_student(self, who):
        try:
            self.students.remove(who)
        except:
            print(str(who) + " not in " + self.number)
    def AllStudents(self):
        for s in self.students:
            yield s
    def get_ugs(self):
        index  = 0
        while index < len(self.students):
            if type(self.students[index]) == UnderGraduate:
                yield self.students[index]
                index += 1
