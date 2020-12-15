#!/usr/bin/env python

import collections
import itertools
import math
import os
import re
import sys
sys.path.append( os.path.abspath( ".." ) )

import common

lines      = common.read_lines( "data.txt" )
memory     = collections.defaultdict( int )
mask_or    = 0b0000000000000000000000000000000
float_bits = []
for line in lines:
    if line.startswith( "mask" ):
        s = line.split( "=" )[ 1 ]
        mask_or     = 0b0000000000000000000000000000000
        float_bits = []
        for index, value in enumerate( reversed( s ) ):
            if value == "1":
                mask_or  |= ( 1 << index )
            if value == "X":
                float_bits.append( index )
    if line.startswith( "mem" ):
        tokens = re.split( "\[|\]|=| ", line )
        tokens = [ t for t in tokens if t ]
        addr   = int( tokens[ 1 ] )
        value  = int( tokens[ 2 ] )
        addr  |= mask_or
        subsets = [ itertools.combinations( float_bits, l ) for l in range( len( float_bits ) + 1 ) ]
        subsets = common.flatten( subsets )
        for subset in subsets:
            invert = [ x for x in float_bits if not x in subset ]
            m_or  =  sum( [ 1 << index for index in subset ] )
            m_and = ~sum( [ 1 << index for index in invert ] )
            memory[ ( addr | m_or ) & m_and ] = value

print( sum( memory.values() ) )