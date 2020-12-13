#!/usr/bin/env python

import collections
import functools
import math
import operator
import os
import sys
sys.path.append( os.path.abspath( ".." ) )

import common

lines  = common.read_lines( "data.txt" )
buses = [ ( int( item ), offset ) for offset, item in enumerate( lines[ 1 ].split( "," ) ) if item != "x" ]

buses = [ ( bus - ( offset % bus ), bus ) for bus, offset in buses ]

timestamp  = 0
multiplier = buses[ 0 ][ 1 ]
for bus in buses[ 1: ]:
    while ( ( timestamp % bus[ 1 ] ) != bus[ 0 ] ):
        timestamp += multiplier
    multiplier *= bus[ 1 ]

print( timestamp )