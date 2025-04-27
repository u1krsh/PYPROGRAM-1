class Students:
    def __init__(self,name,roll,marks):
        self.name = name
        self.roll = roll
        self.marks = marks
    def clc_avg(self):
        print(f"The average marks for student: {self.name} roll: {self.roll} is {sum(self.marks)/len(self.marks)}")


stud1 = Students("Saumya",44731095,[31,42,34])
stud1.clc_avg()