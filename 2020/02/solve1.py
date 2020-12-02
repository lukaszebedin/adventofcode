#!/usr/bin/env python

with open( "data.txt" ) as file_handle:
  data = file_handle.readlines()
data = [ line.split() for line in data ]

correct = 0
for policy, letter, password in data:
  min_count, max_count = policy.split( "-" )
  min_count = int( min_count )
  max_count = int( max_count )
  letter = letter[ 0 ]
  count = password.count( letter )
  if count >= min_count and count <= max_count:
    correct += 1
print( correct )
