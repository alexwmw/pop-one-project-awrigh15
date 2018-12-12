# The Three Musketeers Game

# In all methods,
#   A 'location' is a two-tuple of integers, each in the range 0 to 4.
#        The first integer is the row number, the second is the column number.
#   A 'direction' is one of the strings "up", "down", "left", or "right".
#   A 'board' is a list of 5 lists, each containing 5 strings: "M", "R", or "-".
#        "M" = Musketeer, "R" = Cardinal Richleau's man, "-" = empty.
#        Each list of 5 strings is a "row"
#   A 'player' is one of the strings "M" or "R" (or sometimes "-").
#
# For brevity, Cardinal Richleau's men are referred to as "enemy".
# 'pass' is a no-nothing Python statement. Replace it with actual code.

def create_board():
    global board
    """Creates the initial Three Musketeers board and makes it globally
       available (That is, it doesn't have to be passed around as a
       parameter.) 'M' represents a Musketeer, 'R' represents one of
       Cardinal Richleau's men, and '-' denotes an empty space."""
    m = 'M'
    r = 'R'
    board = [ [r, r, r, r, m],
              [r, r, r, r, r],
              [r, r, m, r, r],
              [r, r, r, r, r],
              [m, r, r, r, r] ]

def set_board(new_board):
    """Replaces the global board with new_board."""
    global board
    board = new_board

def get_board():
    """Just returns the board. Possibly useful for unit tests."""
    return board

def string_to_location(s):
    """Given a two-character string (such as 'A5'), returns the designated
       location as a 2-tuple (such as (0, 4)).
       The function should raise ValueError exception if the input
       is outside of the correct range (between 'A' and 'E' for s[0] and
       between '1' and '5' for s[1]
       """
    # Take unicode value of the string's first character and minuses 65
    # to place it within range 0,5.
    # Takes 2nd character from input string and minuses 1.
    # Checks if output is legal before returning location.
    row = ord(s[0]) - 65
    column = int(s[1]) - 1
    location = (row, column)
    if not is_legal_location(location):
        raise ValueError()
    else:
        return (location)

def location_to_string(location):
    """Returns the string representation of a location.
       Similarly to the previous function, this function should raise
       ValueError exception if the input is outside of the correct range
       """
    # Reverse of previous function
    s = (chr(location[0] + 65) + str(location[1] + 1))
    if not is_legal_location(location):
        raise ValueError()
    else:
        return s

def at(location):
    """Returns the contents of the board at the given location.
    You can assume that input will always be in correct range."""
    return board[location[0]][location[1]]

def all_locations():
    """Returns a list of all 25 locations on the board."""
    locations = []
    for row in range (5):
        for column in range(5):
            locations.append((row, column))
    return locations

def adjacent_location(location, direction):
    """Return the location next to the given one, in the given direction.
       Does not check if the location returned is legal on a 5x5 board.
       You can assume that input will always be in correct range."""
    (row, column) = location
    if direction == "up":
        row -= 1
    if direction == "down":
        row += 1
    if direction == "left":
        column -= 1
    if direction == "right":
        column += 1
    return (row, column)

def is_legal_move_by_musketeer(location, direction):
    """Tests if the Musketeer at the location can move in the direction.
       You can assume that input will always be in correct range. Raises
       ValueError exception if at(location) is not 'M'"""
    if at(location) != 'M':
        raise ValueError()
    elif (is_within_board(location,direction)
            and at(adjacent_location(location,direction)) == "R"):
        return True
    else:
        return False

def is_legal_move_by_enemy(location, direction):
    """Tests if the enemy at the location can move in the direction.
       You can assume that input will always be in correct range. Raises
       ValueError exception if at(location) is not 'R'"""
    if at(location) != 'R':
        raise ValueError()
    elif (is_within_board(location,direction)
            and at(adjacent_location(location, direction)) == "-"):
        return True
    else:
        return False

def is_legal_move(location, direction):
    """Tests whether it is legal to move the piece at the location
    in the given direction.
    You can assume that input will always be in correct range."""
    if at(location) == 'M':
        return is_legal_move_by_musketeer(location, direction)
    elif at(location) == 'R':
        return is_legal_move_by_enemy(location, direction)
    else:
        return False

def can_move_piece_at(location):
    """Tests whether the player at the location has at least one move available.
       You can assume that input will always be in correct range.
       You can assume that input will always be in correct range."""
    # Iterates through each direction from the location
    # and checks if any move is legal.
    # Returns True if legal move is found.
    # Returns False if loop finishes.
    directions = ["up","down","left","right"]
    for direction in directions:
        if is_legal_move(location, direction):
            return True
    return False

def has_some_legal_move_somewhere(who):
    """Tests whether a legal move exists for player "who" (which must
       be either 'M' or 'R'). Does not provide any information on where
       the legal move is.
       You can assume that input will always be in correct range."""
    # Iterates through rach location on the board.
    # Checks if location holds a piece matching 'who' and if that piece can move
    # If so, returns True. Returns False if loop finishes.
    for row in range(5):
        for column in range(5):
            if (can_move_piece_at((row, column))
                    and at((row, column)) == who):
                return True
    return False

def possible_moves_from(location):
    """Returns a list of directions ('left', etc.) in which it is legal
       for the player at location to move. If there is no player at
       location, returns the empty list, [].
       You can assume that input will always be in correct range."""
    # Iterates through each direction from the given location.
    # Checks if a move in each direction is legal.
    # If so, it adds that location to a list of legal locations.
    # Returns list.
    directions = ["up","down","left","right"]
    legal_directions = []
    for direction in directions:
        if is_legal_move(location, direction):
            legal_directions.append(direction)
    return legal_directions

def is_legal_location(location):
    """Tests if the location is legal on a 5x5 board.
    You can assume that input will always be a pair of integers."""
    r = range(0, 5)
    if location[0] not in r or location[1] not in r:
        return False
    else:
        return True

def is_within_board(location, direction):
    """Tests if the move stays within the boundaries of the board.
    You can assume that input will always be in correct range."""
    return is_legal_location(adjacent_location(location,direction))

def all_possible_moves_for(player):
    """Returns every possible move for the player ('M' or 'R') as a list
       (location, direction) tuples.
       You can assume that input will always be in correct range."""
    # Iterates through every location on the board.
    # Checks whether the given player ('M' or 'R') is in that location.
    # Then iterates through each direction.
    # Checks if a move in that direction is legal and within board.
    # If so, it adds that move to a list of possible moves.
    # Returns the list.
    possible_moves = []
    directions = ["up","down","left","right"]
    for row in range(5):
        for column in range(5):
            location = (row, column)
            if at(location) == player:
                for direction in directions:
                    if (is_legal_move(location, direction)
                            and is_within_board(location, direction)):
                        possible_moves.append((location, direction))
    return possible_moves

def make_move(location, direction):
    """Moves the piece in location in the indicated direction.
       Doesn't check if the move is legal. You can assume that input will always
       be in correct range."""
    # Creates (row, column) tuple for the location of the piece.
    # Creates another (row, column) tuple for the proposed location.
    # Then places piece in the new location and replaces it with blank space.
    # Returns updated board.
    board = get_board()
    (piece_row, piece_column) = location
    (new_row, new_column) = adjacent_location(location, direction)
    board[piece_row][piece_column], board[new_row][new_column] = '-', at(location)
    return board

def choose_computer_move(who):
    """The computer chooses a move for a Musketeer (who = 'M') or an
       enemy (who = 'R') and returns it as the tuple (location, direction),
       where a location is a (row, column) tuple as usual.
       You can assume that input will always be in correct range."""
    # Chooses a move at random out of all possible moves for the selected player.
    # Checks if move is legal and within board.
    # Returns chosen location.
    import random
    location, direction = random.choice(all_possible_moves_for(who))
    while (not is_legal_move(location, direction)
            and not is_within_board(location, direction)):
        location, direction = random.choice(all_possible_moves_for(who))
    return (location, direction)

def is_enemy_win():
    """Returns True if all 3 Musketeers are in the same row or column."""
    # Initialises two counting variables.
    # Iterates through every row place/column place, updating count if M is found.
    # At the end of the row/column, if either count equals 3, returns True.
    # Otherwise resets the counters before checking the next row/column.
    # If not yet returned, returns False.
    M_in_row = 0
    M_in_column = 0
    for i in range(5):
        for j in range(5):
            # i is row, j is column:
            if at((i, j)) == 'M':
                M_in_row += 1
            # j is row, i is column:
            if at((j, i)) == 'M':
                M_in_column += 1
        if M_in_row == 3 or M_in_column == 3:
            return True
        else:
            M_in_row, M_in_column = 0, 0
    return False


#------------- Files functions -------------
#--These functions handle saving and loading of game data
#-------------------------------------------

def write_save_file(user, date, board):
    """Writes the current user's side, board and date/time to a file.
       If a file already exists, it overwrites it."""
    with open('game_data.txt', 'w') as f:
        # Write strings to first two lines of file
        new_contents = "{}\n{}\n".format(user, date)
        f.write(new_contents)
        # Then write board contents in one line
        for row in range(5):
            for column in range(5):
                f.write(board[row][column])

def delete_data():
    """Deletes the saved file."""
    import os
    os.remove("game_data.txt")
    pass

def is_saved_game():
    """Checks if there is a game data file and returns True or False
       (handling exceptions)."""
    try:
        f = open('game_data.txt')
        f.close()
        return True
    except IOError:
        return False

def retrieve_file_contents():
    """Reads saved file, assigns contents to list and makes list global."""
    #if is_saved_game():
    with open('game_data.txt', 'r') as f:
        global f_contents
        f_contents = f.read().splitlines()

def saved_player():
    """Returns the saved user (users_side) from the saved data"""
    retrieve_file_contents()
    user = f_contents[0]
    return user

def saved_date():
    """Returns the date/time from the save file."""
    retrieve_file_contents()
    date = f_contents[1]
    return date

def saved_board():
    """Makes board global. Returns the board from the save file."""
    global board
    retrieve_file_contents()
    board_string = f_contents[2]
    saved_board = [[],[],[],[],[]]
    for row in range(5):
        for column in range(5):
            saved_board[row].append(board_string[column+(5*row)])
    board = saved_board
    return board


###------- Communicating with the user --------

#-------------- Unchanged functions ------------

def print_board():
    print("    1  2  3  4  5")
    print("  ---------------")
    ch = "A"
    for i in range(0, 5):
        print(ch, "|", end = " ")
        for j in range(0, 5):
            print(board[i][j] + " ", end = " ")
        print()
        ch = chr(ord(ch) + 1)
    print()

def choose_users_side():
    """Returns 'M' if user is playing Musketeers, 'R' otherwise."""
    user = ""
    while user != 'M' and user != 'R':
        answer = input("Would you like to play Musketeer (M) or enemy (R)? ")
        answer = answer.strip()
        if answer != "":
            user = answer.upper()[0]
    return user

def describe_move(who, location, direction):
    """Prints a sentence describing the given move."""
    new_location = adjacent_location(location, direction)
    print(who, 'moves', direction, 'from',\
          location_to_string(location), 'to',\
          location_to_string(new_location) + ".\n")


#------ Functions below have been amended to accomodate ------
#------------- saving and loading of game data -------------

def print_instructions():
    print()
    print("""To make a move, enter the location of the piece you want to move,
    and the direction you want it to move. Locations are indicated as a
    letter (A, B, C, D, or E) followed by an integer (1, 2, 3, 4, or 5).
    Directions are indicated as left, right, up, or down (or simply L, R,
    U, or D). For example, to move the Musketeer from the top right-hand
    corner to the row below, enter 'A5 down' (without quotes).""")
    print()
    print("""You have the option to save the game so that you may return to
    the board at a later time. You can save any time that it is your move.
    To do so, when prompted with 'Your move?', simply reply with 'SAVE'.""")
    print()
    print("For convenience in typing, you may use lowercase letters on any command.")
    print()

def move_musketeer(users_side):
    """Gets the Musketeer's move (from either the user or the computer)
       and makes it."""
    if users_side == 'M':
        move = get_users_move_or_save()
        if move == 'SAVE':
            return move
        else:
            (location, direction) = move
        if at(location) == 'M':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Musketeer", location, direction)
        else:
            print("You can't move there!")
            return move_musketeer(users_side)
    else: # Computer plays Musketeer
        (location, direction) = choose_computer_move('M')
        make_move(location, direction)
        describe_move("Musketeer", location, direction)

def move_enemy(users_side):
    """Gets the enemy's move (from either the user or the computer)
       and makes it."""
    if users_side == 'R':
        move = get_users_move_or_save()
        if move == 'SAVE':
            return move
        else:
            (location, direction) = move
        if at(location) == 'R':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Enemy", location, direction)
        else:
            print("You can't move there!")
            return move_enemy(users_side)
    else: # Computer plays enemy
        (location, direction) = choose_computer_move('R')
        make_move(location, direction)
        describe_move("Enemy", location, direction)
        return board

def start():
    """Plays the Three Musketeers Game."""
    global users_side
    skip_m_once = False
    if load_game():
        users_side = saved_player()
        board = saved_board()
        print('You are playing as {}'.format(users_side))
        print()
        instructions_again_perhaps()
        if users_side == 'R':
            skip_m_once = True
    else:
        users_side = choose_users_side()
        board = create_board()
        print_instructions()
    print_board()
    while True:
        if skip_m_once:
            skip_m_once = False
        else:
            if has_some_legal_move_somewhere('M'):
                board = move_musketeer(users_side)
                if board == 'SAVE':
                    break
                print_board()
                if is_enemy_win():
                    print("Cardinal Richleau's men win!")
                    break
            else:
                print("The Musketeers win!")
                break
        if has_some_legal_move_somewhere('R'):
            board = move_enemy(users_side)
            if board == 'SAVE':
                break
            print_board()
        else:
            print("The Musketeers win!")
            break


#--------- Functions below are new ----------

def save_dialog():
    print()
    print("Are you sure you want to save and exit the game?")
    print()
    answer = ""
    s = "save the game and exit"
    if is_saved_game():
        print('Saving will overwrite save game data from {}.'.format(saved_date()))
        print()
        s = "overwrite save game data and exit the game"
    while answer != "YES" and answer != "NO":
        answer = input("""Enter YES to {},
                 or NO to continue playing: """.format(s)).upper()
        print()
    if answer == "YES":
        import datetime
        date = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
        write_save_file(users_side, date, board)
        print("Games is saved at {} and will now exit.".format(date))
        print()
        print("Come back soon!")
        return "SAVE"
    else:
        print_board()
        return get_users_move_or_save()

def load_game():
    """Returns True if the user wishes to load a previously saved game.
       Returns False if user declines or if there is no save data.
       Also gives user option to delete saved data."""
    if is_saved_game():
        print("Would you like to continue the previous game, saved at {date}?".format(date = saved_date()))
        print()
        answer = ""
        while answer != "YES" and answer != "NO" and answer != "DEL":
            answer = input("""Enter YES to continue from last save, or NO to start
            a new game, or DEL to delete saved data: """).upper()
            print()
        if answer == "YES":
            return True
        elif answer == "DEL":
            delete_data()
            print("Data deleted. Starting new game.")
            print()
            return False
    else:
        return False

def instructions_again_perhaps():
    print("Would you like to read the game instructions again?")
    print()
    answer = ""
    while answer != "YES" and answer != "NO":
        answer = input("Enter YES or NO: ").upper()
        print()
    if answer == "YES":
        return print_instructions()
    else:
        print("No problem. Let's get to it!")
        return

def get_users_move_or_save():
    """Gets a legal move from the user, and returns it as a
       (location, direction) tuple. Also allows the user the
       option to save game state."""
    directions = {'L':'left', 'R':'right', 'U':'up', 'D':'down'}
    move = input("Your move? ").upper().replace(' ', '')
    if move == 'SAVE':
        return save_dialog()
    elif (len(move) >= 3
            and move[0] in 'ABCDE'
            and move[1] in '12345'
            and move[2] in 'LRUD'):
        location = string_to_location(move[0:2])
        direction = directions[move[2]]
        if is_legal_move(location, direction):
            return (location, direction)
    print("Illegal move--'" + move + "'")
    return get_users_move_or_save()
