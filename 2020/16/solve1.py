#!/usr/bin/env python

import collections
import math
import os
import re
import sys
sys.path.append( os.path.abspath( ".." ) )

import common

def matches_any( field_to_interval, value ):
    for name, intervals in field_to_interval.items():
        for lo, hi in intervals:
            if value < lo or value > hi:
                continue
            return True
    return False

lines = common.read_lines( "data.txt" )

index     = lines.index( "" )
rules     = lines[ :index ]
lines     = lines[ index + 1: ]
index     = lines.index( "" )
my_ticket = lines[ 1:index ]
tickets   = lines[ index + 2: ]

field_to_interval = {}
for rule in rules:
    tokens = rule.split( ":" )
    name   = tokens[ 0 ]
    ranges = tokens[ 1 ].split( " " )[ 1::2 ]
    ranges = [ r.split( "-" ) for r in ranges ]
    ranges = [ ( int( a ), int( b ) ) for a, b in ranges ]
    field_to_interval[ name ] = ranges

count = 0
for ticket in tickets:
    t = [ int( x ) for x in ticket.split( "," ) ]
    flags = [ matches_any( field_to_interval, x ) for x in t ]
    for flag, value in zip( flags, t ):
        if not flag:
            count += value
print( count )
