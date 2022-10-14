import parts.intro as intro
from parts.esq import *
from parts.game_ import *
from parts.world_ import *
from parts.animations import cutscene
intro.go()
print(esq.clear+esq.deft_bg)
cutscene("start")

acc_time = 0
total_time = 0
leftovers=""

sight = []

scrib = []

v = view()
v.reset_disp()
w = world()

cmd_count=0
while True:
  print(end=esq.top+esq.reset)
  for row in v.disp_data:
    print("".join(row))
  a=get_input(esq.blue+"user input ->", leftovers)
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
  if input in ["hit the flashlight"]:
    scrib.append(f"{esq.magenta}* W H A C K ! *")
    v.reset_disp()
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
    scrib=scrib[1:len(scrib)]
  for i, line in enumerate(reversed(scrib)):
    if not i%2:
      print(end=esq.italic+esq.clearline+line, flush=True)
    else:
      print(esq.reset+esq.sdown+esq.sup+esq.right*21+esq.yellow+"| "+esq.italic+line)
