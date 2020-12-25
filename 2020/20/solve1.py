#!/usr/bin/env python

import collections
import math
import os
import re
import sys
sys.path.append( os.path.abspath( ".." ) )

import common


chunks = common.read_chunks( "data.txt" )

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
                    
def matches( s, index, rule_id ):
    if isinstance( rules[ rule_id ], str ):
        return s[ index ] == rules[ rule_id ], 1
    
    for subset in rules[ rule_id ]:
        index2 = index
        for r in subset:
            flag, delta = matches( s, index2, r )
            if not flag:
                break
            
            index2 += delta
        
        if not flag:
            continue
        return True, index2 - index
    return False, 0


count = 0
for line in chunks[ 1 ]:
    flag, length = matches( line, 0, 0 )
    if flag and length == len( line ):
        count += 1
print( count )