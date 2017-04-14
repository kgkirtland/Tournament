# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 15:28:25 2017

Kenny Kirtland
@2015

Table Tournament Application
test comment
"""

from tournament import Match, Game
    
if __name__ == "__main__":
    g = Game()
    g.team1score = 14
    g.team2score = 12
    winner1 = g.isTeam1Winner()
    winner2 = g.isTeam2Winner()

    m = Match()
    m.games.append(g)
    match_score = m.GetScore()
    print(f'Team 1 score: {match_score[0]}, Team 2 score: {match_score[1]}')
    
