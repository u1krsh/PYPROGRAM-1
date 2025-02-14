class Student:
    count = 0
    total = 0
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total += gpa
        
    #instance  meathod
    def get_info(self):
        return f"{self.name} has a GPA of {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return cls.count
    
    @classmethod
    def get_average(cls):
        return cls.total / cls.count
    

    