makharTypes = [
    {"name" : "Sinhasan" , "Make" : "Cardboard"},
    {"name" : "Mandir Pattern" , "Make" : "MDF + Velvet"},
    {"name" : "Saraswati Design" , "Make" : "MDF + Paint"}
]

def types(makharTypes):
    return makharTypes["Make"]

makharTypes.sort(key = types)

print(makharTypes)


#Output
# [{'name': 'Sinhasan', 'Make': 'Cardboard'}, 
# {'name': 'Saraswati Design', 'Make': 'MDF + Paint'},
# {'name': 'Mandir Pattern', 'Make': 'MDF + Velvet'}]
