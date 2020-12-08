#!/usr/bin/env python

import collections
import os
import sys
sys.path.append( os.path.abspath( ".." ) )

import common


acc = 0
ip  = 0
def fct_nop( i ):
  global ip
  ip += 1
def fct_acc( i ):
  global acc, ip
  acc += i
  ip += 1
def fct_jmp( i ):
  global ip
  ip += i

execute = {
  "nop" : fct_nop,
  "acc" : fct_acc,
  "jmp" : fct_jmp 
} 

lines = common.read_lines( "data.txt" )

visited = set()
while True:
  if ip in visited:
    break
  visited.add( ip )

  tokens = lines[ ip ].split( " " )
  execute[ tokens[ 0 ] ]( int( tokens[ 1 ] ) )
  
print( acc )