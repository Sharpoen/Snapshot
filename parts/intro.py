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
  print("| 'guide'            |  go to guide                  |")
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

class guide:
  pages = [
    {
      "title":"1 : Guide",
      "lines":[
        "Thank you for playing \"Snapshot!\"",
        "",
        "To navigate the guide, use arrow keys.",
        "[RIGHT]: Next Page",
        "[LEFT ]: Previous Page",
        "[UP   ]: Scroll Up",
        "[DOWN ]: Scroll Down",
        "",
        "This guide will describe how to play the game, and a little bit about the",
        " game that may be difficult to find out on your own.",
        "-------------------------------------------------------------------------",
        "The table of contents will be on the next page."
      ]
    },
    {
      "title":"2 : Guide -- Table of Contents",
      "lines":[
        "1 - 2    : Guide",
        "3        : Controls",
        "4-5      : Mechanics",
        "6-8      : Story"
      ]
    }
  ]
  def __init__(self):
    self.is_open = False
    self.on_page = 0
    self.scroll = 0
  def operate(self):
    view = self.pages[self.on_page]["lines"][self.scroll:self.scroll+10]
    if len(view) < 10:
      for i in range(10 - len(view)):
        view.append("")
    view.insert(0, "\"%s\"\n<%s>"%(self.pages[self.on_page]["title"], self.scroll))
    print(esq.clear+esq.top+esq.reset+esq.deft_bg+esq.white+'\n| '.join(view))
    print("<%s>"%(self.scroll+10))
    a = get_input("[use arrow keys to navigate] [type 'continue' when finished]\n? ")
    inp = a["input"].lower()
    if inp in ["end", "quit", "cont", "continue"]:
      self.is_open=False
    if inp == "go east":
      self.on_page += 1
      self.scroll = 0
    if inp == "go west":
      self.on_page -= 1
      self.scroll = 0
    if inp == "go north" and self.scroll > 0:
      self.scroll -= 1
    if inp == "go south" and self.scroll < len(self.pages[self.on_page]["lines"])-1:
      self.scroll += 1
    if self.on_page >= len(self.pages):
      self.on_page = len(self.pages)-1
    if self.on_page < 0:
      self.on_page = 0
  def open(self):
    self.on_page = 0
    self.is_open = True
    while self.is_open:
      self.operate()

guide1 = guide()

def go():
  print(esq.clear+esq.top+"Welcome to Snapshot!\nQuick start guide:\n-> You are lost in a place you do not know.\n-> It's pitch black, and all you have is a broken flashlight, and your camera.\n-> To see your surroundings you must take a photo.\n-> All you know is you must get home.\n\n Press 'h' for a full guide (use this if it is your first time playing)\npress 'c' or any other key skip to command reference sheet.")
  if getkey().lower()=="h":
    guide1.open()

  crs()