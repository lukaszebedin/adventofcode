#!/usr/bin/env python

import collections
import math
import os
import re
import sys
sys.path.append( os.path.abspath( ".." ) )

import common

#values = [ 0, 3, 6 ]
values = [ 9, 3, 1, 0, 8, 4 ]
while True:
    if len( values ) == 2020:
        break
    q = values[ -1 ]
    if values.count( q ) == 1:
        values.append( 0 )
    else:
        last = max( loc for loc, val in enumerate( values[ :-1 ] ) if val == q )
        values.append( len( values ) - last - 1 )
print( values[ -1 ] )