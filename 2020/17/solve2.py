#!/usr/bin/env python

import collections
import math
import os
import re
import sys
sys.path.append( os.path.abspath( ".." ) )

import common

lines = common.read_lines( "data.txt" )

def num_active_neighbours( cube, x, y, z, w ):
    count = 0
    for dx in [ -1, 0, +1 ]:
      for dy in [ -1, 0, +1 ]:
        for dz in [ -1, 0, +1 ]:
            for dw in [ -1, 0, +1 ]:
                if dx == 0 and dy == 0 and dz == 0 and dw == 0:
                    continue
                sx = x + dx
                sy = y + dy
                sz = z + dz
                sw = w + dw
                if cube.get( ( sx, sy, sz, sw ), False ):
                    count += 1
    return count


cube = {}
for row, line in enumerate( lines ):
    for col, x in enumerate( line ) :
        cube[ ( 0, 0, row, col ) ] = ( x == "#" )

for iter in range( 6 ):
    new_cube = {}
    for x in range( -2 - iter, 2 + iter ):
      for y in range( -2 - iter, 2 + iter ):
        for z in range( -2 - iter, 11 + iter ):
            for w in range( -2 - iter, 11 + iter ):
                state = cube.get( ( x, y, z, w ) )
                num   = num_active_neighbours( cube, x, y, z, w )
                if state:
                    new_cube[ ( x, y, z, w ) ] = ( num == 2 or num == 3 )
                else:
                    new_cube[ ( x, y, z, w ) ] = ( num == 3 )
    cube = new_cube

count = 0
for pos, state in cube.items():
    if state:
        count += 1
print( count )