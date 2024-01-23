import json
import datetime


def importer():
    with open('weight_data.txt') as f:
        data_list = f.read()
    return data_list

def writer(today_dict):
    # Function to write the information to the
    data_list = importer()
    with open('weight_data.txt', 'w') as f:
        f.write(data_list + today_dict)

def ui():
    # Function to print out the data and ui.
    data_list = importer()
    print("")

def dict_creator(date, weight, walk, exercise):
    # Function to make todays dict with data and send to write function.
    today_dict = {}
    today_dict["date"] = date
    today_dict["weight"] = weight
    today_dict["walk"] = walk
    today_dict["exercise"] = exercise
    writer(today_dict)

def data_input():
    from datetime import date
    date = date.today()



    # COntinue;
    # Make the date into the key for the rest of the data.










