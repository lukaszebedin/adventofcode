#!/usr/bin/env python

import collections
import math
import os
import re
import sys
sys.path.append( os.path.abspath( ".." ) )

import common

lines = common.read_lines( "data.txt" )

def num_active_neighbours( cube, x, y, z ):
    count = 0
    for dx in [ -1, 0, +1 ]:
      for dy in [ -1, 0, +1 ]:
        for dz in [ -1, 0, +1 ]:
            if dx == 0 and dy == 0 and dz == 0:
                continue
            sx = x + dx
            sy = y + dy
            sz = z + dz
            if cube.get( ( sx, sy, sz ), False ):
                count += 1
    return count


cube = {}
for row, line in enumerate( lines ):
    for col, x in enumerate( line ) :
        cube[ ( 0, row, col ) ] = ( x == "#" )

for iter in range( 6 ):
    new_cube = {}
    for x in range( -20, +20 ):
      for y in range( -20, +20 ):
        for z in range( -20, +20 ):
            state = cube.get( ( x, y, z ) )
            num   = num_active_neighbours( cube, x, y, z )
            if state:
                new_cube[ ( x, y, z ) ] = ( num == 2 or num == 3 )
            else:
                new_cube[ ( x, y, z ) ] = ( num == 3 )
    cube = new_cube

count = 0
for pos, state in cube.items():
    if state:
        count += 1
print( count )