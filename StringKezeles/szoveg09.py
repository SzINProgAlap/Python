import re

text = input( "Szám: " )

if( re.match( "[A-za-z0-9@]+", text )):

	print( "Egyezik" )
	
else:
	
	print( "Hiba" )
