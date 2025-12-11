projects01 = {

    "name":"Banánszedés",
    "status":"Folyamatban",
    "priority":4
}

print( projects01 )

del projects01[ "priority" ]
print( projects01 )

check = "start" in projects01
print( type( check ))
print( check )