from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def set_first_name(self, new_first):
        self.first_name = new_first

    def set_last_name(self, new_last):
        self.last_name = new_last

    @abstractmethod
    def compute_salary(self):
        pass

    def full_name(self):
        fullname = self.first_name + '' + self.last_name
        return fullname

class FulltimeEmployee(Employee):
    def __init__(self, first_name, last_name, base_salary=3500.0, bonus=200.0):
        super().__init__(first_name, last_name)
        self.base_salary = base_salary
        self.bonus = bonus

    def get_base_salary(self):
        return self.base_salary

    def get_bonus(self):
        return self.bonus

    def set_base_salary(self, new_base_salary):
        self.base_salary = new_base_salary

    def set_bonus(self, new_bonus):
        self.bonus = new_bonus

    def compute_salary(self):
        salario_total = self.base_salary + self.bonus
        return salario_total
