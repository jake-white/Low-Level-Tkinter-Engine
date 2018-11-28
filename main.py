#main.py
#example game code here
from game import Game

def gameloop():
    print("hello")

game = Game(400, 300)
game.update = gameloop
game.start(5)