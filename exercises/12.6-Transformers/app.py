incomingAJAXData = [
	{ "name": 'Mario', "lastName": 'Montes' },
	{ "name": 'Joe', "lastName": 'Biden' },
	{ "name": 'Bill', "lastName": 'Clon' },
	{ "name": 'Hilary', "lastName": 'Mccafee' },
	{ "name": 'Bobby', "lastName": 'Mc birth' }
]

#Your code go here:

def my_var(name):

	return f"{name['name']} {name['lastName']}"

transformedData = list(map(my_var, incomingAJAXData))

print(transformedData)

#transformedData = list(map(lambda name: f"{name['name']} {name['lastName']}" , incomingAJAXData )) 
	
#print(transformedData)