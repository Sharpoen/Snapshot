from parts.esq import *
from getkey import getkey
from parts.game_ import get_input

def crs(): # command reference sheet
  print(end=esq.clear+esq.top+esq.black_bg+esq.bright_blue)
  print("+----------------------------------------------------+")
  print('| Use arrow keys as a shortcut for "go" commands.    |')
  print("| The longer you take to enter a command, the more   |")
  print("| time the enviroment has to change. Use shortcuts   |")
  print("| and be quick! Tip: 'help' pauses the game.         |")
  print("+--------------------+-------------------------------+")
  print("| 'clear'            |  clear the log                |")
  print("| 'help'             |  display reference sheet      |")
  print("| 'help {command}'   |  get advanced help            |")
  print("| 'take a picture!'  |  hit flashlight               |")
  print("| 'go north'         |  go north one step            |")
  print("| 'go east'          |  go east one step             |")
  print("| 'go south'         |  go south one step            |")
  print("| 'go west'          |  go west one step             |")
  print("| 'inspect'          |  inspect surroundings         |")
  print("| 'open door'        |  open door                    |")
  print("| 'into {thing}'     |  attempt to go inside {thing} |")
  print("| 'destroy {thing}'  |  attempt to destroy {thing}   |")
  print("+----------------------------------------------------+")
  
  print(esq.deft_bg+"Press 'c' or any key to continue.")
  getkey()
def guide():
  print(end=esq.clear+esq.top)
  print("Guide coming soon!")
  print("Press any key to continue.")
  getkey()
def go():
  print(esq.clear+esq.top+"Welcome to Snapshot!\nQuick start guide:\n-> You are lost in a place you do not know.\n-> It's pitch black, and all you have is a broken flashlight, and your camera.\n-> To see your surroundings you must take a photo.\n-> All you know is you must get home.\n\n Press 'h' for a full guide\npress 'c' or any other key skip to command reference sheet.")
  if getkey().lower()=="h":
    guide()
  crs()
