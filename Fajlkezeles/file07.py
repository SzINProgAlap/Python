
file = open( "dolgozok100.txt", "r", encoding="utf8" )
row = file.readline()
rowList = []

while( row ):

    row = file.readline()
    rowSp = row.split( ":" )
    
    if( len( rowSp ) > 1 ):
    
        rowList.append( rowSp )

lajosCounter = 0
for worker in rowList:
    
    nameSp = worker[ 0 ].split( " " )
    if( nameSp[ 1 ] == "Lajos" ):
        
        lajosCounter += 1
    
print( "Lajosok száma: {:^20}".format( lajosCounter ))