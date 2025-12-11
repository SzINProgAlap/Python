projects01 = {

    "name":"Banánszedés",
    "status":"Folyamatban",
    "priority":4
}

projects02 = dict( name = "Sajtkészítés",
                   status = "Elkezdve",
                   priority = 2 )

print( projects01 )
print( projects02 )

projects01[ "start" ] = "2025-11-25"

print( projects01 )
print( projects02.get( "name" ))