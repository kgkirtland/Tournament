# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 15:28:25 2017

Kenny Kirtland
@2015

Table Tournament Application

"""

class Game:
    """
        Game
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
    
    
    
class Match:
    """
        Match
    """
   
    def __init__(self):            
        self.team1score = 0
        self.team2score = 0
        self.games = []
        
    
    def GetScore(self):
        team1score = 0
        team2score = 0
        
        for game in self.games:
           if game.isTeam1Winner(): 
               team1score += 1
           elif game.isTeam2Winner():
               team2score += 1
        return (team1score, team2score)