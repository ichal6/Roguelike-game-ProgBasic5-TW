""" Inventory module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string): Name of item
    * manufacturer (string)
    * purchase_year (number): Year of purchase
    * durability (number): Years it can be used
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

def get_available_items(table):
    """
    Question: Which items have not exceeded their durability yet?

    Args:
        table (list): data table to work on

    Returns:
        list: list of lists (the inner list contains the whole row with their actual data types)
    """
    YEAR = 3
    DURABILITY = 4
    for element in table:
        element[4], element[3] = int(element[4]), int(element[3])
    available_items = [table[index] for index in range(len(table)) if table[index][YEAR]+table[index][DURABILITY]>=2017]
    return available_items


def get_average_durability_by_manufacturers(table):
    """
    Question: What are the average durability times for each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
        dict: a dictionary with this structure: { [manufacturer] : [avg] }
    """
    MANUFACTURER = 1
    DURABILITY = 4
    average_durability = {}
    manaufacturers = list(set([table[index][MANUFACTURER] for index in range(len(table))]))
    for manaufacturer in manaufacturers:
        count = 0.0
        sum_durability = 0.0
        for index in range(len(table)):
            if manaufacturer == table[index][MANUFACTURER]:
                count += 1.0
                sum_durability += float(table[index][DURABILITY])
        average_durability.update({manaufacturer: float(sum_durability) / float(count)})
    return average_durability


def get_data_to_list():
    return data_manager.get_table_from_file("model/inventory/inventory.csv")


def get_random_id(table):
    return common.generate_random(table)


def export_list_to_file(table):
    data_manager.write_table_to_file("model/inventory/inventory.csv", table)
