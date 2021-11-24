def lyrics_generator(lyrics):
    my_lyrics = " "
    for i in range(len(lyrics)):
        if lyrics[i] == 1:
            my_lyrics+=" Drop the base"
        elif lyrics[i] == 0: 
            my_lyrics+=" Boom"
        elif lyrics[i] == 1 and lyrics[i-1] == 1 and lyrics[i-2] ==1:
            my_lyrics+=" !!!Break the base!!!"
        
    return my_lyrics


# Your code go above, nothing to change after this line:
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))