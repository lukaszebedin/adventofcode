#!/usr/bin/env python

import collections
import os
import sys
sys.path.append( os.path.abspath( ".." ) )

import common


def sum_recursively( query, can_hold ):
  count = 1
  for value, color in can_hold[ query ]:
    count += value * sum_recursively( color, can_hold )
  return count

lines = common.read_lines( "data.txt" )

can_hold = collections.defaultdict( list )
for line in lines:
  tokens  = line.split( " " )
  query   = " ".join( tokens[ :2 ] )
  content = zip( tokens[ 4::4 ], tokens[ 5::4 ], tokens[ 6::4 ], tokens[ 7::4 ] )
  can_hold[ query ] = []
  for number, prefix, color, bag in content:
    can_hold[ query ].append( ( int( number ), " ".join( [ prefix, color ] ) ) )

query_color = "shiny gold"
print( sum_recursively( query_color, can_hold ) - 1 )

