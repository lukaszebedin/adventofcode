#!/usr/bin/env python

with open( "data.txt" ) as file_handle:
  data = file_handle.readlines()
data = [ line.strip() for line in data ]


def count_trees( data, inc_x, inc_y ):
  x = 0
  y = 0
  count = 0
  while y < len( data ):
    if data[ y ][ x ] == "#":
      count += 1
    x += inc_x
    y += inc_y
    x = x % len( data[ 0 ] )
  return count

print( count_trees( data, 3, 1 ) )