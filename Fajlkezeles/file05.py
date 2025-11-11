
file = open( "dolgozok100.txt", "r", encoding="utf8" )
row = file.readline()
rowList = []

while( row ):

    row = file.readline()
    rowSp = row.split( ":" )
    
    if( len( rowSp ) > 1 ):
    
        rowList.append( rowSp )

counter = 0
for worker in rowList:
    
    if( worker[ 1 ] == "Miskolc" ):
        
        counter += 1
    
print( "Miskolci dolgozók: {:^20}".format( counter ))