class Employee:
    def __init__(self, name, id, *args):
        self.name = name
        self.id = id

    def get_info(self):
        return f'name: {self.name}, id:{self.id}'


class Manager(Employee):
    def __init__(self, name, id, departments, *args):
        super().__init__(name, id, *args)
        self.department = departments

    def manager_project(self):
        return f'name: {self.name}, id:{self.id}, departments:{self.department}'


class Technician(Employee):
    def __init__(self, name, id, specialization, *args):
        super().__init__(name, id, *args)
        self.specialization = specialization

    def perfo_maintenance(self):
        return f'name: {self.name}, id:{self.id},  specialization:{self.specialization}'


class Tech_Manager(Manager, Technician):
    def __init__(self, name, id, departments, specialization, *args):
        super().__init__(name, id, departments, specialization, *args)
        self.team = []

    def edd_employee(self, employee):
        self.team.append(employee)

    def get_team_info(self):
        return f'team: {', '.join(self.team)}'


a = Employee('a', 1)
print(a.get_info())
a = Manager('a', 1, 'zxc')
print(a.manager_project())
a = Technician('a', 1, 'cxz')
print(a.perfo_maintenance())
a = Tech_Manager('a', 1, 'zxc', 'cxz')
print(a.perfo_maintenance())
print(a.manager_project())
print(a.get_team_info())
a.edd_employee('b')
print(a.get_team_info())
a.edd_employee('b1')
print(a.get_team_info())