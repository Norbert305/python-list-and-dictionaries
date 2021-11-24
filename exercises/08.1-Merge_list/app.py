chunk_one = [ 'Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell' ]
chunk_two = [ 'Lucas' , 'Jake','Scott','Amy', 'Molly','Hannah','Lucas']


def merge_list(list1, list2):
    #Your code go here:
    #list3 = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            #if chunk_one + chunk_two == list1 + list2:
                list3 = list1 + list2
    return list3
print(merge_list(chunk_one, chunk_two))
