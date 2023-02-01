from data_classes.player_line import PlayerLine
import json

f = open("nba-stats\\assets\\sample_box_score.json")
sample_box_score = json.load(f)
f.close()

home_players = sample_box_score['game']['homeTeam']['players']
away_players = sample_box_score['game']['awayTeam']['players']
all_players = home_players + away_players

for player in all_players:
    if player['status'] == "ACTIVE":
        stats = player['statistics']
        line = {
            "player": player['name'],
            "minutes": stats['minutesCalculated'],
            "fgm": stats['fieldGoalsMade'],
            "fga": stats['fieldGoalsAttempted'],
            "threepm": stats['threePointersMade'],
            "threepa": stats['threePointersAttempted'],
            "pts": stats['points'],
            "ftm": stats['freeThrowsMade'],
            "fta": stats['freeThrowsAttempted'],
            "drb": stats['reboundsDefensive'],
            "orb": stats['reboundsOffensive'],
            "ast": stats['assists'],
            "stl": stats['steals'],
            "blk": stats['blocks'],
            "pf": stats['foulsPersonal'],
            "tov": stats['turnovers']
        }

        player_line = PlayerLine(**line)
        print(f"{player_line.get_game_score()} - {player_line.player}", )

