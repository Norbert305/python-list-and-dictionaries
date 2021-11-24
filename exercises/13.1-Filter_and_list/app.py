
all_names = ["Romario","Boby","Roosevelt","Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

#Your code go here:
#def name_r_function(name):
 #   if name[0] == "R":
  #      return name
#resulting_names = list(filter(name_r_function, all_names))
#print(resulting_names)

resulting_names = list(filter(lambda name: name[0] == "R", all_names))

print(resulting_names)






