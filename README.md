# Low-Level-Tkinter-Engine
Low-level game engine in Python/Tkinter for CSCI43700

Low-level engine using Tkinter and Pillow (Python Imaging Library).
Includes Scene and Sprite objects.

Scene using tkinter Canvas to render/draw sprites and geometry. Sprite inherits PIL's PhotoImage class to store .png files.
Supports keypress and keyrelease input keyhandlers as well as basic sprite distance-based collision.
Scenes support different bounding modes.

Contains (buggy) pong demo in main.py. This consists of several sprites and shows off input, sprite movement, and collision.
