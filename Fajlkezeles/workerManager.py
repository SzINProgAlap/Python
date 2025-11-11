from worker import Worker

class WorkerManager:
    
    def __init__( self ):
        
        self.workerList = []
    
    def controller( self ):
        
        print( "1. feladat: Fájl beolvasása" )
        readSuccess = self.readFile()
        if( readSuccess ): print( "Sikeres beolvasás\n" )
        
        print( "2. feladat: Dolgozók számlálása")
        workers = self.countWorkers()
        print( "Dolgozók létszáma: {:^10}\n".format( workers ))
        
    def readFile( self ):
        
        file = open( "dolgozok100.txt", "r", encoding="utf8" )
        row = file.readline()
        
        while( row ):
    
            row = file.readline()
            rowSp = row.split( ":" )
            if( len( rowSp ) > 1 ):
            
                worker = Worker( rowSp[ 0 ], rowSp[ 1 ], rowSp[ 2 ], rowSp[ 3 ],
                                rowSp[ 4 ], rowSp[ 5 ], rowSp[ 6 ])
                
                self.workerList.append( worker )
        
        return True      

    def countWorkers( self ):
        
        counter = 0
        for worker in self.workerList:
            
            counter += 1
        
        return counter    
            
manager = WorkerManager()
manager.controller()           
"""
0. fájl beolvasás 
1. dolgozók számolása
2. Szegedi dolgozók létszáma
3. Budapesti dolgozók fizetése
4. Legtöbbet kereső ember
5. Hányan nem kapnak jutalmat
6. Győri dolgozók fizetésének az átlaga
7. Fájlba írni az átlagot
"""