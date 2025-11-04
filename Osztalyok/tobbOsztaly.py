class Worker:

    def __init__( self ):
        
        self.name = None
        self.age = None
    
class Employee:
    
    def __init__( self ):
        
        self.name = None
        self.age = None
        
w = Worker()
w.name = "Sanyi"
w.age = 23

e = Employee()
e.name = "Pityu"
e.age = 32

print( w.name )
print( w.age )
print( e.name )
print( e.age )