class esq:
  # bg
  black_bg = '\x1b[40m'
  deft_bg = '\x1b[49m'
  # colors
  black = '\x1b[30m'
  red = '\x1b[31m'
  green = '\x1b[32m'
  yellow = '\x1b[33m'
  blue = '\x1b[34m'
  magenta = '\x1b[35m'
  cyan = '\x1b[36m'
  white = '\x1b[37m'
  gray = '\x1b[90m'
  bright_red = '\x1b[91m'
  bright_green = '\x1b[92m'
  bright_yellow = '\x1b[93m'
  bright_blue = '\x1b[94m'
  bright_magenta = '\x1b[95m'
  bright_cyan = '\x1b[96m'
  bright_white = '\x1b[97m'
  #special!
  crossout = "\033[9m"
  reset = "\033[0m"
  italic = "\033[3m"
  lined = "\033[4m"
  #
  top = "\033[H"

  up  = "\033[1A"
  down = "\033[1B"
  right = "\033[1C"
  left = "\033[1D"

  sup = "\033[1F"
  sdown = "\033[1E"

  def goto(x, y):return"\033[%s;%sH"%(y,x)
  def line(y):return"\033[%sG"%y

  # clear
  clear = "\033[2J"
  clearline = "\033[2K"