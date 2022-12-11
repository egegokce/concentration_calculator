print ("Input the volume in milliliter")
volume = int(input ())
print ("Input the molecular weight of the chemical")
molecular_weight = int(input ())
print ("Input the weight in milligram")
weight = int(input ())
mol = weight / molecular_weight / volume
print ("Concentration of the solution is:  ",mol, " M")