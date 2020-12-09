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
    break

for index in range( len( lines ) ):
  for l in range( 2, len( lines ) - index ):
    s = sum( lines[ index : index + l ] )
    if s > value:
      break
    if s == value:
      v1 = min( lines[ index : index + l ] )
      v2 = max( lines[ index : index + l ] )
      print( v1 + v2 )