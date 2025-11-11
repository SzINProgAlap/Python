

print( "Fájl beolvasása....")

file = open( "dolgozok100.txt", "r", encoding="utf8" )
row = file.readline()

while( row ):

    row = file.readline()
    rowSp = row.split( ":" )

    print( rowSp )