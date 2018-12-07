import pytest
from three_musketeers import *

left = 'left'
right = 'right'
up = 'up'
down = 'down'
M = 'M'
R = 'R'
_ = '-'

board1 =  [ [_,  _,  _,  M,  _],
            [_,  _,  R,  M,  _],
            [_,  R,  M,  R,  _],
            [_,  R,  _,  _,  _],
            [_,  _,  _,  R,  _] ]

board2 =  [ [M,  _,  _,  _,  _],
            [R,  _,  _,  R,  _],
            [R,  _,  _,  R,  R],
            [_,  M,  _,  _,  M],
            [_,  _,  R,  R,  _] ]

board3 =  [ [_,  _,  _,  _,  _],
            [_,  _,  R,  _,  _],
            [_,  R,  _,  M,  _],
            [_,  R,  _,  M,  _],
            [_,  _,  _,  M,  _] ]

# A musketeer M can move to any orthogonal space occupied by an enemy
# An enemy R can move to any orthogonal empty space

def test_create_board():
    create_board()
    assert at((0, 0)) == R
    assert at((0, 4)) == M
    assert at((2,2)) == M
    assert at((4,0)) == M
    assert at((1,3)) == R

def test_set_board():
    set_board(board1)
    assert at((0, 0)) == _
    assert at((1, 2)) == R
    assert at((1, 3)) == M
    set_board(board2)
    assert at((0, 0)) == M
    assert at((1, 1)) == _
    assert at((4, 3)) == R
    set_board(board3)
    assert at((0, 4)) == _
    assert at((1, 2)) == R
    assert at((3, 3)) == M

def test_get_board():
    set_board(board1)
    assert board1 == get_board()
    set_board(board2)
    assert board2 == get_board()
    set_board(board3)
    assert board3 == get_board()


def test_string_to_location():
    with pytest.raises(ValueError):
        string_to_location('X3')
    with pytest.raises(ValueError):
        string_to_location('A6')
    with pytest.raises(ValueError):
        string_to_location('F1')
    assert string_to_location('A1') == (0, 0)
    assert string_to_location('D2') == (3, 1)
    assert string_to_location('E5') == (4, 4)

def test_location_to_string():
    with pytest.raises(ValueError):
        location_to_string((0, 7))
    with pytest.raises(ValueError):
        location_to_string((4, 5))
    assert location_to_string((0, 3)) == 'A4'
    assert location_to_string((3, 4)) == 'D5'
    assert location_to_string((4, 0)) == 'E1'

def test_at():
    set_board(board1)
    assert at((0, 3)) == M
    assert at((2, 4)) == _
    set_board(board2)
    assert at((1, 1)) == _
    assert at((4, 2)) == R
    set_board(board3)
    assert at((1, 4)) == _
    assert at((1, 2)) == R

def test_all_locations():
    """All 5x5 board locations are listed below
    so that the test can assert equality"""
    list_of_locations = [
        (0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
        (1, 0), (1, 1), (1, 2), (1, 3), (1, 4),
        (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
        (3, 0), (3, 1), (3, 2), (3, 3), (3, 4),
        (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)
        ]
    assert sorted(list_of_locations ) == sorted(all_locations())

def test_adjacent_location():
    assert adjacent_location((1, 2), right) == (1, 3)
    assert adjacent_location((2, 2), down) == (3, 2)
    assert adjacent_location((1, 2), left) == (1, 1)
    assert adjacent_location((3, 2), up) == (2, 2)
    assert adjacent_location((4, 4), left) == (4, 3)

def test_is_legal_move_by_musketeer():
    """See in-line comments on each line below to see what each move is attempting to do."""
    set_board(board1)
    with pytest.raises(ValueError):
        is_legal_move_by_musketeer((3, 0), down)                # Trying to move _
    with pytest.raises(ValueError):
        is_legal_move_by_musketeer((2, 1), right)               # Trying to move R
    assert is_legal_move_by_musketeer((0, 3), up) == False      # Move to a location that is out of bounds
    assert is_legal_move_by_musketeer((2, 2), down) == False    # Move to a location that is _
    assert is_legal_move_by_musketeer((2, 2), up) == True       # Move to a location that is R
    set_board(board2)
    assert is_legal_move_by_musketeer((3, 4), right) == False   # Move to a location that is out of bounds
    assert is_legal_move_by_musketeer((3, 4), up) == True       # Move to a location that is R
    assert is_legal_move_by_musketeer((3, 1), down) == False    # Move to a location that is _
    set_board(board3)
    assert is_legal_move_by_musketeer((4, 3), up) == False      # Move to a location that is M
    assert is_legal_move_by_musketeer((4, 3), down) == False    # Move to a location that is out of bound
    assert is_legal_move_by_musketeer((3, 3), right) == False   # Move to a location that is _

def test_is_legal_move_by_enemy():
    """See in-line comments on each line below to see what each move is attempting to do."""
    set_board(board1)
    with pytest.raises(ValueError):
        is_legal_move_by_enemy((0, 3), left)                    # Trying to move M
    with pytest.raises(ValueError):
        is_legal_move_by_enemy((4, 1), left)                    # Trying to move _
    assert is_legal_move_by_enemy((1, 2), left) == True         # Move to a location that is _
    assert is_legal_move_by_enemy((2, 3), up) == False          # Move to a location that is M
    assert is_legal_move_by_enemy((2, 3), left) == False        # Move to a location that is M
    assert is_legal_move_by_enemy((2, 3), down) == True         # Move to a location that is _
    assert is_legal_move_by_enemy((2, 3), right) == True        # Move to a location that is _
    set_board(board2)
    assert is_legal_move_by_enemy((4, 3), down) == False        # Move to a location that is out of bounds
    assert is_legal_move_by_enemy((4, 3), up) == True           # Move to a location that is _
    assert is_legal_move_by_enemy((4, 3), right) == True        # Move to a location that is _
    assert is_legal_move_by_enemy((4, 3), left) == False        # Move to a location that is R

def test_is_legal_move():
    """See in-line comments on each line below to see what each move is attempting to do."""
    set_board(board1)
    assert is_legal_move((3, 1), up) == False                   # Move R to location that is R
    assert is_legal_move((2, 2), left) == True                  # Move M to location that is R
    set_board(board2)
    assert is_legal_move((2, 4), right) == False                # Move R to a location that is out of bounds
    assert is_legal_move((0, 0), up) == False                   # Move M to a location that is out of bounds
    set_board(board3)
    assert is_legal_move((1, 2), right) == True                 # Move R to location that is _
    assert is_legal_move((4, 4), down) == False                 # Move _ to a location that is out of bounds

def test_can_move_piece_at():
    set_board(board1)
    assert can_move_piece_at((0, 3)) == False
    assert can_move_piece_at((1, 2)) == True
    assert can_move_piece_at((2, 2)) == True
    set_board(board3)
    assert can_move_piece_at((4, 3)) == False
    assert can_move_piece_at((1, 2)) == True

def test_has_some_legal_move_somewhere():
    set_board(board1)
    assert has_some_legal_move_somewhere('M') == True
    assert has_some_legal_move_somewhere('R') == True
    set_board(board2)
    assert has_some_legal_move_somewhere('M') == True
    assert has_some_legal_move_somewhere('R') == True
    set_board(board3)
    assert has_some_legal_move_somewhere('M') == False
    assert has_some_legal_move_somewhere('R') == True

def test_possible_moves_from():
    set_board(board1)
    assert possible_moves_from((3, 1)) == [down, left, right]
    assert possible_moves_from((0, 2)) == []
    assert possible_moves_from((0, 0)) == []
    assert possible_moves_from((4, 3)) == [up, left, right]
    assert possible_moves_from((2, 2)) == [up, left, right]

def test_is_legal_location():
    assert is_legal_location((5, 1)) == False
    assert is_legal_location((2, 5)) == False
    assert is_legal_location((0, 3)) == True
    assert is_legal_location((0, 0)) == True
    assert is_legal_location((6, 6)) == False
    assert is_legal_location((4, 4)) == True

def test_is_within_board():
    assert is_within_board((0, 3),  up) == False
    assert is_within_board((4, 1),  down) == False
    assert is_within_board((3, 0),  left) == False
    assert is_within_board((2, 4),  right) == False
    assert is_within_board((4, 3),  up) == True
    assert is_within_board((1, 3),  down) == True

def test_all_possible_moves_for():
    """Board is set to board1. All posible move for M and R on board1 are listed below
    so that the test can assert equality"""
    set_board(board1)
    All_M_moves = [
        ((1, 3), left),
        ((1, 3), down),
        ((2, 2), left),
        ((2, 2), right),
        ((2, 2), up)
        ]
    All_R_moves = [
        ((1, 2), up),
        ((1, 2), left),
        ((2, 1), up),
        ((2, 1), left),
        ((2, 3), right),
        ((2, 3), down),
        ((3, 1), left),
        ((3, 1), right),
        ((3, 1), down),
        ((4, 3), up),
        ((4, 3), left),
        ((4, 3), right)
        ]
    assert sorted(all_possible_moves_for(M)) == sorted(All_M_moves)
    assert sorted(all_possible_moves_for(R)) == sorted(All_R_moves)
    """Board is set to board3. All posible move for M and R on board3 are listed below
    so that the test can assert equality"""
    set_board(board3)
    All_M_moves = []
    All_R_moves = [
        ((1, 2), up),
        ((1, 2), left),
        ((1, 2), down),
        ((1, 2), right),
        ((2, 1), up),
        ((2, 1), left),
        ((2, 1), right),
        ((3, 1), left),
        ((3, 1), right),
        ((3, 1), down)
        ]
    assert sorted(all_possible_moves_for(M)) == sorted(All_M_moves)
    assert sorted(all_possible_moves_for(R)) == sorted(All_R_moves)

def test_make_move():
    """Board is set to board1. Move is made. 'new_board' showing the expected board is
    created below so that the test can assert that the board has been updated correctly."""
    set_board(board1)
    make_move((3, 1), left)
    new_board = [ [_,  _,  _,  M,  _],
                  [_,  _,  R,  M,  _],
                  [_,  R,  M,  R,  _],
                  [R,  _,  _,  _,  _],
                  [_,  _,  _,  R,  _] ]
    assert get_board() == new_board
    """The board is not reset. Move is made. 'new_board' showing the expected board is
    updated below so that the test can assert that the board has been updated correctly."""
    make_move((2, 2), up)
    new_board = [ [_,  _,  _,  M,  _],
                  [_,  _,  M,  M,  _],
                  [_,  R,  _,  R,  _],
                  [R,  _,  _,  _,  _],
                  [_,  _,  _,  R,  _] ]
    assert get_board() == new_board

    """Board is set to board3. Move is made. 'new_board' showing the expected board is
    updated below so that the test can assert that the board has been updated correctly."""
    set_board(board3)
    make_move((1, 2), left)
    new_board = [ [_,  _,  _,  _,  _],
                  [_,  R,  _,  _,  _],
                  [_,  R,  _,  M,  _],
                  [_,  R,  _,  M,  _],
                  [_,  _,  _,  M,  _] ]
    assert get_board() == new_board
    """The board is not reset. Move is made. 'new_board' showing the expected board is
    updated below so that the test can assert that the board has been updated correctly."""
    make_move((1, 1), up)
    new_board = [ [_,  R,  _,  _,  _],
                  [_,  _,  _,  _,  _],
                  [_,  R,  _,  M,  _],
                  [_,  R,  _,  M,  _],
                  [_,  _,  _,  M,  _] ]
    assert get_board() == new_board


def test_choose_computer_move():
    """Simply checks that the chosen moves for R and M are legal and within board."""
    set_board(board1)
    location, direction = choose_computer_move(M)
    assert (is_legal_move_by_musketeer(location, direction)
                and is_within_board(location, direction))
    location, direction = choose_computer_move(R)
    assert (is_legal_move_by_enemy(location, direction)
                and is_within_board(location, direction))

def test_is_enemy_win():
    """Two configurations are created below in order to test the two
    win conditions (all M in same row or all M in same column).
    The three test boards are also tested."""
    row_win = [ [_,  _,  _,  _,  _],
                 [_,  _,  R,  _,  _],
                 [_,  R,  M,  M,  M],
                 [_,  R,  _,  _,  _],
                 [_,  _,  _,  R,  _]
                 ]
    column_win = [[_,  _,  _,  M,  _],
                 [_,  _,  R,  M,  _],
                 [_,  R,  _,  M,  _],
                 [_,  R,  _,  _,  _],
                 [_,  _,  _,  R,  _]
                 ]
    set_board(row_win)
    assert is_enemy_win() == True
    set_board(column_win)
    assert is_enemy_win() == True
    set_board(board1)
    assert is_enemy_win() == False
    set_board(board2)
    assert is_enemy_win() == False
    set_board(board3)
    assert is_enemy_win() == True
