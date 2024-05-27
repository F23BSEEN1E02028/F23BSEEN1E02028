#Name : Emam Mazhar
#Roll No : F23BSEEN1E02028
#Assignment of Oop Teacher Allocations

class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

class School:
    def __init__(self, name):
        self.name = name
        self.teachers = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def allocate_teachers(self):
        allocation = {}
        for teacher in self.teachers:
            if teacher.subject not in allocation:
                allocation[teacher.subject] = [teacher.name]
            else:
                allocation[teacher.subject].append(teacher.name)
        return allocation


school = School("High School")

teacher1 = Teacher("Ali", "Math")
teacher2 = Teacher("Zain", "Science")
teacher3 = Teacher("Raouf", "English")

school.add_teacher(teacher1)
school.add_teacher(teacher2)
school.add_teacher(teacher3)

allocation = school.allocate_teachers()
print(allocation)
