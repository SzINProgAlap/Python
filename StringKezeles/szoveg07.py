number01 = 123456789	#%d
text = "Szöveg"			#%s
number02 = 20.123456789		#%f

print( "{}".format( number01 ))
print( "{:_>15}".format( number01 ))
print( "{:_<15}".format( number01 ))
print( "{:_^15}".format( number01 ))

print( "Szöveg: {1}, Szám: {0}".format(  number01, text ))
print( "Lebegőpontos: {:^15.2f}".format( number02 ))
print( "Ezredes tagolás: {:,d}".format( number01 ))
