""" Human resources module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * birth_year (number)
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

def get_oldest_person(table):
    """
    Question: Who is the oldest person?

    Args:
        table (list): data table to work on

    Returns:
        list: A list of strings (name or names if there are two more with the same value)
    """
    YEAR = 2
    NAME = 1
    FIRST_LINE = 0
    oldest_year = int(table[FIRST_LINE][YEAR])
    for index in range(len(table)):
        if int(table[index][YEAR]) < oldest_year:
            oldest_year = int(table[index][YEAR])

    oldest_persons_names = [table[index][NAME] for index in range(len(table)) if int(table[index][YEAR]) == oldest_year]

    return oldest_persons_names


def get_persons_closest_to_average(table):
    """
    Question: Who is the closest to the average age?

    Args:
        table (list): data table to work on

    Returns:
        list: list of strings (name or names if there are two more with the same value)
    """
    YEAR = 2
    FIRST_LINE = 0
    NAME = 1
    sum_of_years = 0
    for index in range(len(table)):
        sum_of_years += int(table[index][YEAR])
    avg = sum_of_years / len(table)

    difference_from_avg = abs(avg - int(table[FIRST_LINE][YEAR]))
    for index in range(len(table)):
        if difference_from_avg > abs(avg - int(table[index][YEAR])):
            difference_from_avg = abs(avg - int(table[index][YEAR]))
    closest_persons_to_avg = [table[index][NAME] for index in range(len(table)) if abs(avg-int(table[index][YEAR])) == difference_from_avg]
    return closest_persons_to_avg


def get_data_to_list():
    return data_manager.get_table_from_file("model/hr/persons.csv")


def get_random_id(table):
    return common.generate_random(table)


def export_list_to_file(table):
    data_manager.write_table_to_file("model/hr/persons.csv", table)

