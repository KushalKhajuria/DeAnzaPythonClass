class School:
    def __init__(self):
        self.studentList = []
    def __str__(self):
        str = ""
        for student in self.studentList:
            str += (student.__str__() + "\n")
        return str
    def addStudent(self, Student):
        self.studentList.append(Student)
    def removeStudent(self, Student):
        self.studentList.remove(Student)
    def getStudentList(self):
        return self.studentList

class Student (School):
    def __init__(self, firstName, lastName, gpa):
        self.firstName = firstName
        self.lastName = lastName
        self.gpa = gpa
    def __str__(self):
        return("Name:" + self.firstName + " " + self.lastName + "\nGPA:" + str(self.gpa) + "\n")
    def getFirstName(self):
        return self.firstName
    def getLastName(self):
        return self.lastName
    def getGpa(self):
        return self.gpa
    def setGpa(self, gpa):
        self.gpa = gpa

student1 = Student("Damon", "Derese", 4.0)
student2 = Student("Terence", "Busk", 3.9)
student3 = Student("Sahiti", "Chilukuri", 3.5)
student4 = Student("Vijay", "Baliga", 4.0)
student5 = Student("Jordan", "Nakamoto", 3.7)
student6 = Student("Fangyi", "Wang", 2.8)
student7 = Student("Ivan", "Dimitrov", 3.1)
student8 = Student("Kai", "Del", 3.5)
student9 = Student("Benjamin", "Lublin", 3.8)
student10 = Student("Tan", "Nguyen", 1.5)

school = School()
school.addStudent(student1)
school.addStudent(student2)
school.addStudent(student3)
school.addStudent(student4)
school.addStudent(student5)
school.addStudent(student6)
school.addStudent(student7)
school.addStudent(student8)
school.addStudent(student9)
school.addStudent(student10)

print(school)

#print(student1)
#print(student2)
#print(student3)
#print(student4)
#print(student5)
#print(student6)
#print(student7)
#print(student8)
#print(student9)
#print(student10)
