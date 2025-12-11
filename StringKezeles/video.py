file = open( "video.txt", "r", encoding="utf-8")
text = file.readlines()

sample = input( "Szövegrész: " )
counter = 0
for row in text:
	counter += row.count( sample )
# ~ if( len( sample ) != 1 ):
	# ~ for row in text:
		# ~ counter += row.count( sample )
# ~ else:
	# ~ for row in text:
		# ~ for spell in row:
			# ~ if( spell == sample ):
				# ~ counter += 1
		
print( counter )
