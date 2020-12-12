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
wx    = 10
wy    = 1

for line in lines:
    if line.startswith( "F" ):
        x += wx * int( line[ 1: ] )
        y += wy * int( line[ 1: ] )
    if line.startswith( "N" ):
        wy += int( line[ 1: ] )
    if line.startswith( "S" ):
        wy -= int( line[ 1: ] )
    if line.startswith( "W" ):
        wx -= int( line[ 1: ] )
    if line.startswith( "E" ):
        wx += int( line[ 1: ] )
    if line.startswith( "L" ):
        for _ in range( int( line[ 1: ] ) // 90 ):
            wx, wy = -wy,  wx
    if line.startswith( "R" ):
        for _ in range( int( line[ 1: ] ) // 90 ):
            wx, wy =  wy, -wx

print( abs( x ) + abs( y ) )