# 1
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f'название книги: {self.title}, автор: {self.author}, год издания {self.year}'


# 2
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, new_radius):
        self.radius = new_radius


c = Circle(2)
print(c.get_radius())
c.set_radius(5)
print(c.get_radius())
