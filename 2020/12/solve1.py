#!/usr/bin/env python

import collections
import math
import os
import sys
sys.path.append( os.path.abspath( ".." ) )

import common

lines = common.read_lines( "data.txt" )
rot   = 0
x     = 0
y     = 0

for line in lines:
    if line.startswith( "F" ):
        while rot < 0:
            rot += 4
        rot = rot % 4
        if rot == 0:
            line = "E" + line[ 1: ]
        if rot == 1:
            line = "S" + line[ 1: ]
        if rot == 2:
            line = "W" + line[ 1: ]
        if rot == 3:
            line = "N" + line[ 1: ]
    if line.startswith( "N" ):
        y += int( line[ 1: ] )
    if line.startswith( "S" ):
        y -= int( line[ 1: ] )
    if line.startswith( "W" ):
        x -= int( line[ 1: ] )
    if line.startswith( "E" ):
        x += int( line[ 1: ] )
    if line.startswith( "L" ):
        rot -= int( line[ 1: ] ) // 90
    if line.startswith( "R" ):
        rot += int( line[ 1: ] ) // 90

print( abs( x ) + abs( y ) )