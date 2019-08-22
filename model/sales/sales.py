""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
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

def get_lowest_price_item_id(table):
    """
    Question: What is the id of the item that was sold for the lowest price?
    if there are more than one item at the lowest price, return the last item by alphabetical order of the title

    Args:
        table (list): data table to work on

    Returns:
         string: id
    """

    # your code
    lowest_price = table[0][2]
    list_of_lowest_price_names = []

    for line in table:
        if line[2] < lowest_price:
            lowest_price = line[2]
    
    for line in table:
        if line[2] == lowest_price:
            list_of_lowest_price_names.append(line[0])
    return list_of_lowest_price_names[0]


def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    """
    Question: Which items are sold between two given dates? (from_date < sale_date < to_date)

    Args:
        table (list): data table to work on
        month_from (int)
        day_from (int)
        year_from (int)
        month_to (int)
        day_to (int)
        year_to (int)

    Returns:
        list: list of lists (the filtered table)
    """

    # your code
    filtered_table = []

    start_time_range = (int(month_from) * 31 + int(day_from) + int(year_from) * 365)
    end_time_range = (int(month_to) * 31 + int(day_to) + int(year_to) * 365)
    time_range = list(range(start_time_range + 1 , end_time_range))

    # start_time_range = (int(month_from) * 31 + int(day_from) + int(year_from) * 365)
    # end_time_range = (int(month_to) * 31 + int(day_to) + int(year_to) * 365)
    # time_range = list(range(start_time_range + 1 , end_time_range))


    for item in range(len(table)):
        if ((int(table[item][5]) * 365) + (int(table[item][3]) * 31) + int(table[item][4])) in time_range:
            filtered_table.append(table[item])

    for line in filtered_table:
        line[2] = int(line[2])
        line[3] = int(line[3])
        line[4] = int(line[4])
        line[5] = int(line[5])
    
    return filtered_table


def get_data_to_list():
    return data_manager.get_table_from_file("model/sales/sales.csv")


def get_random_id(table):
    return common.generate_random(table)


def export_list_to_file(table):
    data_manager.write_table_to_file("model/sales/sales.csv", table)
