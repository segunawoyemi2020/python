class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")
point = Point(10, 20)
point1 = Point('move', 'draw')
print(point1.x)
print(point.x)
print(point.y)
print(point1.y)


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'Hi, I am {self.name}')


John = Person('John Smith')
John.talk()

bob = Person('Bob Smith')
bob.talk()

import converters
print(converters.kg_to_lbs(70))

from converters import kg_to_lbs

print(kg_to_lbs(100))

from max import find_max

numbers = [10, 15, 20, 50, 12, 45]
print(find_max(numbers))

from grade import find_grade
print(find_grade(37))

from principal_comment import result_comment
print(result_comment(30))

from calculator import calculate
print(calculate(50,5,'k'))

maximum = lambda number : number ** 5
print(maximum(6))



