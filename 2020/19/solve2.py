#!/usr/bin/env python

import collections
import math
import os
import re
import sys
sys.path.append( os.path.abspath( ".." ) )

import common


chunks = common.read_chunks( "sample.txt" )
rules = {}
for rule in chunks[ 0 ]:
    tokens = rule.split( ":" )
    rule_id = int( tokens[ 0 ] )
    if "\"" in tokens[ 1 ]:
        rules[ rule_id ] = tokens[ 1 ].strip()[ 1 : -1 ]
    else:
        tokens = tokens[ 1 ].split( "|" )
        rules[ rule_id ] = []
        for token in tokens:
            ids = [ int( x ) for x in token.strip().split( " " ) ]
            rules[ rule_id ].append( ids )

rules[  8 ] = [ [ 42 ], [ 42, 8 ] ]
rules[ 11 ] = [ [ 42, 31 ], [ 42, 11, 31 ] ]
print( rules[8])
print( rules[11])

def matches( s, index, rule_id, callstack ):
    if index >= len( s ):
        return False, 0
    if isinstance( rules[ rule_id ], str ):
        return s[ index ] == rules[ rule_id ], 1
    #if callstack > 10000000:
     #   return False, 0
    
    for subset in rules[ rule_id ]:
        index2 = index
        for r in subset:
            flag, delta = matches( s, index2, r, callstack + 1 )
            if not flag:
                break
            
            index2 += delta
        
        if not flag:
            continue
        return True, index2 - index
    return False, 0


count = 0
for index, line in enumerate( chunks[ 1 ] ):
    print( index, line )
    flag, length = matches( line, 0, 0, 0 )
    if flag and length == len( line ):
        print("MATCH")
        count += 1
print( count )