#!/usr/bin/env python

import collections
import os
import sys
sys.path.append( os.path.abspath( ".." ) )

import common


def can_hold_recursively( query, values, can_hold ):
  if query in values:
    return True
  for value in values:
    if can_hold_recursively( query, can_hold[ value ], can_hold ):
      return True
  return False

lines = common.read_lines( "data.txt" )

query_color = "shiny gold"

can_hold = collections.defaultdict( list )
for line in lines:
  tokens  = line.split( " " )
  query   = " ".join( tokens[ :2 ] )
  content = zip( tokens[ 4::4 ], tokens[ 5::4 ], tokens[ 6::4 ], tokens[ 7::4 ] )
  can_hold[ query ] = []
  for number, prefix, color, bag in content:
    can_hold[ query ].append( " ".join( [ prefix, color ] ) )

count = 0
for key, values in can_hold.items():
  if can_hold_recursively( query_color, values, can_hold ):
    count += 1

print( count )

