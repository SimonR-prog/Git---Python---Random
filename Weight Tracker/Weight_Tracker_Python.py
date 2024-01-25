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
    old_data.update(today_dict)
    new_data = old_data
    with open('weight_data.json', 'w') as f:
        f.write(json.dumps(new_data))

def ui():
    # Function to print out the data and ui.
    data_dict = importer()
    print("")

def dict_creator(date):
    # Function to make todays dict with data and send to write function.
    today_dict = {}
    today_dict["date"] = f"{date}"
    #today_dict["weight"] = weight
    #today_dict["walk"] = walk
    #today_dict["exercise"] = exercise
    writer(today_dict)

def data_input():
    from datetime import date
    date = date.today()
    walk = float(input("How far did you walk? > "))
    exercise = int(input("Did you go to the gym? > "))
    dict_creator(date, walk, exercise)


data_input()



    # Continue;
    # Make the date into the key for the rest of the data.
    # Make it so that only the last week is saved?
    # Can make it so that there are two different dicts,
    # One with the weight difference between first and last day of the week.
    # One with the










