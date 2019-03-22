import cls_variable

class Trainee(cls_variable.Employee):
    def get_salary(self, days):
        print(days*200)
    def get_emp_salary(self, days):
        super().get_salary(days)

ramesh = cls_variable.Employee(223,9564)
ramesh.get_salary(22)
deepak = Trainee(226,99666)
deepak.get_emp_salary(22)
deepak.get_salary(22)