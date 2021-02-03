# A script to get the neighbors array from the states list
import json
import os
import sys

# Open the json file

def pause():
    programPause = input("Press the <ENTER> key to continue...")
with open('us_state_codes.json') as json_file:
    data = json.load(json_file)

    print(data)

    pause()

    for state in data:
        print(state['Code'])
        for neighbor in state['Neighbors']:
            print(neighbor)
