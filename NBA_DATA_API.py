from requests import get

BASE_URL = "http://data.nba.net"
ALL_JSON = "/prod/v1/today.json"


def get_links():
    response = get(BASE_URL+ALL_JSON).json()
    return response["links"]


def get_currentScoreboard():
    response = get(BASE_URL+get_links()["currentScoreboard"]).json()
    games = response["games"]

    for game in games:
        home_team = game["hTeam"]
        away_team = game["vTeam"]
        clock = game["clock"]
        period = game["period"]

        print("#########################################\n")
        print(f"{home_team['triCode']} vs {away_team['triCode']}")
        print(f"SCORE: {home_team['score']} x {away_team['score']}")
        print(f"{clock} - {period['current']}\n")
