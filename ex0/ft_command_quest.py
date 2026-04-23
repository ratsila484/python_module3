#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_command_quest.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: ny-araza <ny-araza@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/14 08:52:01 by ny-araza            #+#    #+#            #
#   Updated: 2026/04/14 09:32:26 by ny-araza           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys

if __name__ == "__main__":
    try:
        len: int = len(sys.argv)
        print(f"Program name: {sys.argv[0]}")
        if len == 1:
            print("No arguments provided!")
        else:
            print(f"Argument received: {len - 1}")
            for i in range(1, len):
                print(f"Argument {i}: {sys.argv[i]}")
        print(f"Total arguments: {len}")
    except Exception as e:
        print(f"An error occured: {e}")
