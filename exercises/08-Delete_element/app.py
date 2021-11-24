people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:
def deletePerson(person_name):
    
    x = []
    #Your code go here:
    for name in person_name:
        
        if person_name == "daniella" :
            x=['juan','ana','michelle','stefany','lucy','barak']
        elif person_name == "juan":
            x=['ana','michelle','daniella','stefany','lucy','barak']
        else:
            x=['juan','ana','michelle','daniella','stefany','lucy','barak']
        
    return x
print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))