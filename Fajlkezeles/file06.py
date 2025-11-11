
file = open( "dolgozok100.txt", "r", encoding="utf8" )
row = file.readline()
rowList = []

while( row ):

    row = file.readline()
    rowSp = row.split( ":" )
    
    if( len( rowSp ) > 1 ):
    
        rowList.append( rowSp )

gyorSalary = 0
for worker in rowList:
    
    if( worker[ 1 ] == "Győr" ):
        
        gyorSalary += int( worker[ 3 ])
    
print( "Győri fizetések: {:^20}".format( gyorSalary ))