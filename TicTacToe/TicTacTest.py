test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)

player_input()

place_marker(test_board,'$',8)
display_board(test_board)

win_check(test_board,'X')

import random

