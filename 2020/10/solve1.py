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
diffs = [ b - a for a, b in zip( lines, lines[ 1: ] ) ]
ones   = diffs.count( 1 )
threes = diffs.count( 3 )
print( ones * threes )