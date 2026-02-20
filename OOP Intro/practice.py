import numpy as np  
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        # self.maths = maths
        # self.science = science
        # self.it = it
    def get_average(self):
        print(f"{self.name} got an Average marks of {round(np.average(self.marks),2)}")

student1 = Student('Pratish',[45,66,44])

student1.get_average()

# 

