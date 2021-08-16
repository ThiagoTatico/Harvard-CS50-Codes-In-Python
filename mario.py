# Build Mario's ladder

from cs50 import get_int
# -----------------------------------------

# Asks for a size between 1 and 8
while True:
    height = get_int("Height: ")
    
    if height >= 1 and height <= 8:
        break

# Making the ladders ----------------------
for reps in range(height):
    
    for space in range(height - reps - 1):
        print(" ", end="")

    for hashtag in range(reps + 1):
        print("#", end="")

    print("  ", end="")

    for hashtag in range(reps + 1):
        print("#", end="")
    
    print("")