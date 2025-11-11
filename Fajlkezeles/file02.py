

print( "Fájl beolvasása....")

file = open( "dolgozok100.txt", "r", encoding="utf8" )
row = file.readline()
rowList = []

while( row ):

    row = file.readline()
    rowSp = row.split( ":" )
    
    if( len( rowSp ) > 1 ):
    
        rowList.append( rowSp )
  
counter = 0  
for i in rowList:
    
    counter += 1
    
print( "Dolgozók létszáma: {:>15}".format(counter ))