#game.py
#mostly game loop code here
import time
from tkinter import *

class Game:
    def __init__(self, canvas_width, canvas_height):
        self.width = canvas_width
        self.height = canvas_height
        tk = Tk()
        canvas = Canvas(tk, width=self.width, height=self.height)
        canvas.pack()
        canvas.create_line(0, self.height/2, self.width, self.height/2, fill="#12ff53")
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
                self.update()
    def update(self):
        #this should be overridden with custom game code that gets called every tick
        pass

