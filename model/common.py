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
    special_character1 = random.choice('!#$%&*+-<?@^_~')
    special_character2 = random.choice('!#$%&*+-<?@^_~')
    id_raw = (str(number1) + str(number2) + special_character1 + letter1 + capital_letter1 
    + letter2 + special_character2 + capital_letter2)
    id_final = ''.join(random.sample(id_raw, len(id_raw)))

    for line in table :
        if id_final == line[0]:
            return generate_random(table) 


    # your code

    generated = id_final

    return generated


def remove(table, id_):

    for i in table:
        if i[0] == id_:
            table.remove(i)

    return table


def add(table, new_record):
    table.append(new_record)
    return table


def update(table, id_, update_record):
    for i in range(len(table)):
        if table[i][0] == id_:
            table.insert(i, update_record)
            table[i].insert(0, generate_random(table))
            remove(table, table[i+1][0])
    return table
