#!/usr/bin/env python

import os
import sys
sys.path.append( os.path.abspath( ".." ) )

import common


chunks = common.read_chunks( "data.txt" )

count = 0
for chunk in chunks:
  answers = common.flatten( chunk )
  count += len( set( answers ) )

print( count )

