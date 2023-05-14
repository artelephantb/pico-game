from . import vector


class SpriteKind():
    PLAYER = 1
    ENEMY = 2
    PROJECTILE = 3
    TILE = 4

class Sprite:
    """Class to track sprite objects."""
    def __init__(self,kind=SpriteKind.PLAYER, position=(0,0), speed=(0,0), image=None):
        self.kind = kind
        self.position = vector.Vector(position[0],position[1])
        self.image = image
        self.speed = vector.Vector(speed)

        if self.image != None:
            # Set the width and height
            self.width = self.image.size[0]
            self.height = self.image.size[1]
        else:
            self.width = 0
            self.height = 0
        
    def updatePosition(self):
        if self.kind == SpriteKind.PROJECTILE:
            self.position += self.speed
        elif self.kind == SpriteKind.ENEMY:
            # AI updates
            pass
    
    def getBuffer(self):
        return self.image.buffer
        
    
        
    