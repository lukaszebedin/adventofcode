#!/usr/bin/env python

import collections
import os
import sys
sys.path.append( os.path.abspath( ".." ) )

import common

lines = common.read_lines( "data.txt" )
lines = [ int( x ) for x in lines ]

lines = sorted( lines )
lines = [ 0 ] + lines + [ lines[ -1 ] + 3 ]

counts = [ 0 ] * len( lines )
counts[ 0 ] = 1

for index, jolts in enumerate( lines ):
    for diff in range( 1, 4 ):
        if index + diff >= len( lines ):
            continue 
        if lines[ index + diff ] - lines[ index ] <= 3:
            counts[ index + diff ] += counts[ index ]

print( counts[ -1 ] )