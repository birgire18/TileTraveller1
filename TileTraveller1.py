#First we create the file map from 1,1 to 3,3
#Then make possible moves for each tile
#Request the user for an input, wich should be a destination
#Respond to that input.(if it is not a valid input we let the user know then we re-request an input)
#If player reaches 3,3 we print out "victory!", and then exit the program

for i in range(1, 4):
    for j in range(1, 4):
        print(i,j)
x=1
y=1
player_start = (x,y)

player_location = player_start


if direction == str("n") or direction

if player_location == (1,1) or player_location == (2,1):
    print("You can travel: (N)orth.")
    direction = str(input("Directions: "))
elif player_location == (1,2):
    print("You can travel: (N)orth or (S)outh or (W)est.")
    direction = str(input("Directions: "))
elif player_location == (2,2) or player_location == (3,3):
    print("You can travel: (S)outh or (W)est.")
    direction = str(input("Directions: "))
elif player_location == (1,3):
    print("You can travel: (S)outh or (E)ast. ")
    direction = str(input("Directions: "))
elif player_location == (2,3):
    print("You can travel: (E)ast or (W)est.")
    direction = str(input("Directions: "))
elif player_location == (3,2):
    print("You can travel: (N)orth or (S)outh.")
    direction = str(input("Directions: "))
elif player_location == (3,1):
    print("Victory!")
    exit

if direction == str("n") or direction == str("N"):
    player_location = (x+0,y+1)
elif direction == str("s") or direction == str("S"):
    player_location = (x+0,y-1)
elif direction == str("e") or direction == str("E"):
    player_location = (x+1,y+0)
elif direction == str("w") or direction == str("W"):
    player_location = (x-1,y+0)
else:
    print("Not a valid direction!")
    direction = str(input("Directions: "))








