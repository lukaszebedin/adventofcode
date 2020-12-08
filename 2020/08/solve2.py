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

def terminates( lines ):
  global acc, ip
  acc = 0
  ip  = 0
  visited = set()
  while True:
    if ip in visited:
     return False
    visited.add( ip )

    tokens = lines[ ip ].split( " " )
    execute[ tokens[ 0 ] ]( int( tokens[ 1 ] ) )
    if ip >= len( lines ):
      return True

lines = common.read_lines( "data.txt" )
for index, _ in enumerate( lines ):
  cpy = [ str( line ) for line in lines ]
  tokens = cpy[ index ].split( " " )
  if tokens[ 0 ] == "nop":
    cpy[ index ] = "jmp " + tokens[ 1 ]
  elif tokens[ 0 ] == "jmp":
    cpy[ index ] = "nop " + tokens[ 1 ]
  else:
    pass
  
  if terminates( cpy ):
    print( acc )
    break