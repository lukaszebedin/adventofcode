#!/usr/bin/env python

import collections
import math
import os
import re
import sys
sys.path.append( os.path.abspath( ".." ) )

import common


def eval( line ):
    value = 0
    op    = "add"
    while True:
        line = line.strip()
        if len( line ) == 0:
            break

        if line.startswith( "(" ):
            v, line = eval( line[ 1: ] )

            if op == "add":
                value += v
            else:
                value *= v
            continue
        if line.startswith( ")" ):
            line = line[ 1: ]
            break

        if line.startswith( "+" ):
            op = "add"
            line = line[ 1: ]
            continue        
        
        if line.startswith( "*" ):
            op = "mul"
            line = line[ 1: ]
            continue
        
        v = int( re.compile( "(\d+)" ).match( line ).group( 1 ) )
        line = line[ len( str( v ) ): ]
        if op == "add":
            value += v
        else:
            value *= v

    return value, line

    

lines = common.read_lines( "data.txt" )
sumr = 0
for line in lines:
    r, v = eval( line )
    sumr += r

print( sumr )

