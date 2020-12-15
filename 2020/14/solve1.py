#!/usr/bin/env python

import collections
import math
import os
import re
import sys
sys.path.append( os.path.abspath( ".." ) )

import common

lines = common.read_lines( "data.txt" )
memory = collections.defaultdict( int )
mask_and = 0b1111111111111111111111111111111
mask_or  = 0b0000000000000000000000000000000
for line in lines:
    if line.startswith( "mask" ):
        s = line.split( "=" )[ 1 ]
        mask_and = 0b1111111111111111111111111111111
        mask_or  = 0b0000000000000000000000000000000
        for index, value in enumerate( reversed( s ) ):
            if value == "1":
                mask_or  |= ( 1 << index )
            if value == "0":
                mask_and &= ~( 1 << index )
    if line.startswith( "mem" ):
        tokens = re.split( "\[|\]|=| ", line )
        tokens = [ t for t in tokens if t ]
        value  = int( tokens[ 2 ] )
        value &= mask_and
        value |= mask_or
        memory[ int( tokens[ 1 ] ) ] = value

print( sum( memory.values() ) )