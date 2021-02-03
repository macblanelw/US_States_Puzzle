# puzzle.py
# Objective 1: Make a collection of lists such that each list starts with a
#   US State and contains three more states that can be reached as if "on foot"\
# Objective 2: For each list, make an array of each of the letters of all of the 
#   state codes in that list
# Objective 3: Perutate each of those arrays, and see if any of those permutations
#   are in the list of English words
# Objective 4: Store the results in a list


# Imports

import json, os, sys

# Globals

paths = []      # an array of strings


# Functions

# Import list of state codes. Store in an array

# Import the list of English Words. Store in an array

# Recursive Function to create a list of 4 states
def createPath(state, path, count):
    if count == 4:
        if state not in path:
            path.append(state)
            paths.append(path)

    else:
        for neighbor in state[Neighbors]:
            if state not in path:
                createPath(neighbor, path, count + 1)


# Main
