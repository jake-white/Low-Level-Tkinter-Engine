#sprite.py
from PIL import Image, ImageTk
from enum import Enum
import math

class Sprite(ImageTk.PhotoImage):    
    def __init__(self, file, x, y, width, height):
        img = Image.open(file).resize((width, height))
        ImageTk.PhotoImage.__init__(self, img)
        self.file = file
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.width = width
        self.height = height
        self.border_mode = BorderMode.WRAP
        self.collidable = False
        self.collide_mode = CollideMode.FIXED

    def tick(self, scene):
        self.physics(scene)
        self.update(scene)

    def update(self, scene):
        #this should be overridden with custom game code that gets called every tick
        #(this is done in main.py, with the example game)
        pass

    def physics(self, scene):
        if(self.border_mode == BorderMode.BOUNCE):
            print(self)
            if(self.x +self.width/2 > scene.get_width()):
                self.dx = -self.dx
                self.x = scene.get_width() - self.width/2
            elif(self.x - self.width/2 < 0):
                self.dx = -self.dx
                self.x = self.width/2
            if(self.y + self.height/2 > scene.get_height()):
                self.dy = -self.dy
                self.y = scene.get_height() - self.height/2
            elif(self.y - self.height/2 < 0):
                self.dy = -self.dy
                self.y = self.height/2
        self.x += self.dx
        self.y += self.dy

    def collide(self, sprites):
        if(self.collidable and self.collide_mode == CollideMode.BOUNCE):
            for sprite in sprites:
                if(not sprite == self and sprite.collidable == True):
                    distance = math.sqrt(math.pow(sprite.x - self.x, 2) + math.pow(sprite.y - self.y, 2))
                    if(distance < self.width):
                        self.dx = -self.dx

    def set_collidable(self, collidable):
        self.collidable = collidable


class BorderMode(Enum):
    WRAP = 1
    BOUNCE = 2
    IGNORE = 3

class CollideMode(Enum):
    FIXED = 1
    BOUNCE = 2
    KILLS = 3