import parts.intro as intro
from parts.esq import *
from parts.game_ import *
from parts.world_ import *
from parts.animations import cutscene
from parts.builder import *

interface_options = []


# if input("Type '1' if on mobile, otherwise just press enter.\n>") == "1":
#   interface_options.append("on mobile")
#   print("In some situations you make need to press the send/enter button\nfor the game to accept your input.\nPress send/enter/return to continue.")
#   input()

acc_time = 0
total_time = 0
leftovers=""

sight = []

scrib = []

v = view()
v.reset_disp()
w = world(map, special_areas)

  

w.map[0][0].generate_render()
w.map[0][1].generate_render()

tx=0
ty=0
r=0
c=0
while True and "dev mode" in interface_options:
  print(end=esq.top+esq.reset)
  w.map[r][c].test_render(tx, ty)
  print("use arrow keys to seek [%s][%s] -> (%s:%s, %s:%s)"%(r, c, tx, tx+14, ty, ty+14))
  pin = get_input("type 'continue' to escape\n->", leftovers)
  a = pin["input"].lower()
  leftovers = pin["leftovers"]
  if a == "go north":
    ty-=1
  elif a == "go south":
    ty+=1
  elif a == "go west":
    tx-=1
  elif a == "go east":
    tx+=1
  else:
    if a == "column":
      c=(c+1)%20
      w.map[r][c].generate_render()
    elif a == "row":
      r=(r+1)%10
      w.map[r][c].generate_render()
    elif a == "goto":
      print(end="Column: \nRow: "+esq.sup)
      c = int(input("Column:"))
      r = int(input("Row:"))
    elif a in ["continue", "cont", "end", "quit"]:
      break
    print(esq.clear)
    print(a)
  if tx<0:
    tx=0
  if ty<0:
    ty=0
  if tx>36:
    tx=36
  if ty>36:
    ty=36
  
intro.go()
print(esq.clear+esq.deft_bg)
if not ("skip cutscenes" in interface_options):
  cutscene("start")

p = player(0, 0)

cmd_count=0
while True:
  print(end=esq.top+esq.reset)
  for row in v.disp_data:
    print("".join(row))
  a = {}
  if "on mobile" in interface_options:
    a=get_inputMobile(esq.blue+"-->")
    print(esq.up+esq.clearline)
  else:
    a=get_input(esq.blue+"-->", leftovers)
  if a["input"].lower() in ["quit", "exit"]:
    break
  leftovers = a["leftovers"]

  if a["time"]<1:
    acc_time+=1
  else:
    acc_time+=a["time"]
  total_time+=a["time"]

  # environment & monster
  while acc_time > 3:
    break
  
  # player
  input = a["input"].lower()
  # multiple word commands
  if input in ["take a picture!", "take a picture"]:
    scrib.append(f"{esq.magenta}* C L I C K ! *")
    v.set_disp(w, p.x, p.y)
  elif len(input.split(" "))>1:
    words = input.split(" ")
    if words[0] in ["help"]:
      print(flush=True, end="not yet available"+esq.sdown+esq.sup)
      getkey()
    elif words[0] in ["go"]:
      if words[1] in ["north", "south", "east", "west"]:
        scrib.append(w.move(p, words[1]))
        if words[1] == "north":
          v.player_face="/\\"
        if words[1] == "east":
          v.player_face="[>"
        if words[1] == "south":
          v.player_face="\\/"
        if words[1] == "west":
          v.player_face="<]"
      else:
        scrib.append(f"{esq.bright_red}Use north, south, east, or west.")
        scrib.append(f"{esq.bright_red}'{words[1]}' is not a direction!")
    else:
      scrib.append(f"{esq.bright_red}Type 'help' for reference sheet.")
      scrib.append(f"{esq.bright_red}That's not a command.")
  # single word commands
  elif input in ["guide", "tutorial"]:
    intro.guide1.open()
    print(end=esq.clear)
  elif input in ["help", "ref", "reference", "pause"]:
    intro.crs()
    print(end=esq.clear)
  elif input in ["clear"]:
    scrib=[]
    print(end=esq.clear)
  else:
    scrib.append(f"{esq.bright_red}That's not a command.")
    scrib.append(f"{esq.bright_red}Type 'help' for reference sheet.")
  cmd_count+=1

  # scrib
  print(esq.clearline+esq.yellow+"-----------------------------------------")
  if len(scrib)>12:
    scrib=scrib[len(scrib)-12:len(scrib)]
  for i, line in enumerate(reversed(scrib)):
    print(esq.italic+esq.clearline+esq.down+esq.sup+line, flush=True)