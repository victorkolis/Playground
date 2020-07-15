tic_tac_toe_board = {'A':'X', 'B':' ', 'C':'0', \
                     'D':' ', 'E':'0', 'F':' ', \
                     'G':'X', 'H':'X', 'I':'X'}


def printBoard(board):
    print(board['A'] + '|' + board['B'] + '|' + board['C'])
    print('-----')
    print(board['D'] + '|' + board['E'] + '|' + board['F'])
    print('-----')
    print(board['G'] + '|' + board['H'] + '|' + board['I'])

printBoard(tic_tac_toe_board)
