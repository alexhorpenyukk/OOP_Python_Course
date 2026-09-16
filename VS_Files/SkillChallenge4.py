#################
## CHALLENGE 4 ##
#################

# Requirements
# - Define a new type called Vector that stores 3 instance attributes: x, y, z
# - Users should be able to create new instances as Vector(x=1, y=2, z=3), where the coordinates are positional args
# with no defaults
# - Instances of this new Vector type should have a representation that would help the user reconstruct the instance
# - The magnitude of the vector should be accessible through a method, ideally a built-in
#     hint: the magnitude is calculated as sqrt of sum of squared coordinates
#     hint2: as far as built-ins are concerned, __len__ will not work; try to target abs()?
# - Users should be able to add two vectors to get a third, e.g. Vector(1, 2, 3) + Vector(4, 5, 6) -> Vector(5, 7, 9)
# - Users should be able to numerically scale a vector, e.g. Vector(1, 2, 3) * 2 = Vector(2, 4, 6)
# - The scalar multiplication operation should work the same regardless of the order of operands, e.g. Vector(1, 2, 3) * 2 =
# 2 * Vector(1, 2, 3)
# - All comparison operators should be supported
# - Vector should be hashable
# - A Vector instance should evaluate to False if and only if its magnitude is zero
# - Lastly, the Vector class should let the user select coordinates using square brackets too, e.g.
# if v1 = Vector(1, 2, 3) then v1['y'] or v1['Y'] should return 2

# Example Usage:
# v1 = Vector(1, 2, 3)
# v2 = Vector(2, 3, 6)
# v3 = Vector(0, 0, 0)

# v1 + v2
# Vector(3, 5, 9)

# bool(v1)
# True

# bool(v3)
# False

# abs(v2) == math.sqrt(49)
# True

# v2 * 2 == Vector(4, 6, 12)
# True

# assert 2 * v2 == Vector(4, 6, 12)
# True

# v1 < v2
# True

# v1 <= v2
# True

# v1 > v2
# False

# v1 == eval(repr(v1))
# True

# v1['x']
# 1

# v2['Y']
# 3

# v3['Z']
# 0

# v3["Andy"]
# NotImplemented

import math
from functools import total_ordering

@total_ordering
class Vector():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def magnitude(self):
        return math.sqrt((self.x)**2 + (self.y)**2 + (self.z)**2)
    
    def __repr__(self):
        return f"Vector(x={self.x}, y={self.y}, z={self.z})"
    
    def __add__(self, other):
        
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    
    def __mul__(self, multiplyer):
        return Vector(self.x * multiplyer, self.y * multiplyer, self.z * multiplyer)

    def __rmul__(self, multiplyer):
        return Vector(self.x * multiplyer, self.y * multiplyer, self.z * multiplyer) 
    
    def __bool__(self):
        if self.magnitude() == 0:
            return False
        
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return True
        return False
    
    def __abs__(self):
        return float(self.x * self.y * self.z)
    
    def __gt__(self, other):
        sum_s = self.x + self.y + self.z
        sum_o = other.x + other.y + other.z

        return sum_s > sum_o
    
    def __getitem__(self, key):
        dct = {'x' : self.x, 'y' : self.y, 'z' : self.z}
        return dct[key.lower()]
    

v1 = Vector(1, 2, 3)
v2 = Vector(1, 2, 4)

print(4 * v1)
print(v1.magnitude())
print(v1 == Vector(1, 2, 3))
print(abs(v1))
print(v1 > v2)
print(v1 <= v2)
print(eval(repr(v1)))
