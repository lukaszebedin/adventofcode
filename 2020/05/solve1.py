#!/usr/bin/env python

def decode_str( s, ch_one ):
  value = 0
  for ch in s:
    value = value * 2
    if ch == ch_one:
      value += 1
  return value

with open( "data.txt" ) as file_handle:
  data = [ line.strip() for line in file_handle.readlines() ]

ids = []
for line in data:
  row = decode_str( line[ :7 ], "B" )
  col = decode_str( line[ 7: ], "R" )
  seat_id = row * 8 + col
  ids.append( seat_id )

print( max( ids ) )

