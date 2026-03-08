#dunder methods, also known as magic methods,
#  are special methods in Python that have double underscores
#  at the beginning and end of their names. They are used to define 
# the behavior of objects for built-in operations such as addition, 
# multiplication, string representation, and equality comparison.
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, number):
        if not isinstance(number, (int, float)):
            return NotImplemented
        return Vector(self.x * number, self.y * number)

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return False
        return self.x == other.x and self.y == other.y
    
v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1)
print(v1 + v2)
print(v1 * 3)
print((v1 + v2) == Vector(4, 6))