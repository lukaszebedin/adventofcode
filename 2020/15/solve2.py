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
lut    = { value : index + 1 for index, value in enumerate( values[ :-1 ] ) }
while True:
    if len( values ) == 30000000:
        break
    q = values[ -1 ]
    if not q in lut:
        lut[ q ] = len( values )
        values.append( 0 )
    else:
        last = lut[ q ]
        lut[ q ] = len( values )
        values.append( len( values ) - last )
print( values[ -1 ] )