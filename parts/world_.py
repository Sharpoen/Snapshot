from random import choice
from parts.esq import *


blocks = {
  "stone":{
    "face":esq.gray
  },
  "air":{
    "face":"ignore"
  }
}

class world:#yah um there isn't much here
  def __init__(self):
    self.topLeft=[]
    self.bottomLeft=[]
    self.topRight=[]
    self.bottomRight=[]

  def load_area(self, segment, path):
    # segs -> 'topLeft', 'bottomLeft', 'bottomRight', 'topRight'
    
  def go_north(self):
    return choice([f"{esq.green}You go north.", f"{esq.red}You couldn't go north."])
  def go_east(self):
    return choice([f"{esq.green}You go east.", f"{esq.red}You couldn't go east."])
  def go_south(self):
    return choice([f"{esq.green}You go south.", f"{esq.red}You couldn't go south."])
  def go_west(self):
    return choice([f"{esq.green}You go west.", f"{esq.red}You couldn't go west."])
