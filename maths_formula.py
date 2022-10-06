class Circle:
    pi = 3.142

    def __init__(self, r):
        self.r = r

    def get_area(self):
        return Circle.pi * self.r * self.r

    def get_circumference(self):
        return 2 * Circle.pi * self.r


radius = Circle(7)
print(f' Area of a circle: {radius.get_area()}')
p = Circle(7)
print(f' Circumference of a circle: {p.get_circumference()}')


class Rectangle:
    def __init__(self, breadth, length):
        self.breadth = breadth
        self.length = length

    def get_areas(self):
        return  self.breadth * self.length

    def get_perimeter(self):
        return 2 * (self.breadth + self.length)


A = Rectangle(7, 10)
print(f'area of a rectangle: {A.get_areas()}')
p = Rectangle(8, 10)
print(f' perimeter of a rectangle: {p.get_perimeter()}')

from math import sqrt


class Cylinder:
    pi = 22/7

    def __init__(self, r, height):
        self.r = r
        self.height = height

    def get_volume(self):
        return Cylinder.pi * self.r * self.r * self.height

    def total_surface(self):
        return 2 * Cylinder.pi * self.r * (self.height + self.r)

    def cylinder_curvedsurface(self):
        return 2 * Cylinder.pi * self.r * self.height



v = Cylinder(7, 14)
print(f'Volume of a cylinder: {v.get_volume()}')
s = Cylinder(7, 10)
print(f'Total surface area of a cylinder: {s.total_surface()}')
a = Cylinder(7, 10)
print(f'curved surface area: {a.cylinder_curvedsurface()}')


class Cone:
    pi = 22/7

    def __init__(self, radius, height,l):
        self.radius = radius
        self.height = height
        self.slant = l

    def get_volcone(self):
        return 1/3 * Cone.pi * self.radius * self.radius * self.height

    def total_surface(self):
        return Cone.pi * self.radius * (self.radius + self.slant)

    def cone_curvedsurface(self):
        return  Cone.pi * self.radius * self.slant


d = Cone(7, 14, 0)
print(f'Volume of a cone: {d.get_volcone()}')
s = Cone(7, 0, 10)
print(f'Total surface area of a cone: {s.total_surface()}')
f = Cone(7, 0, 10)
print(f'curved surface area: {f.cone_curvedsurface()}')


class Cube:

    def __init__(self, length):
        self.length = length

    def get_volcube(self):
        return self.length * self.length * self.length

    def get_surface(self):
        return  6 * self.length * self.length


d = Cube(10)
print(f'Volume of a cube: {d.get_volcube()}')
s = Cube(10)
print(f'Total surface area of a cube: {s.get_surface()}')


class Cuboid:

    def __init__(self, length, breadth, height):
        self.length = length
        self.breadth = breadth
        self.height = height

    def get_volcuboid(self):
        return self.length * self.breadth * self.height

    def get_surface(self):
        return  2 * (self.length * self.breadth + self.breadth * self.height + self.length * self.height)


d = Cuboid(5, 7, 10)
print(f'Volume of a cuboid: {d.get_volcuboid()}')
s = Cuboid(5, 7, 10)
print(f'Total surface area of a cuboid: {s.get_surface()}')


class Cone:
    pi = 22/7

    def __init__(self, radius, height,l):
        self.radius = r
        self.height = height
        self.slant = l

    def get_volcone(self):
        return 1/3 * Cone.pi * self.radius * self.radius * self.height

    def total_surface(self):
        return Cone.pi * self.radius * (self.height + self.slant)

    def cone_curvedsurface(self):
        return  Cone.pi * self.radius * self.slant


    d = Cone(7, 14, 0)
    print(f'Volume of a cone: {d.get_volcone}')
    s = Cone(7, 14, 10)
    print(f'Total surface area of a cone: {s.total_surface()}')
    f = Cone(7, 0, 10)
    print(f'curved surface area: {f.cone_curvedsurface()}')
