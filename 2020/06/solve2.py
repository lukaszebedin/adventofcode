#!/usr/bin/env python

import os
import sys
sys.path.append( os.path.abspath( ".." ) )

import common


chunks = common.read_chunks( "data.txt" )

count = 0
for chunk in chunks:
  answers = set( chunk[ 0 ] )
  for line in chunk[ 1: ]:
    answers = answers.intersection( set( line ) )
  count += len( set( answers ) )

print( count )