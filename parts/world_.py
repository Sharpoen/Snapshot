import json
from random import choice
from parts.esq import *

class area:
  def __init__(self, path):
    with open("%s/skin.json"%path) as f:
      self.skin = json.load(f)
    with open("%s/special.json"%path) as f:
      self.special = json.load(f)
    with open("%s/collision.txt"%path) as f:
      self.collision = f.readlines()
    with open("%s/color.txt"%path) as f:
      self.color = f.readlines()
    self.render = []
  def ctc(self, char):
    if "b" in char: return esq.blue
    elif "r" in char: return esq.bright_red
    elif "R" in char: return esq.red
    elif "g" in char: return esq.green
    elif "y" in char: return esq.yellow
    elif "w" in char: return esq.white
    elif "c" in char: return esq.cyan
    elif "m" in char: return esq.magenta
    else: return esq.white
  def item_skin(self, item):
    # (skin, color)
    if item["type"]=="door":
      if item["state"]=="open":
        return ( "::", 'c' ) 
      if item["state"]=="closed":
        return ( "||", 'c' )
        
    return ("XX", 'm')
  def generate_render(self):
    self.render = []
    for y, r in enumerate(self.skin):
      line = ""
      for x in range(50):
        if "%s,%s"%(x,y) in self.special:
          item = self.special["%s,%s"%(x,y)]
          line += self.item_skin(item)[0]
          color_line = list(self.color[y])
          color_line[x] = self.item_skin(item)[1]
          self.color[y] = "".join(color_line)
        else:
          line += r[x*2:x*2+2]
      self.render.append(line)
  def test_render(self, *args):
    if len(args)==2:
      for row, row2, row3 in zip(self.render[args[1]:14+args[1]], self.collision[args[1]:14+args[1]], self.color[args[1]:14+args[1]]):
        line=""
        for x in range(14):
          line+="%s%s%s"%(esq.black_bg, self.ctc(row3[x+args[0]]), row[x*2+args[0]*2:x*2+2+args[0]*2])
        print("| %s%s | %s | %s |"%(line, esq.white+esq.deft_bg, row2[args[0]:14+args[0]], row3[args[0]:14+args[0]]))
    else:
      for row, row2, row3 in zip(self.render[0:14], self.collision[0:14], self.color[0:14]):
        line=""
        for x in range(14):
          line+="%s%s%s"%(esq.black_bg, self.ctc(row3[x]), row[x*2:x*2+2])
        print("| %s%s | %s | %s |"%(line, esq.white+esq.deft_bg, row2[0:14], row3[0:14]))

  
class world:  #yah um there isn't much here

    def __init__(self, map):
        self.map = map
        
    def load_area(self, segment, path):
        # segs -> 'topLeft', 'bottomLeft', 'bottomRight', 'topRight'
        pass

    def go_north(self):
        return f"{esq.green}You go north."
    def go_east(self):
        return f"{esq.green}You go east."
    def go_south(self):
        return f"{esq.green}You go south."
    def go_west(self):
        return f"{esq.green}You go west."