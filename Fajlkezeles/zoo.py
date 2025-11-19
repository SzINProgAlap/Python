from animal import Animal

class Zoo:
    
    def __init__( self ):
        
        self.animalList =  []
    
    def controller( self ):
        
        self.readFile()
        self.countType()
        carnivore = self.carnivore()
        print( "Összes húsevők száma: {:^10}".format(carnivore) )
    
    def readFile( self ):
        
        file = open( "allatkert.csv", "r", encoding="utf-8")
        row = file.readline()
        
        while( row ):
            
            row = file.readline()
            rowSp = row.split( ";" )
            
            if( len( rowSp ) > 1 ):
                
                animal = Animal( rowSp[ 0 ], rowSp[ 1 ], rowSp[ 2 ], rowSp[ 3 ], rowSp[ 4 ])
                self.animalList.append( animal )
     
    def countType( self ):
        
        counter = 0
        for animal in self.animalList:
            
            if( animal.type == "Emlős"  ):    
                
                counter += 1
                
        print( counter )   
         
    def carnivore( self ):
        counter = 0
        for animal in self.animalList:
            if animal.food ==  "Hús":
                counter += 1
        return counter
                   
zoo = Zoo()
zoo.controller()

"""
1. állatok számlálása
2. emlősök számlálása
3. Hány állat eszik húst?
4. Összes hússzükséglet / nap
5. Mennyibe kerül a madarak fenntartása / év
6. Melyik állat eszi a legtöbb húst / nap?
7. Melyi állat a legdrágább / nap?        
"""