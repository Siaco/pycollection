from soccerapi.api import Api888Sport
# from soccerapi.api import ApiUnibet
# from soccerapi.api import ApiBet365

api = Api888Sport()
url = 'https://www.888sport.com/#/filter/football/italy/serie_a'
odds = api.odds(url)

for match in odds[0]:
    print(match['home_team']+" vs "+match['away_team'])
    print(match['full_time_resut'])
    print(match['both_teams_to_score'])
    print(match['double_chance'])