from time import perf_counter
from getkey import getkey, keys
from parts.esq import *

def get_input(*args):
  start=perf_counter()
  line=""
  input=""
  preface=">"
  if args:
    preface=args[0]
    if len(args)>=2:
      line=args[1]
      preface+=line

  print(end=esq.clearline+esq.sdown+esq.sup+preface, flush=True)
  while True:
    a=getkey()
    if a=="\n":
      input=line
      break
    elif a==keys.UP:
      input="go north"
      break
    elif a==keys.DOWN:
      input="go south"
      break
    elif a==keys.LEFT:
      input="go west"
      break
    elif a==keys.RIGHT:
      input="go east"
      break
    elif a==keys.BACKSPACE:
      if len(line)>0:
        line=line[0:len(line)-1]
        print(end="\b \b",flush=True)
    elif len(a)==1:
      print(end=a,flush=True)
      line+=a

  print()
  leftovers=""
  if input!=line:
    leftovers=line
  return {
    "input":input,
    "leftovers":leftovers,
    "time":perf_counter()-start
  }
class view:
  def __init__(self):
    self.disp_data=[]
    self.player_face="[>"
  def reset_disp(self):
    self.disp_data = []
    sd=10 # shine distance
    vs=sd*2+1 # view size
    for y in range(vs):
      self.disp_data.append([])
      for x in range(vs):
        a=sd-x
        b=sd-y
        csq=a*a+b*b
        if csq>=sd*sd:self.disp_data[y].append(esq.deft_bg+esq.white+"##")
        else: self.disp_data[y].append(esq.black_bg+"  ")
    self.disp_data[sd][sd]=esq.black_bg+esq.cyan+self.player_face
  def set_disp(self, world, x, y):
    quadrant = 0
    inx = x%50
    iny = y%50

    if inx<25:
      if iny<25:
        quadrant = 4 # top left -> bottom right
      else:
        quadrant = 1 # bottom left -> top right
    else:
      if iny<25:
        quadrant = 3 # top right -> bottom left
      else:
        quadrant = 2 # bottom right -> top left
    
    areay = y//50
    areax = x//50
    insectx = areax%5
    insecty = areay%5
    
    topleft = world.map
    topright = world.map
    bottomleft = world.map
    bottomright = world.map

    if quadrant == 4:
      bottomright = world.map[secty][sectx][areaID]
      if secty-1>0 and sectx-1>0: # top left
        pass
        # topleft = world.map[secty-1][sectx-1][]
    
    self.disp_data = []
    sd=10 # shine distance
    vs=sd*2+1 # view size
    for y in range(vs):
      self.disp_data.append([])
      for x in range(vs):
        a=sd-x
        b=sd-y
        csq=a*a+b*b
        if csq>=sd*sd:self.disp_data[y].append(esq.deft_bg+esq.white+"##")
        else:
          self.disp_data[y].append(esq.black_bg+"  ")
    self.disp_data[sd][sd]=esq.black_bg+esq.cyan+self.player_face
    