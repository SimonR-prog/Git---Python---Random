import json
import os

def clear_console():
    # Function to clear the console.
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')

def current_week():
    # Function to return current week.
    from datetime import date
    week = date.today().isocalendar()[1]
    return week

def current_day():
    # Function to return current day.
    from datetime import date
    date = date.today()
    day = (date.weekday())
    return day

def importer():
    # Function to bring in the data from the json file.
    with open('weight_data.json') as f:
        data_dict = f.read()
    data_dict = json.loads(data_dict)
    return data_dict

def writer(today_dict):
    # Function to write the information to the
    # Bringing in old data.
    old_data = importer()
    # Creating new dictionary.
    new_data = {}
    # Adding the old and then new data to the dict.
    new_data.update(old_data)
    new_data.update(today_dict)
    # Writing the dictionary to the json file.
    with open('weight_data.json', 'w') as f:
        f.write(json.dumps(new_data))

def summary():
    # Function that will check if the current weeks data summary is in the json file.

    """ Need to find out which week it is and to take the weight of the first and last
     day of the previous week and log the difference into a dictionary with the week
     as the key to the value (weight)."""

def ui():
    # Function to print out the data and ui.
    data_dict = importer()
    print("")


def dict_creator(weight, walk, gym):
    # Function to add today's data to the variables and add them to the dictionary.

    # Getting current day and week and storing in variables.
    week = current_week()
    day = current_day()


    # Creates the dict to use to send on the data to the writer function.
    dict_todays_data = {}
    # Creates the dict inside that which will hold the dict with the data.
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






