#!env/bin/python3

import random
from typing import Generator


def gen_event(
            list_players: list[str],
            list_actions: list[str]
            ) -> Generator[tuple[str, str], None, None]:
    while True:
        index_action = random.randint(0, (len(list_actions) - 1))
        index_player = random.randint(0, (len(list_players) - 1))
        yield (list_players[index_player], list_actions[index_action])


def consume_event(
            lists: list[tuple[str, str]]
                ) -> Generator[list[tuple[str, str]], None, None]:
    while True:
        index = random.randint(0, (len(lists) - 1))
        item = lists[index]
        print(item)
        print(f"Got event from lists: {item}")
        lists.remove(item)
        yield lists


if __name__ == "__main__":
    list_players: list[str] = [
        "bob", "alice", "dylan", "charlie"
    ]
    list_actions: list[str] = [
        "run", "eat", "sleep", "grab",
        "move", "swim", "climb", "use", "release"
    ]
    gen = gen_event(list_players, list_actions)
    for i in range(1000):
        temp_gen = next(gen)
        print(
            f"Event {i}: Player {temp_gen[0]}"
            f" did actions {temp_gen[1]}"
            )
    gen = gen_event(list_players, list_actions)
    ten_gen: list[tuple[str, str]] = []
    for i in range(10):
        temp_gen = next(gen)
        ten_gen.append(temp_gen)
    print(f"Built list of 10 events: {ten_gen}")
    consume_gen = consume_event(ten_gen)
    for i in range(len(ten_gen)):
        ten_gen = next(consume_gen)
        print(f"Remains in list: {ten_gen}")
