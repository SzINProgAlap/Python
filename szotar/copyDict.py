projects01 = {

    "name":"Banánszedés",
    "status":"Folyamatban",
    "priority":4
}

projectCopy = projects01.copy()

print( projectCopy )

deleted = projectCopy.pop( "priority" )
print( deleted )

print( type( projectCopy ))
print( projectCopy.get( "name", "semmi" ))
