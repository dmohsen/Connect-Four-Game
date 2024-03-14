#
# 
#
# A Connect-Four Player class 
#  

from Board import Board

# write your class below.
class Player:
    """ playet class of connect 4 game. Either X or O checker """
    def __init__(self, checker):
        """ constructs a new Player object by initializing the following 
        two attributes """
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0
        
    def __repr__(self):
        """ returns a string representing a Player object. The string returned 
    should indicate which checker the Player object is using """
        return 'Player' + ' ' + self.checker

    def opponent_checker(self):
        """ returns a one-character string representing the checker of the Player 
    object’s opponent. The method may assume that the calling Player object 
    has a checker attribute that is either 'X' or 'O' """
        if self.checker == 'O':
            return 'X'
        else:
            return 'O'

    def next_move(self, b):
        """ accepts a Board object b as a parameter and returns the column where 
    the player wants to make the next move. To do this, the method should ask
    the user to enter a column number that represents where the user wants to 
    place a checker on the board """
        self.num_moves += 1
    
        while True:
            col = int(input('Enter a column: '))
            if b.can_add_to(col) == True:
                return col
            else:
                print('Try again!')
