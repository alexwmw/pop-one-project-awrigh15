import pytest
from three_musketeers import *

left = 'left'
right = 'right'
up = 'up'
down = 'down'
M = 'M'
R = 'R'
_ = '-'

board1 =  [ [_, _, _, M, _],
            [_, _, R, M, _],
            [_, R, M, R, _],
            [_, R, _, _, _],
            [_, _, _, R, _] ]

def test_create_board():
    create_board()
    assert at((0,0)) == R
    assert at((0,4)) == M
    #eventually add at least two more test cases

def test_set_board():
    set_board(board1)
    assert at((0,0)) == _
    assert at((1,2)) == R
    assert at((1,3)) == M    
    #eventually add some board2 and at least 3 tests with it

def test_get_board():
    set_board(board1)
    assert board1 == get_board()
    #eventually add at least one more test with another board

def test_string_to_location():
    with pytest.raises(ValueError):
        string_to_location('X3')
    assert string_to_location('A1') == (0,0)
    #eventually add at least one more exception test and two more
    #test with correct inputs

def test_location_to_string():
    with pytest.raises(ValueError):
        location_to_string((0,7))
    assert location_to_string((0,0)) == 'A1'
    # First test added

def test_at():
    assert at((0,3)) == M 
    # First test added

def test_all_locations():
    assert all_locations == [
                            (0,0),(0,1),(0,2),(0,3),(0,4),
                            (1,0),(1,1),(1,2),(1,3),(1,4),
                            (2,0),(2,1),(2,2),(2,3),(2,4),
                            (3,0),(3,1),(3,2),(3,3),(3,4),
                            (4,0),(4,1),(4,2),(4,3),(4,4) ]
    # Test added

def test_adjacent_location():
    assert adjacent_location((1,2),right) == (1,3)
    assert adjacent_location((2,2),down) == (3,2)
    assert adjacent_location((1,2),left) == (1,1)
    assert adjacent_location((3,2),up) == (2,2)
    # Four tests added


def test_is_legal_move_by_musketeer():
    with pytest.raises(ValueError):
        at(3,0)
    assert is_legal_move_by_musketeer((1,3),down) == True
    assert is_legal_move_by_musketeer((2,2),down) == False
    # Tests added
    # Check use of .raises
    
def test_is_legal_move_by_enemy():
    with pytest.raises(ValueError):
        at(0,3)
    assert is_legal_move_by_enemy((1,2),left) == True
    assert is_legal_move_by_enemy((2,3),up) == False
    # Tests added
    # Check use of .raises

def test_is_legal_move():
    # Replace with tests

def test_can_move_piece_at():
    # Replace with tests

def test_has_some_legal_move_somewhere():
    set_board(board1)
    assert has_some_legal_move_somewhere('M') == True
    assert has_some_legal_move_somewhere('R') == True
    # Eventually put at least three additional tests here
    # with at least one additional board

def test_possible_moves_from():
    # Replace with tests

def test_is_legal_location():
    # Replace with tests

def test_is_within_board():
    # Replace with tests

def test_all_possible_moves_for():
    # Replace with tests
    
def test_make_move():
    # Replace with tests
    
def test_choose_computer_move():
    # Replace with tests; should work for both 'M' and 'R'

def test_is_enemy_win():
    # Replace with tests


