import json

import httpx
from igdb.wrapper import IGDBWrapper


def main():
    r = httpx.post("https://id.twitch.tv/oauth2/token?client_id=8m4pmu6ythodlw7sdssutmah1f7b4r&client_secret=14j7uvv3qh5cgsf9q4em6kxkv2n5k1&grant_type=client_credentials")
    access_token = r.json()["access_token"]
    wrapper = IGDBWrapper("8m4pmu6ythodlw7sdssutmah1f7b4r", access_token)
    i = 0
    games = []

    while i < 3000:
        r = wrapper.api_request("games", f"fields *; where rating > 75; sort rating desc; limit 500; offset {i};")
        i += 500
        games += json.loads(r)

    with open("games.json", "w") as games_file:
        json.dump(games, games_file)


if __name__ == "__main__":
    main()
