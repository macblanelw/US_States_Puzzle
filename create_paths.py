import json
import os, sys

paths = []      # an array of strings
codes = []      # a list of the state codes

# Files
with open('us_state_codes.json') as json_file:
    data = json.load(json_file)

# Recursive Function to create a list of 4 states
def createPath(state, path, count):
    if count == 4:
        if state not in path:
            path.append(state)
            paths.append(path)

    else:
        for neighbor in state['Neighbors']:
            if state not in path:
                createPath(neighbor, path, count + 1)


# make a list of the state codes
for state in data:
    codes.append(state['Code'])

for state in codes:
    path = []
    count = 1
    createPath(state, path, count)

print(paths)




# with open('us_state_codes.json') as json_file:
#     data = json.load(json_file)

#     print(data)

#     pause()

#     for state in data:
#         print(state['Code'])
#         for neighbor in state['Neighbors']:
#             print(neighbor)