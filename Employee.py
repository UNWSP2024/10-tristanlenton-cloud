class Employee:
    def __init__(self, name, id_number, department, job_title):
        self.name = name
        self._id_number = id_number
        self.department = department
        self.job_title = job_title
employee1 = Employee("Susan Meyers", "47889", "Accounting", "Vice President")
employee2 = Employee("Mark Jones", "39119", "IT", "Programmer")
employee3 = Employee("Joy Rogers", "Joy Rogers", "Manufacturing", "Engineer")
print(employee1.name, employee1._id_number, employee1.department, employee1.job_title)
print(employee2.name, employee2._id_number, employee2.department, employee2.job_title)
print(employee3.name, employee3._id_number, employee3.department, employee3.job_title)
