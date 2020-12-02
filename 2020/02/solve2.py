#!/usr/bin/env python

with open( "data.txt" ) as file_handle:
  data = file_handle.readlines()
data = [ line.split() for line in data ]

correct = 0
for policy, letter, password in data:
  pos1, pos2 = policy.split( "-" )
  pos1 = int( pos1 ) - 1
  pos2 = int( pos2 ) - 1
  letter = letter[ 0 ]
  flag1 = ( password[ pos1 ] == letter )
  flag2 = ( password[ pos2 ] == letter )
  if flag1 and flag2:
    continue
  if flag1 or flag2:
    correct += 1
print( correct )

