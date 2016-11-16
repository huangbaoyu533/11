class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def print_grade(self):
        print("%s:%s"%(self.name,self.score))
    def get_grade(self):
        if self.score>90:
            return "A"
        elif self.score>60:
            return "B"
        else :
            return "c"
bart=Student("huang",90)
jack=Student("liu",59)
print("bart.name=",bart.name)
print("bart,score=",bart.score)
bart.print_grade()
print("bart.grade",bart.get_grade())
print("jack.grade",jack.get_grade())
