# Task 1: The for Loop DJ Set
# Using the provided genres list, write a for loop that prints out each genre with a custom message. Extend this task by adding a 
# counter that displays the number of the track before the genre.

#genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
#track = 1

#for genre in genres:
#    print(f"We're listening to track number {track}: {genre}.")
#    track += 1
#    continue



# Task 2: The Remix Artist with while
# Convert the for loop from Task 1 into a while loop. Ensure it performs the same function but also includes a condition to stop the 
# loop if a certain genre is played for instance Hip-hop.
#import random
#genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
#track = 1
#listen = ''
#while listen != 'Hip-hop':
#    listen = random.choice(genres)
#    print(f"We're listening to track number {track}: {listen}.")
#    track += 1
    
#if listen == 'Hip-hop':
#    pass
    

# Task 3: Light Show Technician Loop
# Using the range() function, loop through the genres list by index. For each genre, print out the track number and a message that the 
# light show is ready. Modify the loop to skip a genre if it's not suitable for the light show, for instance Classical genre.

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
track = 1
light_show = genres[:3]
no_light_show = genres[3:]

for genre in light_show:
    print(f"We're listening to track number {track}: {genre}. The Light Show is ready!")
    track += 1
    continue
for genre in no_light_show:
    print(f"We're listening to track number {track}: {genre}.")

    

