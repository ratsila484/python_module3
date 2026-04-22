#!bin/bin/python3

import random

if __name__ == "__main__":
    players = [
        'Alice', 'bob', 'Charlie', 'dylan',
        'Emma', 'Gregory', 'john', 'kevin', 'Liam'
        ]
    all_players_capitalize = [
                    player.capitalize() for player in players
                    ]
    only_player_capitalize = [
                    player for player in players
                    if player.capitalize() == player
                    ]
    print(
        f"Initial list of "
        f"player: {players}"
        )
    print(
        f"New list with all "
        f"name capitalized: {all_players_capitalize}"
        )
    print(
        f"New list of capitalized "
        f"names only: {only_player_capitalize}"
        )
    players_dict: dict[str, int] = {}
    players_dict = {
            player: random.randint(1, 1000) for
            player in all_players_capitalize
            }
    print(players_dict)
    average = sum(players_dict.values()) / (len(players_dict.values()))
    print(f"Score average is {round(average, 2)}")
    hight_scores = {
            player: score for player, score
            in players_dict.items() if score > average
            }
    print(hight_scores)
