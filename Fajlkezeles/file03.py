
file = open( "dolgozok100.txt", "r", encoding="utf8" )
row = file.readline()
rowList = []

while( row ):

    row = file.readline()
    rowSp = row.split( ":" )
    
    if( len( rowSp ) > 1 ):
    
        rowList.append( rowSp )
  
for worker in rowList:
    
    print( worker[ 0 ] )