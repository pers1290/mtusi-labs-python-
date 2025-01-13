# 1
class UserAccount:
    def __init__(self, username, emal, passworld):
        self.username = username
        self.emal = emal
        self.__passworld = passworld

    def set_passworld(self, npassw):
        self.__passworld = npassw

    def check_passworld(self, passw):
        return self.__passworld == passw


a = UserAccount(1, 2, 3)
print(a.check_passworld(4))
a.set_passworld(4)
print(a.check_passworld(4))


# 2
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return f'марка: {self.make}, модель: {self.model}'


class Car(Vehicle):
    def __init__(self, make, model, fuel):
        super().__init__(model, make)
        self.fuel = fuel

    def get_info(self):
        return f'марка: {self.make}, модель: {self.model}, топливо: {self.fuel}'


a = Vehicle(1, 2)
print(a.get_info())
a = Car(1, 2, 2)
print(a.get_info())
