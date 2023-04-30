class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        newVector = Vector()
        newVector.x = self.x + other.x
        newVector.y = self.y + other.y
        return newVector
    
    def __subtract__(self, other):
        newVector = Vector()
        newVector.x = self.x - other.x
        newVector.y = self.y - other.y
        return newVector
    
    def __mul__(self, scalar:int):
        if isinstance(scalar, int):
            newVector = Vector()
            newVector.x = self.x * scalar
            newVector.y = self.y * scalar
            return newVector
        
    __rmul__ = __mul__
        
    def __str__(self):
        return (self.x,self.y)