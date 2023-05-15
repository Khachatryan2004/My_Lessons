'''
# խնդիր 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)


class Student(Person):
    def __init__(self, name, age, section):
        Person.__init__(self, name, age)
        self.section = section

    def displayStudent(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Section:", self.section)


student = Student("John", "16", "A")
student.displayStudent()
'''


# խնդիր 2
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def display(self):
        print("Length:", self.length)
        print("Width:", self.width)
        print("Perimeter:", self.perimeter())
        print("Area:", self.area())


class Parallelepiped(Rectangle):
    def __init__(self, length, width, height):
        Rectangle.__init__(self, length, width)
        self.height = height

    def volume(self):
        return self.length * self.width * self.height


parallelepiped = Parallelepiped(7, 3, 5)
parallelepiped.display()
print("Volume:", parallelepiped.volume())
