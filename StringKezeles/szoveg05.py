text = "alma:körte:banán:eper"

spText = text.split( ":" )

for i in range( len( spText )):

	print( spText[ i ])
	
for gyumi in spText:

	print( gyumi )

if( "narancs" in spText ):
	
	print( "Benne van" )
	
else:
	print( "Nincs benne" )
	
print( text.find( "banán" ))
