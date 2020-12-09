#!/usr/bin/env python

import collections
import os
import sys
sys.path.append( os.path.abspath( ".." ) )

import common

lines = common.read_lines( "data.txt" )
lines = [ int( x ) for x in lines ]

for index, value in enumerate( lines[ 25: ] ):
  preamble = lines[ index : index + 25 ]
  valid = False
  for num in preamble:
    if value - num in preamble and num != value - num:
      valid = True
      break
  
  if not valid:
    print( value )
    break