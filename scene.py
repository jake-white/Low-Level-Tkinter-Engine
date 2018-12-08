#game.py
#mostly game loop code here
import time
from tkinter import *
from sprite import Sprite

class Scene:
    def __init__(self, canvas_width, canvas_height):
        #initialize the tkinter window with a set width and height
        self.width = canvas_width
        self.height = canvas_height
        self.sprites = []
        self.tk = Tk()
        self.tk.resizable(False, False)
        self.tk.title("Pong")
        self.canvas = Canvas(self.tk, width=self.width, height=self.height)
        self.canvas.focus_set()
        self.keypress_handler = None
        self.keyrelease_handler = None
        
    def start(self, fps):
        #start the game loop given frames per second
        self.millisBetweenTicks = (1/fps) * 1000
        self.lastTick = int(time.time() * 1000)
        self.tick()

    def tick(self):
        #this is the game loop
        while(True):
            if(int(time.time()*1000) > self.lastTick + self.millisBetweenTicks):
                self.lastTick = int(time.time() * 1000)
                self.canvas.delete("all")
                self.update_gameobjects()
                self.update()
                self.draw_sprites()

                #tkinter stuff (in place of the tkinter mainloop)
                self.canvas.pack()
                self.tk.update_idletasks()
                self.tk.update()

    def update(self):
        #this should be overridden with custom game code that gets called every tick
        #(this is done in main.py, with the example game)
        pass

    def draw_line(self, x, y, x2, y2, fill):
        self.canvas.create_line(x, y, x2, y2, fill=fill)

    def add_sprite(self, sprite):
        self.sprites.append(sprite)

    def update_gameobjects(self):
        for sprite in self.sprites:
            sprite.collide(self.sprites)
            sprite.tick(self)
    
    def set_keypress_handler(self, keyhandler):
        self.keypress_handler = keyhandler

    def set_keyrelease_handler(self, keyhandler):
        self.keyrelease_handler = keyhandler

    def bind_input(self, key):
        self.canvas.bind("<{}>".format(key), self.keypress_handler)
        self.canvas.bind("<KeyRelease-{}>".format(key), self.keyrelease_handler)

    def bind_specific_input(self, key, callback):
        self.canvas.bind(key, callback)

    def draw_sprites(self):
        for sprite in self.sprites:
            self.canvas.create_image(sprite.x, sprite.y, image=sprite)

    def get_width(self): #returns window width
        return self.width
    def get_height(self): #returns window height
        return self.height