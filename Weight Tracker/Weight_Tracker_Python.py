import json
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
    new_data = ""
    with open('weight_summary.json', 'w') as f:
        f.write(json.dumps(new_data))

    """ Need to find out which week it is and to take the weight of the first and last
     day of the previous week and log the difference into a dictionary with the week
     as the key to the value (weight)."""


def ui():
    # Function to print out the data and ui.
    data_dict = importer()
    print("")

def current_week():
    # Function to return current week.
    from datetime import date
    week = date.today().isocalendar()[1]
    return week

def current_day():
    # Function to return current day.
    from datetime import date
    date = date.today()
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day = weekdays[(date.weekday())]
    return day

def dict_creator(weight, walk, gym):
    # Function to add today's data to the variables and add them to the dictionary.
    # Need to have one dict for each week as well inside another dict that sums up the data for that week.


    day = current_day()
    dict_todays_data = {}
    dict_todays_data[day] = {}
    # Inserting data as values to keys;
    dict_todays_data[day]["weight"] = weight
    dict_todays_data[day]["walk"] = walk
    dict_todays_data[day]["gym"] = gym
    # Sending todays updated data to the next function.
    writer(dict_todays_data)

def data_input():
    weight = int(input("How much do you weigh? > "))
    walk = float(input("How far did you walk? > "))
    gym = int(input("Did you go to the gym? (1 for yes, 0 for no.) > "))
    dict_creator(weight, walk, gym)


data_input()






