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

def matching_fields( field_to_interval, value ):
    fields = []
    for name, intervals in field_to_interval.items():
        matches = False
        for lo, hi in intervals:
            if value >= lo and value <= hi:
                matches = True
        if matches:
            fields.append( name )
    return fields

lines = common.read_lines( "data.txt" )

index     = lines.index( "" )
rules     = lines[ :index ]
lines     = lines[ index + 1: ]
index     = lines.index( "" )
my_ticket = [ int( x ) for x in lines[ 1].split( "," ) ]
tickets   = lines[ index + 2: ]

field_to_interval = {}
for rule in rules:
    tokens = rule.split( ":" )
    name   = tokens[ 0 ]
    ranges = tokens[ 1 ].split( " " )[ 1::2 ]
    ranges = [ r.split( "-" ) for r in ranges ]
    ranges = [ ( int( a ), int( b ) ) for a, b in ranges ]
    field_to_interval[ name ] = ranges

valids = []
for ticket in tickets:
    t = [ int( x ) for x in ticket.split( "," ) ]
    flags = [ matches_any( field_to_interval, x ) for x in t ]
    if all( flags ):
        valids.append( t )

assignments = [ [] for _ in range( len( my_ticket ) ) ]
for index in range( len( my_ticket ) ):
    fields = common.flatten( [ matching_fields( field_to_interval, valid[ index ] ) for valid in valids ] )
    for name in field_to_interval.keys():
        if fields.count( name ) == len( valids ):
            assignments[ index ].append( name )

final = {}
while True:
    if len( final ) == len( my_ticket ):
        break
    for index, ass in enumerate( assignments ):
        if len( ass ) == 1:
            key = ass[ 0 ]
            final[ key ] = index
            for a in assignments:
                if key in a:
                    a.remove( key )
            break

count = 1
for name, index in final.items():
    if name.startswith( "departure" ):
        count *= my_ticket[ index ]
print( count )