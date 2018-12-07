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
    #Five test cases

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
    #Three boards tested

def test_get_board():
    set_board(board1)
    assert board1 == get_board()
    set_board(board2)
    assert board2 == get_board()
    set_board(board3)
    assert board3 == get_board()
    #Three boards tested


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
    # First test passed
    # More ValueError and assert tests added

def test_location_to_string():
    #
    with pytest.raises(ValueError):
        location_to_string((0, 7))
    with pytest.raises(ValueError):
        location_to_string((4, 5))
    assert location_to_string((0, 3)) == 'A4'
    assert location_to_string((3, 4)) == 'D5'
    assert location_to_string((4, 0)) == 'E1'
    # First test passed
    # More ValueError and assert tests added



def test_at():
    set_board(board1)
    assert at((0, 3)) == M
    assert at((2, 4)) == _
    set_board(board2)
    assert at((1, 1)) == _
    assert at((4, 2)) == R
    # First test passed
    # Five more tests added across two boards

def test_all_locations():
    list_of_locations = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
    assert sorted(list_of_locations) == sorted(all_locations())
    # Test passed

def test_adjacent_location():
    assert adjacent_location((1, 2), right) == (1, 3)
    assert adjacent_location((2, 2), down) == (3, 2)
    assert adjacent_location((1, 2), left) == (1, 1)
    assert adjacent_location((3, 2), up) == (2, 2)
    # Four tests passed
'''
def test_is_legal_move_by_musketeer():
    set_board(board1)
    with pytest.raises(ValueError):
        is_legal_move_by_musketeer((3, 0), down)    # Piece at 3, 0 is _
    with pytest.raises(ValueError):
        is_legal_move_by_musketeer((2, 1), right)   # Piece at 1, 3 is R
    assert is_legal_move_by_musketeer((2, 2), down) == False    # is _
    assert is_legal_move_by_musketeer((2, 2), up) == True       # is R
    assert is_legal_move_by_musketeer((2, 2), left) == True     # is R
    assert is_legal_move_by_musketeer((2, 2), right) == True    # is R
    assert is_legal_move_by_musketeer((1, 3), left) == True     # is R
    set_board(board2)
    assert is_legal_move_by_musketeer((3, 4), right) == False   # out of bounds
    assert is_legal_move_by_musketeer((3, 4), up) == True       # is R
    assert is_legal_move_by_musketeer((3, 1), down) == False    # is _
    assert is_legal_move_by_musketeer((3, 1), left) == False    # is _
    assert is_legal_move_by_musketeer((3, 1), right) == False   # is _
    set_board(board3)
    assert is_legal_move_by_musketeer((4, 3), up) == False      # is M
    assert is_legal_move_by_musketeer((4, 3), down) == False    # out of bound
    assert is_legal_move_by_musketeer((4, 3), left) == False    # is _
    assert is_legal_move_by_musketeer((3, 3), right) == False   # is _
    assert is_legal_move_by_musketeer((0, 3), up) == False      # out of bound
    #First tests passed
    #More cases added

def test_is_legal_move_by_enemy():
    set_board(board1)
    with pytest.raises(ValueError):
        is_legal_move_by_enemy((0, 3), left)    # Piece at 0, 3 is M
    with pytest.raises(ValueError):
        is_legal_move_by_enemy((4, 1), left)    # Piece at 0, 3 is _
    assert is_legal_move_by_enemy((1, 2), left) == True         # is _
    assert is_legal_move_by_enemy((2, 3), up) == False          # is M
    assert is_legal_move_by_enemy((2, 3), left) == False        # is M
    assert is_legal_move_by_enemy((2, 3), down) == True         # is _
    assert is_legal_move_by_enemy((2, 3), right) == True        # is _
    set_board(board2)
    assert is_legal_move_by_enemy((4, 3), down) == False        # out of bounds
    assert is_legal_move_by_enemy((4, 3), up) == True           # is _
    assert is_legal_move_by_enemy((4, 3), right) == True        # is _
    assert is_legal_move_by_enemy((4, 3), left) == False        # is R
    # Tests passed;
    # More cases added

### CONTINUE FROM HERE ###

def test_is_legal_move():
    set_board(board1)
    assert is_legal_move((3, 1), up) == False
    assert is_legal_move((2, 2), right) == True
    set_board(board2)
    assert is_legal_move((2, 4), right) == False    # out of bounds
    assert is_legal_move((0, 0), up) == False       # out of bounds
    # Tests passed;
    # More cases added

def test_can_move_piece_at():
    set_board(board1)
    assert can_move_piece_at((0, 3)) == False
    assert can_move_piece_at((1, 2)) == True
    assert can_move_piece_at((2, 2)) == True
    set_board(board3)
    assert can_move_piece_at((4, 3)) == False
    # Four tests added; two tests passed

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
    # Test for three boards

def test_possible_moves_from():
    set_board(board1)
    assert possible_moves_from((3, 1)) == [down, left, right]
    assert possible_moves_from((0, 2)) == []
    assert possible_moves_from((0, 0)) == []
    assert possible_moves_from((4, 3)) == [up, left, right]
    assert possible_moves_from((2, 2)) == [up, left, right]
    # Five tests added


def test_is_legal_location():
    assert is_legal_location((5, 1)) == False
    assert is_legal_location((2, 5)) == False
    assert is_legal_location((0, 3)) == True
    # Three tests passed

def test_is_within_board():
    assert is_within_board((0, 3),  up) == False
    assert is_within_board((4, 1),  down) == False
    assert is_within_board((3, 0),  left) == False
    assert is_within_board((2, 4),  right) == False
    assert is_within_board((4, 3),  up) == True
    # Five tests passed

def test_all_possible_moves_for():
    set_board(board1)
    # Possible moves for R, M in board1 as lists:
    M_moves = [((1, 3), left), ((1, 3), down), ((2, 2), left), ((2, 2), right), ((2, 2), up)]
    R_moves = [((1, 2), up), ((1, 2), left), ((2, 1), up), ((2, 1), left), ((2, 3), right), ((2, 3), down), ((3, 1), left), ((3, 1), right), ((3, 1), down), ((4, 3), up), ((4, 3), left), ((4, 3), right)]
    assert sorted(all_possible_moves_for(M)) == sorted(M_moves)
    assert sorted(all_possible_moves_for(R)) == sorted(R_moves)
    # Two tests added; first test passed

def test_make_move():
    set_board(board1)
    make_move((3, 1), left)
    new_board = [ [_,  _,  _,  M,  _],
                  [_,  _,  R,  M,  _],
                  [_,  R,  M,  R,  _],
                  [R,  _,  _,  _,  _],
                  [_,  _,  _,  R,  _] ]
    assert get_board() == new_board
    make_move((2, 2), up)
    new_board = [ [_,  _,  _,  M,  _],
                  [_,  _,  M,  M,  _],
                  [_,  R,  _,  R,  _],
                  [R,  _,  _,  _,  _],
                  [_,  _,  _,  R,  _] ]
    assert get_board() == new_board
    # One test passed; second added

def test_choose_computer_move():
    set_board(board1)
    location, direction = choose_computer_move(M)
    assert is_legal_move_by_musketeer(location, direction) and is_within_board(location, direction)
    location, direction = choose_computer_move(R)
    assert is_legal_move_by_enemy(location, direction) and is_within_board(location, direction)



def test_is_enemy_win():
    set_board(board1)
    assert is_enemy_win() == False

    row_win = [ [_,  _,  _,  _,  _],
                 [_,  _,  R,  _,  _],
                 [_,  R,  M,  M,  M],
                 [_,  R,  _,  _,  _],
                 [_,  _,  _,  R,  _] ]
    set_board(row_win)
    assert is_enemy_win() == True


    column_win = [[_,  _,  _,  M,  _],
                 [_,  _,  R,  M,  _],
                 [_,  R,  _,  M,  _],
                 [_,  R,  _,  _,  _],
                 [_,  _,  _,  R,  _] ]
    set_board(column_win)
    assert is_enemy_win() == True
    # Tests passed
    set_board(board1)
    assert is_enemy_win() == False
    set_board(board2)
    assert is_enemy_win() == False
    set_board(board3)
    assert is_enemy_win() == True
'''
