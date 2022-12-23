people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:
people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:
def deletePerson(person_name):
    #Your code go here:

    answer = []

    for i in range(len(people)):
        if people[i] != person_name:
            answer.append(people[i])

    return answer

    


print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))