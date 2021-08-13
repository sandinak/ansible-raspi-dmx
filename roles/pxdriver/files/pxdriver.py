#!/usr/bin/env python3

import getopt
import textwrap
import sys
from ola.ClientWrapper import ClientWrapper
import board
import neopixel
import daemon

__author__ = 'branson@sandsite.org'

count = 17
universe = 0
foreground = True

pixels = neopixel.NeoPixel(board.D18, count, auto_write=False)
type = 'rgb'
lastpx = []


def NewData(data):
  global lastpx
  if (data != lastpx):
    for i in range(0, count):
      dmx_i=i*3
      pixels[i] = data[dmx_i:(dmx_i+3)]
    pixels.show()
  lastpx=data


def Usage():
  print(textwrap.dedent("""
  Usage: ola_recv_dmx.py --universe <universe>

  Display the DXM512 data for the universe.

  -h, --help                Display this help message and exit.
  -u, --universe <universe> Universe number.
  -p, --pixels <count>      Pixel Count."""))



def run():

  wrapper = ClientWrapper()
  client = wrapper.Client()
  client.RegisterUniverse(universe, client.REGISTER, NewData)
  wrapper.Run()

def main():
  global universe, count
  try:
      opts, args = getopt.getopt(sys.argv[1:], "hfu:p:", ["help", "universe="])
  except getopt.GetoptError as err:
    print(str(err))
    Usage()
    sys.exit(2)

  for o, a in opts:
    print(o,a)
    if o in ("-h", "--help"):
      Usage()
      sys.exit()
    elif o in ("-u", "--universe"):
      universe = int(a)
    elif o in ("-p", "--pixels"):
      count = int(a)
    elif o in ("-f", "--foreground"):
      foreground = true

  if not foreground:
    with daemon.DaemonContext():
      run()
  else: 
    run()

  sys.exit(0)

if __name__ == "__main__":
  main()