class Employee:
    
    def __init__( self ):
        
        self.__name = ""
                
    def setName( self, name ):
        
        self.__name = name

    def getName( self ):
        
        return self.__name
   
sanyi = Employee()     
# print( "_ " + sanyi.name + " _" )
print( "_ " + sanyi.getName() + " _")


sanyi.setName( "Sándor" )
#print( "_ " + sanyi.name + " _" )
print( "_ " + sanyi.getName() + " _")