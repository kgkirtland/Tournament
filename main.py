# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 15:28:25 2017

@author: E002592
"""

class Match:
    """
        Match
    """
    WINNING_SCORE = 11
    
    def __init__(self):            
        self.team1score = 0
        self.team2score = 0
               
    def isTeam1Winner(self):
        return self.CheckWinner(self.team1score, self.team2score)
    
    def isTeam2Winner(self):
        return self.CheckWinner(self.team2score, self.team1score)
    
    def CheckWinner(self, score1, score2):
        winning_score = self.WINNING_SCORE
        
        if score1 < winning_score and score2 < winning_score:
            return False
        if score1 == winning_score and score2 < winning_score:
            return True
        if score1 >= winning_score and score2 >= winning_score and score1 - score2 >= 2:
            return True   
        return False
    
if __name__ == "__main__":
    m = Match()
    m.team1score = 14
    m.team2score = 12
    winner1 = m.isTeam1Winner()
    winner2 = m.isTeam2Winner()    
    print(f"Team 1 Winner  = {winner1}")
    print(f"Team 2 Winner  = {winner2}")