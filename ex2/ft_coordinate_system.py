#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_coordinate_system.py                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: ny-araza <ny-araza@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/16 09:01:21 by ny-araza            #+#    #+#            #
#   Updated: 2026/04/16 14:11:36 by ny-araza           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import math


def get_player_pos() -> tuple[float, float, float]:
    try:
        input_coordinate = input(
            "Enter new coordinates as floats"
            " in format 'x,y,z': "
        )
        input_coordinate.split(',')
        temp_coordinate: list[float] = [0, 0, 0]
        cpt = 0
        for i in range(0, len(input_coordinate)):
            if (input_coordinate[i] != ',' and input_coordinate[i] != ' '):
                temp_coordinate[cpt] = float(input_coordinate[i])
                cpt = cpt + 1
        if (cpt != 3):
            raise ValueError
        coordinate: tuple[float, float, float] = (
                    temp_coordinate[0],
                    temp_coordinate[1],
                    temp_coordinate[2]
                    )
        return coordinate
    except ValueError:
        print("Invalid syntax")
        return (0.0, 0.0, 0.0)


def calculate_distance(
            coordonate1: tuple[float, float, float],
            coordonate2: tuple[float, float, float]
            ) -> float:
    return (math.sqrt((coordonate2[0] - coordonate1[0])**2
            + (coordonate2[1] - coordonate1[1])**2
            + (coordonate2[2]-coordonate1[2])**2
            )
            )


if __name__ == "__main__":
    coordonate: tuple[float, float, float] = get_player_pos()
    print(f"Got a first tuple: {coordonate}")
    x: float = coordonate[0]
    y: float = coordonate[1]
    z: float = coordonate[2]
    print(
        f"It includes: X={x}, "
        f"Y={y}, "
        f"Z={z}"
        )
    print(
        f"Distance to center: "
        f"{round(
            calculate_distance((x, y, z), (0.0, 0.0, 0.0)), 4)}"
        )
