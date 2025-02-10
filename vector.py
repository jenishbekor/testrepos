class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __len__(self):
        return 2  # Vectors in 2D space have a length of 2 components

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Index out of range")

    def __setitem__(self, index, value):
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        else:
            raise IndexError("Index out of range")

    def __call__(self):
        return f"Vector called! Current values: ({self.x}, {self.y})"

# Example usage
v1 = Vector(2, 3)
v2 = Vector(4, 5)

print(v1)               # Output: (2, 3)
print(repr(v1))         # Output: Vector(2, 3)
print(v1 + v2)          # Output: (6, 8)
print(v1 - v2)          # Output: (-2, -2)
print(v1 * 3)           # Output: (6, 9)
print(v1 == v2)         # Output: False
print(len(v1))          # Output: 2
print(v1[0])            # Output: 2
v1[1] = 10
print(v1)               # Output: (2, 10)
print(v1())             # Output: Vector called! Current values: (2, 10)