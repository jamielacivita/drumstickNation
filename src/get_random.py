import random

def get_random_food_name():
    with open(r"/home/jamie/PycharmProjects/drumstickNation/data/food_names_random") as f:
        names = f.readlines()
    f.close()
    return random.choice(names)


def get_random_upc():
    """
    :return: a ten digit string of random numbers
    """
    digits = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9"]
    out_string = ""
    for n in range(0,9):
        out_string = out_string + random.choice(digits)

    return out_string

