import os
import sys
import platform
import time

def clear():
  os_name = platform.system()
  if os_name == "Windows":
    os.system("cls")
  if os_name == "Linux":
    os.system("clear")

def printscr(scrtxt="", speed=0.01, wrapspc=1, stoprnd=None):
  txtpwrap = ((" " * len(scrtxt)) * wrapspc) + scrtxt
  rnd = 0
  while True:
    clear()
    print (txtpwrap[(len(scrtxt) * wrapspc)-rnd:][0:len(scrtxt)])
    rnd += 1
    time.sleep(speed)
    try:
      if rnd > len(scrtxt) * stoprnd:
        sys.exit()
    except TypeError:
      pass
    if rnd > len(txtpwrap):
      rnd = 0
