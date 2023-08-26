# Move Between Rooms Milestone - Mason Smith

# A dictionary for the simplified dragon text game
# The dictionary links a room to other rooms.
rooms = {
    'Great Hall': {'South': 'Bedroom'},
    'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
    'Cellar': {'West': 'Bedroom'}
}

# A tuple for valid directions
valid_direction = ('North', 'East', 'South', 'West')

# A dictionary for outputs
outputs = {
    'invalid_command': 'Your command is not valid. Please try again.'
}


# Quality of life functions
# Function to italicize text
def italicize(word):
    word = '\x1B[3m' + word + '\x1B[0m'
    return word


# A function to print a line
def print_line():
    print('_' * 70)


# A function to print the current room
def print_room(room):
    print('You are currently in the {}'.format(room))
    print_room_doors(room)


# A function to print out the commands
def print_commands():
    print_line()
    print('To change rooms type {} followed by a direction (North, East, South, or West)'.format(italicize('go')))
    print('For example: {}'.format(italicize('go North')))
    print('Or if you would like to close the game please type {}'.format(italicize('exit')))
    print_line()
    return


# A function to print the possible directions
def print_room_doors(room):
    # Building a list of possible directions based off of the dictionary
    possible_directions = []
    for direction in rooms[room]:
        possible_directions.append(direction)
    # Checking to length of the list in order to format the output
    if len(possible_directions) == 1:
        print('There is a door to the {}'.format(possible_directions[0]))
    elif len(possible_directions) == 2:
        print('There are doors to the {} and the {}'.format(possible_directions[0], possible_directions[1]))
    elif len(possible_directions) == 3:
        print('There are doors to the {}, the {}, and the {}'.format(possible_directions[0], possible_directions[1],
                                                                     possible_directions[2]))
    else:
        print('You can go in any direction!')


# A function to check that the command is two words, with the first word being go, and the second word being a valid
# direction
def valid_command(command):
    command_words = command.split()
    if len(command_words) == 2:
        if command_words[0] == 'go':
            if command_words[1] in valid_direction:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


# A function to check if there is a door in a direction
# If a door is present there then return the new room location
# If a door is not there then return the current room
def change_room(command, room):
    # Splicing the string to get the direction
    command_words = command.split()
    direction = command_words[1]
    # If the room has a door in that direction
    if direction in rooms[room]:
        # Return the room associated with that direction
        return rooms[room][direction]
    # If the room does not have a door in that direction
    else:
        # Return the current room
        print("There isn't a door on the {} wall!".format(direction))
        return room


# Setting starting room and beginning the gameplay loop
current_room = 'Cellar'
print_commands()
help_message = True
new_room = False
print_room(current_room)
while current_room != 'exit':
    # Informing the user of the help command
    if help_message:
        print('For help type {}. To get rid of this message type {}'.format(italicize('help'), italicize('stop help')))
    user_command = str(input())
    # Processing user command
    if 'exit' in user_command:
        current_room = 'exit'
    elif 'stop help' in user_command:
        help_message = False
        print_room(current_room)
    elif 'help' in user_command:
        print_commands()
        print_room(current_room)
    else:
        if valid_command(user_command):
            # Setting a temporary room check variable to see if the player is changing rooms
            room_check = current_room
            current_room = change_room(user_command, current_room)
            if room_check != current_room:
                new_room = True
        else:
            print((italicize(outputs['invalid_command'])))
    # Printing a message if the player entered a new room
    if new_room:
        print('You walk into the {}'.format(current_room))
        print_room_doors(current_room)
        new_room = False

print('Thanks for playing! :)')
