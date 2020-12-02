#!/usr/bin/env python

import sys

with open( "data.txt" ) as file_handle:
  data = file_handle.readlines()
data = [ int( item.strip() ) for item in data ]

data_set = set( data )
for x in data:
  for y in data:
    z = 2020 - x - y
    if z in data_set:
      print( x * y * z )
      sys.exit()
