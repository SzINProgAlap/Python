
file = open( "dolgozok100.txt", "r", encoding="utf8" )
row = file.readline()
rowList = []

while( row ):

    row = file.readline()
    rowSp = row.split( ":" )
    
    if( len( rowSp ) > 1 ):
    
        rowList.append( rowSp )

sumSalary = 0
for worker in rowList:
    
    sumSalary += int( worker[ 3 ])
    
print( "Összes fizetés: {:^20}".format( sumSalary ))