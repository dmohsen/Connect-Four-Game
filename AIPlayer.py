#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: dylanmohsen
"""
from Board import Board
from Player import Player
import random

class AIPlayer(Player):
    """ AIPlayer class for connect four """
    def __init__(self, checker, tiebreak, lookahead):
        """ constructs a new Player object by initializing the following 
         attributes """
        Player.__init__(self, checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
    
    def __repr__(self):
        """ returns a string representing an AIPlayer object. This method will
        override/replace the __repr__ method that is inherited from Player """
        return ('Player ' + self.checker + ' (' + self.tiebreak + ', ' + \
                str(self.lookahead) + ')')
            
    def max_score_column(self, scores):
        """ takes a list scores containing a score for each column of the 
        board, and that returns the index of the column with the maximum score.
        If one or more columns are tied for the maximum score, the method 
        sshould apply the called AIPlayer‘s tiebreaking strategy to break the 
        tie """
        max_scores = []
        for i in range(len(scores)):
            if scores[i] == max(scores):
                max_scores += [i]
        if self.tiebreak == 'LEFT':
            return max_scores[0]
        if self.tiebreak == 'RIGHT':
            return max_scores[-1]
        if self.tiebreak == 'RANDOM':
            return random.choice(max_scores)
        
    def scores_for(self, b):
        """ takes a list scores containing a score for each column of the 
        board, and that returns the index of the column with the maximum 
        score. If one or more columns are tied for the maximum score, the 
        method should apply the called AIPlayer‘s tiebreaking strategy to 
        break the tie """
        scores = [50] * (range(b.width))
        
        for col in range(b.width):
            if b.can_add_to(col) == False:
                scores[col] = -1
            elif b.is_win_for(self.checker):
                scores[col] = 100
            elif b.is_win_for(self.opponent_checker()):
                scores[col] = 0
            elif self.lookahead == 0 :
                scores[col] = 50
            else:
                b.add_checker(self.checker, col)
                other_player = AIPlayer(self.opponent_checker(), \
                self.tiebreak, self.lookahead-1)
                other_scores = other_player.scores_for(b)
                if max(other_scores) == 0:
                    scores[col] = 100
                elif max(other_scores) == 100:
                    scores[col] = 0
                elif max(other_scores) == 50:
                    scores[col] = 50
                    
                b.remove_checker(col)
        return scores

    def next_move(self, b):
        """ overrides (i.e., replaces) the next_move method that is inherited 
        from Player. Rather than asking the user for the next move, this 
        version of next_move should return the called AIPlayer‘s judgment 
        of its best possible move. """
        self.num_moves += 1
        scores = self.scores_for()
        return self.max_score_column(scores)

         
