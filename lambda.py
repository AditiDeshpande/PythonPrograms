makharTypes = [
    {"name" : "Sinhasan" , "Make" : "Cardboard"},
    {"name" : "Mandir Pattern" , "Make" : "MDF + Velvet"},
    {"name" : "Saraswati Design" , "Make" : "MDF + Paint"}
]

makharTypes.sort(key = lambda makharTypes: makharTypes["name"])
#lambda input / parameter to function : output

print(makharTypes)


#Output foll is sorted by make
# [{'name': 'Sinhasan', 'Make': 'Cardboard'},
# {'name': 'Saraswati Design', 'Make': 'MDF + Paint'},
# {'name': 'Mandir Pattern', 'Make': 'MDF + Velvet'}]

#Output foll is sorted by name using lambda function
# [{'name': 'Mandir Pattern', 'Make': 'MDF + Velvet'},
#  {'name': 'Saraswati Design', 'Make': 'MDF + Paint'},
#  {'name': 'Sinhasan', 'Make': 'Cardboard'}]
