""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
"""

# everything you'll need is imported:
from model import data_manager
from model import common


def add(table, record):
    """
    Add new record to table

    Args:
        table (list): table to add new record to
        record (list): new record

    Returns:
        list: Table with a new record
    """
    # your code

    return common.add(table, record)


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    # your code

    return common.remove(table, id_)


def update(table, id_, record):
    """
    Updates specified record in the table.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update
        record (list): updated record

    Returns:
        list: table with updated record
    """

    # your code

    return common.update(table, id_, record)


# special functions:
# ------------------

def get_counts_by_manufacturers(table):
    """
    Question: How many different kinds of game are available of each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
         dict: A dictionary with this structure: { [manufacturer] : [count] }
    """

    # your code
    output = {}

    for key in table:
        if key[2] not in output.keys():
            output[key[2]] = 1
        else:
            output[key[2]] += 1

    return output

def get_average_by_manufacturer(table, manufacturer):
    """
    Question: What is the average amount of games in stock of a given manufacturer?

    Args:
        table (list): data table to work on
        manufacturer (str): Name of manufacturer

    Returns:
         number
    """

    # your code

    game_counter = 0
    manufacturer_counter = 0

    for i in range(len(table)):
        if manufacturer in table[i][2]:
            game_counter += float(table[i][4])
            manufacturer_counter += 1
    aver = game_counter / manufacturer_counter
    return round(aver, 2)


def get_data_to_list():
    return data_manager.get_table_from_file("model/store/games.csv")


def get_random_id(table):
    return common.generate_random(table)


def export_list_to_file(table):
    data_manager.write_table_to_file("model/store/games.csv", table)

