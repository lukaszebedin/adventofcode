#!/usr/bin/env python

with open( "data.txt" ) as file_handle:
  data = [ line.strip() for line in file_handle.readlines() ]
passports = [ {} ]
for line in data:
  if len( line ) == 0:
    passports.append( {} )
    continue

  tokens = [ item.strip() for item in line.split( " " ) ]
  for token in tokens:
    items = [ item.strip() for item in token.split( ":" ) ]
    passports[ -1 ][ items[ 0 ] ] = items[ 1 ]

fields = [ "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid" ]
def valid( passport ):
  return all( [ f in passport.keys() for f in fields ] )

valids = [ passport for passport in passports if valid( passport ) ]
print( len( valids ) )
