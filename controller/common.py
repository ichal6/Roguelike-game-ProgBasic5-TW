""" Common functions for controllers
implement commonly used functions here
"""


def check_is_number(number, list_length):
    """Check if given input is number and
    in right partition
    (number) - input from user
    (list length) - int, length of list"""
    try:
        number = int(number)
        if number > 0 and number <= list_length:
            return True
        else:
            return False
    except ValueError:
        return False


def check_id_by_number(list_of_games, number):
    """Check record ID from given line number
    (list of games) - list of id`s
    (number) - int, line number from user"""
    for list_index in range(len(list_of_games)):
        if number == list_index+1:
            return list_of_games[list_index][0]
