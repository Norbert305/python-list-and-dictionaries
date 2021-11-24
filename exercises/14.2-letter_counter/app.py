par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

counts = {}
#your code go here:
par = par.lower()
for i in par:
    
    if i != " ":
        if i in counts:  #wont change structure
            counts[i] += 1

        if i not in counts:         #will change structure
            counts[i] = 1
    
    
    
    
        
        print(counts)

# loop through it
#if statement should check if element is in counts. 
# if its in counts I should sum 1 to it
# if not otherwise add it to counts. 
