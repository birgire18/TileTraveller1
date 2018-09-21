# https://github.com/birgire18/TileTraveller1
#First we create the file map from 1,1 to 3,3 by using numbers from 1 to 9 to name the tiles
#Then make possible moves for each tile
#Request the user for an input, wich should be a destination
#Respond to that input.(if it is not a valid input we let the user know then we re-request an input)
#If player reaches 3,1 (tile number 7) we print out "victory!", and then exit the program

def information(player_location):
    if player_location == 1 or player_location == 4:            #In these if/elif sentences I'm putting an value for each tile
       return print("You can travel: (N)orth.")
    elif player_location == 2:
       return print("You can travel: (N)orth or (E)ast or (S)outh.")
    elif player_location == 5 or player_location == 9:                      
       return print("You can travel: (S)outh or (W)est.")
    elif player_location == 3:
       return print("You can travel: (E)ast or (S)outh.")
    elif player_location == 6:
       return print("You can travel: (E)ast or (W)est.")
    elif player_location == 8:
       return print("You can travel: (N)orth or (S)outh.")

def movement(direction, player_location):
    if direction == "n" and (player_location in (1, 2, 4 , 8)):
        player_location += 1
    elif direction == "s" and (player_location in (2, 3, 5, 8, 9)):    
        player_location -= 1
    elif direction == "e" and (player_location in (2, 3, 6)):          
        player_location += 3
    elif direction == "w" and (player_location in (5, 6 ,9)):
        player_location -= 3
    return player_location

player_location = 1


while player_location != 7:            # While the players location isn't on the victory tile the loop keeps going
    t_or_f = True                       
    information(player_location)       
    while t_or_f:                                                          # This while loop keeps going until the player inserts a valid value
        direction = str(input("Direction: ").lower())
        old_player_location = player_location
        player_location = movement(direction, player_location)
        if player_location == old_player_location:                      # If the player doesn´t insert an value that goes with his tile posistion
            print("Not a valid direction!")                                # then it will print out "Not a valid direction!" and allows him to try again
            continue
        t_or_f = False
    
else:
    print("Victory!")
    exit