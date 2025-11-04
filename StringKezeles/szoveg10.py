import re

number = input( "Szám: " )

while( not (re.match( "[0.-9.]+$", number ))):

	print( "Hiba!" )
	number = input( "Szám: " )

print( "Rendben" )
# ~ numberConv = int( number )
# ~ print( type( numberConv ) )
