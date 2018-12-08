#main.py
#example game code here
from scene import Scene
from sprite import Sprite, BorderMode, CollideMode

left_up = False
left_down = False
right_up = False
right_down = False

def gameloop():
    global left_up, left_down, right_up, right_down
    scene.draw_line(scene.get_width()/2, 0, scene.get_width()/2, scene.get_height(), "#000000")
    if(left_up):
        left_paddle.dy -= 1
    elif(left_down):
        left_paddle.dy += 1
        
    if(right_up):
        right_paddle.dy -= 1
    elif(right_down):
        right_paddle.dy += 1

    #physics
    if(left_paddle.dy > .1):
        left_paddle.dy -= .1
    elif(left_paddle.dy < -.1):
        left_paddle.dy += .1

def keypress_handler(event):
    global left_up, left_down, right_up, right_down
    print(event.type)
    if(event.char == "w"):
        left_up = True
    if(event.char == "s"):
        left_down = True
    if(event.keysym == "Up"):
        right_up = True
    if(event.keysym == "Down"):
        right_down = True

def keyrelease_handler(event):
    global left_up, left_down, right_up, right_down
    print(event)
    if(event.char == "w"):
        left_up = False
    if(event.char == "s"):
        left_down = False
    if(event.keysym == "Up"):
        right_up = False
    if(event.keysym == "Down"):
        right_down = False

scene = Scene(400, 300)
scene.update = gameloop

smile = Sprite("ball.png", scene.get_width()/2 - 50, scene.get_height()/2 - 30, 30, 30)
left_paddle = Sprite("paddle.png", 50, scene.get_height()/2, 30, 60)
right_paddle = Sprite("paddle.png", scene.get_width() - 50, scene.get_height()/2, 30, 60)

left_bound = Sprite("bound.png", 15, scene.get_height(), 30, 600)
right_bound = Sprite("bound.png", scene.get_width(), scene.get_height(), 30, 600)


smile.set_collidable(True)
left_paddle.set_collidable(True)
right_paddle.set_collidable(True)
smile.collide_mode = CollideMode.BOUNCE
left_bound.collide_mode = CollideMode.KILLS
right_bound.collide_mode = CollideMode.KILLS

smile.border_mode = BorderMode.BOUNCE
left_bound.border_mode = BorderMode.IGNORE
right_bound.border_mode = BorderMode.IGNORE

smile.set_collidable(True)
scene.add_sprite(smile)
scene.add_sprite(left_paddle)
scene.add_sprite(right_paddle)
#scene.add_sprite(left_bound)
#scene.add_sprite(right_bound)

smile.dx = 2

scene.set_keypress_handler(keypress_handler)
scene.set_keyrelease_handler(keyrelease_handler)

scene.bind_input("w")
scene.bind_input("s")
scene.bind_input("Up")
scene.bind_input("Down")
#scene.bind_input("<Up>", right_paddle_up)

scene.start(30)