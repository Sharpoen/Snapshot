from time import perf_counter
from getkey import getkey, keys
from parts.esq import *

game_extra = []

def get_inputMobile(text):
  start=perf_counter()
  inp = input(text)
  return {
    "input":inp,
    "leftovers":"",
    "time":perf_counter()-start
  }
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
        if csq>=sd*sd:self.disp_data[y].append(esq.deft_bg+esq.white+"+-")
        else: self.disp_data[y].append(esq.black_bg+"  ")
    self.disp_data[sd][sd]=esq.black_bg+esq.cyan+self.player_face
  def set_disp(self, world, x, y):
    quadrant = 0

    areay = y//50
    areax = x//50
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
    
    
    topleft = world.map
    topright = world.map
    bottomleft = world.map
    bottomright = world.map

    offsetx = 0
    offsety = 0
    
    if quadrant == 4: # bottom right
      bottomright = world.gfm(areay, areax)
      topleft = world.gfm(areay-1, areax-1)
      topright = world.gfm(areay-1, areax)
      bottomleft = world.gfm(areay, areax-1)
      offsetx = 50+inx
      offsety = 50+iny
    if quadrant == 1: # top right
      topright = world.gfm(areay, areax)
      topleft = world.gfm(areay, areax-1)
      bottomleft = world.gfm(areay+1, areax-1)
      bottomright = world.gfm(areay+1, areax)
      offsetx = 50+inx
      offsety = iny
    if quadrant == 3: # bottom left
      bottomleft = world.gfm(areay, areax)
      topleft = world.gfm(areay-1, areax)
      topright = world.gfm(areay-1, areax+1)
      bottomright = world.gfm(areay, areax+1)
      offsetx = inx
      offsety = 50+iny
    if quadrant == 2: # top left
      topleft = world.gfm(areay, areax)
      topright = world.gfm(areay, areax+1)
      bottomleft = world.gfm(areay+1, areax)
      bottomright = world.gfm(areay+1, areax+1)
      offsetx = inx
      offsety = iny
    topleft.generate_render()
    topright.generate_render()
    bottomleft.generate_render()
    bottomright.generate_render()
    
    skin=[part1+part2 for part1, part2 in zip(topleft.render, topright.render)]
    color=[part1.replace('\n','')+part2.replace('\n','') for part1, part2 in zip(topleft.color, topright.color)]
 
    skin+=[part1+part2 for part1, part2 in zip(bottomleft.render, bottomright.render)]
    color+=[part1.replace('\n','')+part2.replace('\n','') for part1, part2 in zip(bottomleft.color, bottomright.color)]
    
    self.disp_data = []
    sd=10 # shine distance
    vs=sd*2+1 # view size
    game_extra.append(color)
    for ny in range(vs):
      self.disp_data.append([])
      for nx in range(vs):
        a=sd-nx
        b=sd-ny
        csq=a*a+b*b
        fy = ny+offsety-sd
        fx = nx+offsetx-sd
        if csq>=sd*sd:self.disp_data[ny].append(esq.deft_bg+esq.white+"+-")
        else:
          game_extra.append(fx)
          self.disp_data[ny].append(
            esq.black_bg+topleft.ctc(color[fy][fx])+skin[fy][fx*2:fx*2+2]
          )
    self.disp_data[sd][sd]=esq.black_bg+esq.cyan+self.player_face
    