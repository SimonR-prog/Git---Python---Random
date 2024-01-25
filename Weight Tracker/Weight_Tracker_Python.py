import json
import datetime
import os
def clear_console(): # Function to clear the console.
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')

def importer():
    with open('weight_data.json') as f:
        data_dict = f.read()
    data_dict = json.loads(data_dict)
    return data_dict

def writer(today_dict):
    # Function to write the information to the
    old_data = importer()
    new_data = {}
    for i in old_data:
        new_data.update(i)
    new_data.update(today_dict)
    #new_data = old_data
    with open('weight_data.json', 'w') as f:
        f.write(json.dumps(new_data))

def summary():
    # Function to use on sundays to sum up the previous weeks data and put into json.file.

    with open('weight_summary.json', 'w') as f:
        f.write(json.dumps(new_data))

    """ Need to find out which week it is and to take the weight of the first and last
     day of the previous week and log the difference into a dictionary with the week
     as the key to the value (weight)."""


def ui():
    # Function to print out the data and ui.
    data_dict = importer()
    print("")

def dict_creator(date, weight, walk, gym):
    # Function to make todays dict with data and send to write function.
    # Find out which day it is and make that the dictionaries name
    from datetime import date
    date = date.today()
    day = date.weekday()
     = {}

    today_dict = {}
    today_dict["date"] = f"{date}"
    today_dict["weight"] = weight
    today_dict["walk"] = walk
    today_dict["gym"] = gym

    writer(today_dict)

def data_input():
    from datetime import date
    date = date.today()
    weight = int(input("How much do you weigh? > "))
    walk = float(input("How far did you walk? > "))
    gym = int(input("Did you go to the gym? (1 for yes, 0 for no.) > "))
    dict_creator(date, weight, walk, gym)


data_input()






