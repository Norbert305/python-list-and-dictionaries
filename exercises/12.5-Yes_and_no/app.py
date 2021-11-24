theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:

def wiki_woko(value):

        if value == 0:
            return "woko"
        else:
            return "wiki"

new_list = list(map(wiki_woko, theBools))

print(new_list)
