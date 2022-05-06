import random
import json


def random_name():
    name_list = read_file("namelist.json")
    name = random.choice(name_list)
    return name

def read_file(filename):
    file = open(filename,"r")
    file_data = json.load(file)
    file.close()
    return file_data

def write_file(filename,data):
    file = open(filename,"w")
    json.dump(data,file)
    file.close()

