class Student:
    def __init__(self, name, roll, markList, stream, percentage=None, grade=None, division=None):
        self.name = name
        self.roll = roll
        self.markList = markList
        self.stream = stream
        self.percentage = percentage
        self.grade = grade
        self.division = division

    def setMarks(self, markList):
        self.markList = markList

    def getMarks(self):
        return self.markList

    def getStream(self):
        return self.stream

    def calculatePercentage(self):
        self.percentage = sum(self.markList) / len(self.markList)

    def calculateGrade(self):
        if self.percentage >= 90:
            self.grade = "A"
        elif self.percentage >= 80:
            self.grade = "B"
        elif self.percentage >= 70:
            self.grade = "C"
        elif self.percentage >= 60:
            self.grade = "D"
        else:
            self.grade = "F"

    def calculateDivision(self):
        if self.percentage >= 60:
            self.division = "First"
        elif self.percentage >= 45:
            self.division = "Second"
        elif self.percentage >= 33:
            self.division = "Third"
        else:
            self.division = "Fail"

    def display(self):
        self.calculatePercentage()
        self.calculateGrade()
        self.calculateDivision()
        print(f"Name: {self.name}, Roll: {self.roll}, Stream: {self.stream}, Percentage: {self.percentage:.2f]]}, Grade: {self.grade}, Division: {self.division}")


# Example usage
stu1 = Student("Chutkit", 1, [22, 23, 34, 55, 22], "Science")
stu1.setMarks([22, 23, 34, 55, 22])
print("Marks:", stu1.getMarks())
print("Stream:", stu1.getStream())
stu1.display()