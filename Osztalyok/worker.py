class Worker:
    
    name = "Névtelen"
    city = "Ismeretlen"
    age = 0
    
print( "Osztály:" )
print( Worker.name )
print( Worker.city )
print( Worker.age )

pali = Worker
pali.name = "Pál"
pali.city = "Vác"
pali.age = 34

print( "Objektum" )
print( pali.name )
print( pali.city )
print( pali.age )
    
    
    