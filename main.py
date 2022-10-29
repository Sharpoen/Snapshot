import parts.intro as intro
from parts.esq import *
from parts.game_ import *
from parts.world_ import *
from parts.animations import cutscene
from parts.builder import *



acc_time = 0
total_time = 0
leftovers=""

sight = []

scrib = []

v = view()
v.reset_disp()
w = world(map)
w.map[0][0].special["0,0"] = {"type":"door", "state":"open"}
w.map[0][0].special["1,0"] = {"type":"door", "state":"closed"}

  

w.map[0][0].generate_render()
w.map[0][1].generate_render()

tx=0
ty=0
r=0
c=0
while True:
  print(end=esq.top+esq.reset)
  w.map[r][c].test_render(tx, ty)
  print("use arrow keys to seek [%s][%s] -> (%s:%s, %s:%s)"%(r, c, tx, tx+14, ty, ty+14))
  pin = get_input("type 'continue' to escape\n->")
  a = pin["input"].lower()
  if a=="go north":
    ty-=1
  elif a=="go south":
    ty+=1
  elif a=="go west":
    tx-=1
  elif a=="go east":
    tx+=1
  else:
    if a=="column":
      c=(c+1)%20
      w.map[r][c].generate_render()
    elif a=="row":
      r=(r+1)%10
      w.map[r][c].generate_render()
    elif a=="continue":
      break
    print(esq.clear)
  if tx<0:
    tx=0
  if ty<0:
    ty=0
  if tx>31:
    tx=31
  if ty>31:
    ty=31
  
intro.go()
print(esq.clear+esq.deft_bg)
cutscene("start")

area = "Darkness"

cmd_count=0
while True:
  print(end=esq.top+esq.reset)
  for row in v.disp_data:
    print("".join(row))
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
  if input in ["take a picture!"]:
    scrib.append(f"{esq.magenta}* C L I C K ! *")
    v.set_disp()
  elif input in ["go north"]:
    scrib.append(w.go_north())
    v.player_face="/\\"
  elif input in ["go south"]:
    scrib.append(w.go_south())
    v.player_face="\\/"
  elif input in ["go west"]:
    scrib.append(w.go_west())
    v.player_face="<]"
  elif input in ["go east"]:
    scrib.append(w.go_east())
    v.player_face="[>"
  elif len(input.split(" "))>1:
    if input.split(" ")[0] in ["help"]:
      print(flush=True, end="not yet available"+esq.sdown+esq.sup)
      getkey()
    else:
      scrib.append(f"{esq.bright_red}Type 'help' for reference sheet.")
      scrib.append(f"{esq.bright_red}That's not a command.")
  # single word commands
  elif input in ["help"]:
    intro.crs()
    print(end=esq.clear)
  elif input in ["clear"]:
    scrib=[]
    print(end=esq.clear)
  else:
    scrib.append(f"{esq.bright_red}Type 'help' for reference sheet.")
    scrib.append(f"{esq.bright_red}That's not a command.")
  cmd_count+=1

  # scrib
  print(esq.clearline+esq.yellow+"---------------------+-----")
  if len(scrib)>10:
    scrib=scrib[len(scrib)-10:len(scrib)]
  for i, line in enumerate(reversed(scrib)):
    if not i%2:
      print(end=esq.italic+esq.clearline+line, flush=True)
    else:
      print(esq.reset+esq.sdown+esq.sup+esq.right*21+esq.yellow+"| "+esq.italic+line)
