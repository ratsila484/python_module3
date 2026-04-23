#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_score_analytics.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: ny-araza <ny-araza@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/14 09:30:46 by ny-araza            #+#    #+#            #
#   Updated: 2026/04/16 09:00:57 by ny-araza           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys


class NoParameterGiven(Exception):
    def __init__(
            self,
            program_name: str = "python3 ft_score_analytics.py"
            ):
        self.error = f"{program_name}"


def no_parameter_given(len: int, program_name: str) -> bool:
    if (len <= 1):
        return False
    else:
        return True


def non_numeric_parameter(parameter: str) -> int:
    try:
        number = int(parameter)
        return number
    except ValueError:
        print(f"Invalid parameter: '{parameter}'")
        return 0


if __name__ == "__main__":
    try:
        print("=== Player Score Analytics ===")
        len_parameter: int = len(sys.argv)
        if (not no_parameter_given(len_parameter, sys.argv[0])):
            raise NoParameterGiven(sys.argv[0])
        else:
            scores: list[int] = []
            for i in range(1, len_parameter):
                score = non_numeric_parameter(sys.argv[i])
                scores.append(score)
            if (not scores[0]):
                raise NoParameterGiven(sys.argv[0])
            print(f"Scores processed: {scores}")
            print(f"Total player: {len(scores)}")
            print(f"Total score: {sum(scores)}")
            print(f"Average score: {round(sum(scores)/len(scores), 1)}")
            print(f"High score: {max(scores)}")
            print(f"Low score: {min(scores)}")
            print(f"Score range: {max(scores) - min(scores)}")
    except NoParameterGiven as e:
        print(
            f"No score provided. Usage:"
            f"{e} <score1> <score2> ..."
            )
