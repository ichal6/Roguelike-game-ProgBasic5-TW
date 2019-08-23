""" Accounting module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * month (number): Month of the transaction
    * day (number): Day of the transaction
    * year (number): Year of the transaction
    * type (string): in = income, out = outflow
    * amount (int): amount of transaction in USD
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

def which_year_max(table):
    """
    Question: Which year has the highest profit? (profit = in - out)

    Args:
        table (list): data table to work on

    Returns:
        number
    """
    # your code
    YEAR_START = 1
    YEAR_STOP = 2100
    YEAR_INDEX = 3
    IN_OUT_INDEX = 4
    COST_INDEX = 5
    actual_year = 1
    max_profit = 0
    return_year = 0
    profit = 0
    for actual_year in range(YEAR_START, YEAR_STOP):
        profit = 0
        for row in table:
            if int(row[YEAR_INDEX]) == actual_year:
                if row[IN_OUT_INDEX] == "in":
                    profit += int(row[COST_INDEX])
                else:
                    profit -= int(row[COST_INDEX])

        if profit > max_profit:
            max_profit = profit
            return_year = actual_year

    return return_year


def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    """
    # your code
    YEAR_INDEX = 3
    IN_OUT_INDEX = 4
    PROFIT_INDEX = 5
    profit = 0
    count = 0
    averange = 0
    for row in table:
        if int(row[YEAR_INDEX]) == year:
            count += 1
            if row[IN_OUT_INDEX] == "in":
                profit += int(row[PROFIT_INDEX])
            else:
                profit -= int(row[PROFIT_INDEX])
    if count != 0:
        averange = profit / count

    return round(averange, 4)


def get_data_to_list():
    return data_manager.get_table_from_file("model/accounting/items.csv")


def get_random_id(table):
    return common.generate_random(table)


def export_list_to_file(table):
    data_manager.write_table_to_file("model/accounting/items.csv", table)
