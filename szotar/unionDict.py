workers = {
    "name":"Jani",
    "age":30,
    "active":True,
    "city":"Vác"
}

projects01 = {

    "projectName":"Banánszedés",
    "status":"Folyamatban",
    "priority":4
}

workers.update( projects01 )

print( workers )