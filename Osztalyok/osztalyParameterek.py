class Parameterek:
    
    def __init__( self, number, text ):
        
        self.number = number
        self.text = text
        

par = Parameterek( 10, "Hello" )
print( par.number )
print( par.text )