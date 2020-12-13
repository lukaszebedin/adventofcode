#!/usr/bin/env python

import collections
import math
import os
import sys
sys.path.append( os.path.abspath( ".." ) )

import common

lines     = common.read_lines( "data.txt" )
timestamp = float( lines[ 0 ] )
min_delta = 10000
solution  = -1
for item in lines[ 1 ].split( "," ):
    if item == "x":
        continue
    bus_id    = int( item )
    departure = math.ceil( timestamp / bus_id ) * bus_id
    delta     = departure - timestamp
    if delta < min_delta:
        min_delta = delta
        solution  = bus_id * delta 

print( int( solution ) )