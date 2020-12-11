#!/usr/bin/env python

import collections
import os
import sys
sys.path.append( os.path.abspath( ".." ) )

import common

current = common.read_lines( "data.txt" )
w = len( current[ 0 ] )
h = len( current )

def get_neighbours( state, x, y ):
    count = 0
    for dx in [ -1, 0, +1 ]:
        for dy in [ -1, 0, +1 ]:
            if dx == 0 and dy == 0:
                continue
            sx = x + dx
            sy = y + dy
            if sx < 0 or sy < 0 or sx >= w or sy >= h:
                continue
            if state[ sy ][ sx ] == "#":
                count += 1
    return count
 
while True:
    state = [ [ '.' ] * w for _ in range( h ) ]
    for x in range( w ):
        for y in range( h ):
            if current[ y ][ x ] == ".":
                continue
            n = get_neighbours( current, x, y )
            if current[ y ][ x ] == "L" and n == 0:
                state[ y ][ x ] = "#"
            elif current[ y ][ x ] == "#" and n >= 4:
                state[ y ][ x ] = "L"
            else:
                state[ y ][ x ] = current[ y ][ x ]
    if all( [ a == b for a, b in zip( state, current ) ] ):
        break
    current = state

count = 0
for line in current:
    count += "".join( line ).count( "#" )
print( count )