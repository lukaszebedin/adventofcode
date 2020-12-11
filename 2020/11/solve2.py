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
    for dx, dy in [ ( -1, -1 ), ( -1, 0 ), ( -1, +1 ), ( 0, -1), ( 0, +1 ), ( +1, -1 ), ( +1, 0 ), ( +1, +1 ) ]:
        sx = x
        sy = y
        occupied = False
        while True:
            sx += dx
            sy += dy
            if sx < 0 or sy < 0 or sx >= w or sy >= h:
                break
            if state[ sy ][ sx ] == "#":
                occupied = True
                break
            if state[ sy ][ sx ] == "L":
                occupied = False
                break
        if occupied:
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
            elif current[ y ][ x ] == "#" and n >= 5:
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