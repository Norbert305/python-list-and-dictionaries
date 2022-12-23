par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

counts = {}
#your code go here:

def letter_counter(par):

    par = par.replace(" ","")
    for i in range(len(par)):

        key = par[i]

        key = key.lower()

        if key in counts:
            counts[key] += 1

        else:
            counts[key] = 1

    return counts

print(letter_counter(par))
