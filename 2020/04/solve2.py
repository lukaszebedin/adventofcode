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
  if not all( [ f in passport.keys() for f in fields ] ):
    return False
  
  byr = int( passport[ "byr" ] )
  if byr < 1920 or byr > 2002:
    return False

  iyr = int( passport[ "iyr" ] )
  if iyr < 2010 or iyr > 2020:
    return False

  eyr = int( passport[ "eyr" ] )
  if eyr < 2020 or eyr > 2030:
    return False

  hgt = passport[ "hgt" ]
  if hgt.endswith( "cm" ):
    h = int( hgt[ :-2 ] )
    if h < 150 or h > 193:
      return False
  elif hgt.endswith( "in" ):
    h = int( hgt[ :-2 ] )
    if h < 59 or h > 76:
      return False
  else:
    return False
 
  hcl = passport[ "hcl" ]
  if hcl[ 0 ] != "#":
    return False
  if len( hcl ) != 7:
    return False
  for ch in hcl[ 1: ]:
    if ch not in "1234567890abcdef":
      return False

  ecl = passport[ "ecl" ]
  if ecl not in [ "amb", "blu", "brn", "gry", "grn", "hzl", "oth" ]:
    return False

  pid = passport[ "pid" ]
  if len( pid ) != 9:
    return False
  for ch in pid:
    if ch not in "0123456789":
      return False

  return True

valids = [ passport for passport in passports if valid( passport ) ]
print( len( valids ) )
