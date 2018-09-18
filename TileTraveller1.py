#First we create the file map from 1,1 to 3,3
#Then make possible moves for each tile
#Request the user for an input, wich should be a destination
#Respond to that input.(if it is not a valid input we let the user know then we re-request an input)
#If player reaches 3,3 we print out "victory!", and then exit the program


x=1
y=1
player_start = (x,y)

player_location = player_start

while player_location != (3,1):
    if player_location == (1,1) or player_location == (2,1):
        print("You can travel: (N)orth.")
        valid_direction = "n" or "N"
        direction = str(input("Directions: "))
    elif player_location == (1,2):
        print("You can travel: (N)orth or (S)outh or (W)est.")
        valid_direction = "n" or "s" or "w" or "N" or "S" or "W"
        direction = str(input("Directions: "))
    elif player_location == (2,2) or player_location == (3,3):
        print("You can travel: (S)outh or (W)est.")
        valid_direction = "s" or "w" or "S" or "W"
        direction = str(input("Directions: "))
    elif player_location == (1,3):
        print("You can travel: (S)outh or (E)ast. ")
        valid_direction = "s" or "w" or "S" or "W"
        direction = str(input("Directions: "))
    elif player_location == (2,3):
        print("You can travel: (E)ast or (W)est.")
        valid_direction = "e" or "w" or "E" or "W"
        direction = str(input("Directions: "))
    elif player_location == (3,2):
        print("You can travel: (N)orth or (S)outh.")
        valid_direction = "n" or "s" or "N" or "S"
        direction = str(input("Directions: "))

    if (direction == str("n") or direction == str("N")) and (valid_direction == "n" or valid_direction == "N"):
        player_location = (x+0,y+1)
    elif (direction == str("s") or direction == str("S")) and (valid_direction == "s" or valid_direction == "S"):
        player_location = (x+0,y-1)
    elif (direction == str("e") or direction == str("E")) and (valid_direction == "e" or valid_direction == "E"):
        player_location = (x+1,y+0)
    elif (direction == str("w") or direction == str("W")) and (valid_direction == "w" or valid_direction == "W"):
        player_location = (x-1,y+0)
    else:
        print("Not a valid direction!")
        direction = str(input("Directions: "))
else:
    print("Victory!")
    exit








