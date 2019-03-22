class Employee:
    COMPANY ="BOA"
    LOCATION="Hyd"
    __COUNT=0

    def __init__(self,eid,mobile):
        self.eid =eid
        self.mobile =mobile
        Employee.__COUNT+=1
    @classmethod
    def get_emp_cnt(cls):
        print(cls.__COUNT)

    def get_salary(self,days):
        print(days*1000)

def main():
    Employee.__COUNT=12
    ramesh = Employee("12",98598)
    print(ramesh.mobile)
    Employee.get_emp_cnt()
    print(ramesh.get_emp_cnt())
    deepak = Employee("13",98455)
    print(deepak.mobile)
    print(deepak.get_emp_cnt())
    Employee.get_emp_cnt()
    print(Employee.__COUNT)
    deepak.get_salary(100)

if __name__ =="__main__":
    main()