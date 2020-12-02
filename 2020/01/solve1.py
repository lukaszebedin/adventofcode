#!/usr/bin/env python

import sys

with open( "data.txt" ) as file_handle:
  data = file_handle.readlines()
data = [ int( item.strip() ) for item in data ]

data_set = set( data )
for x in data:
  if 2020 - x in data_set:
    print( x * ( 2020 - x ) )
    sys.exit()
