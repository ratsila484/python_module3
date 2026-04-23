#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_achievement_tracker.py                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: ny-araza <ny-araza@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/16 14:13:31 by ny-araza            #+#    #+#            #
#   Updated: 2026/04/19 00:18:48 by ny-araza           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import random


class Player:
    def __init__(
                self, name: str = "Unknown player",
                achievements_list: list[str] = []
                ):
        self.name = name
        self.achievements = set(
                random.sample(achievements_list, (
                    random.randint(0, (len(achievements_list) - 1))
                    ))
                )

    def show_info(self, status: str = "") -> None:
        if (status == ""):
            print(
                f"Player {self.name}: "
                f"{self.achievements}"
            )
        else:
            print(
                f"{self.name} {status}: "
                f"{self.achievements}"
            )


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    achievements_list: list[str] = [
        'Crafting Genius', 'Strategist',
        'World Savior', 'Speed Runner',
        'Survivor', 'Master Explorer',
        'Treasure Hunter', 'Unstoppable',
        'First Steps', 'Collector Supreme',
        'Untouchable', 'Sharp Mind', 'Boss Slayer'
    ]
    p1 = Player("alice", achievements_list)
    p2 = Player("bob", achievements_list)
    p3 = Player("charlie", achievements_list)
    p4 = Player("dylan", achievements_list)
    print()
    p1.show_info()
    p2.show_info()
    p3.show_info()
    p4.show_info()
    print(f"\nAll distinct achievements: {set(achievements_list)}")
    print()
    print(f"Common achievements: {set.intersection(
                    p1.achievements,
                    p2.achievements,
                    p3.achievements,
                    p4.achievements
                                    )}")
    print(f"Only {p1.name.capitalize()} has: {p1.achievements.difference(
                    p2.achievements,
                    p3.achievements,
                    p4.achievements,
                                    )}")
    print(f"Only {p2.name.capitalize()} has: {p2.achievements.difference(
                    p1.achievements,
                    p3.achievements,
                    p4.achievements,
                                    )}")
    print(f"Only {p3.name.capitalize()} has: {p3.achievements.difference(
                    p1.achievements,
                    p2.achievements,
                    p4.achievements,
                                    )}")
    print(f"Only {p4.name.capitalize()} has: {p4.achievements.difference(
                    p1.achievements,
                    p2.achievements,
                    p3.achievements,
                                    )}")

    print(
        f"\n{p1.name.capitalize()} is missing: "
        f"{set(achievements_list).difference(p1.achievements)}"
        )
    print(
        f"{p2.name.capitalize()} is missing: "
        f"{set(achievements_list).difference(p2.achievements)}"
        )
    print(
        f"{p3.name.capitalize()} is missing: "
        f"{set(achievements_list).difference(p3.achievements)}"
        )
    print(
        f"{p4.name.capitalize()} is missing: "
        f"{set(achievements_list).difference(p4.achievements)}")
