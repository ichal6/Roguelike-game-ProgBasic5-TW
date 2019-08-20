""" Common functions for models
implement commonly used functions here
"""
import random


def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """

    generated = ''
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    letter1 = random.choice('abcdefghijklmnopqrstuvwxyz')
    letter2 = random.choice('abcdefghijklmnopqrstuvwxyz')
    capital_letter1 = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    capital_letter2 = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    # your code

    return generated

def remove(table, id_):

    for i in table:
        if i[0] == id_[0]:
            table.remove(i)

    return table


