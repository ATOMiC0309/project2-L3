 # 1-topshiriq:
# Figure = type("Figure", (), {"name": "Figure", "get_info": lambda self: self.name})
# print(Figure().get_info())
#
# Triangle = type("Triangle", (Figure, ), {"name": "Triangle"})
# print(Triangle.name)
#
# Square = type("Square", (Figure, ), {"name": "Square"})
# print(Square.name)
#
# Circle = type("Circle", (Figure, ), {"name": "Circle"})
# print(Circle.name)

# 2-topshiriq
# class Meta(type):
#     def __new__(cls, name, bases, attrs):
#         attrs["model"] = "Malibu"
#         attrs["color"] = "Black"
#         attrs["speed"] = 300
#         return type(name, bases, attrs)
#
# class Car(metaclass=Meta):
#     pass
#
# print(Car.model)

# 3-topshiriq

# class Meta(type):
#     def __new__(cls, name, bases, attrs):
#         attrs["id_num"] = 1
#         attrs["name"] = "Jadval1"
#         attrs["phone"] = "+998912345678"
#         attrs["address"] = "Fergana"
#         return type(name, bases, attrs)
#
# class Table(metaclass=Meta):
#     pass
#
# print(Table.name)

#  4- topshiriq

# class Calculate:
#     @classmethod
#     def qoshish(cls, a, b):
#         return f"{a}+{b}={a+b}"
#
#     @classmethod
#     def ayirish(cls, a, b):
#         return f"{a}-{b}={a-b}"
#
#     @classmethod
#     def kopaytirish(cls, a, b):
#         return f"{a}*{b}={a*b}"
#
#     @classmethod
#     def bolish(cls, a, b):
#         return f"{a}/{b}={a/b}"
#
# print(Calculate.qoshish(3, 4))
# print(Calculate.ayirish(3, 4))
# print(Calculate.bolish(3, 4))
# print(Calculate.kopaytirish(3, 4))