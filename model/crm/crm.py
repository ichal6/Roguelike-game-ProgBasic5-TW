""" Customer Relationship Management (CRM) module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * email (string)
    * subscribed (int): Is she/he subscribed to the newsletter? 1/0 = yes/no
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

def get_longest_name_id(table):
    """
        Question: What is the id of the customer with the longest name?

        Args:
            table (list): data table to work on

        Returns:
            string: id of the longest name (if there are more than one, return
                the last by alphabetical order of the names)
        """

    NAME = 1
    ID = 0
    FIRST_ELEMENT = 0
    LAST_ELEMENT = -1
    longest_names = []
    longest_name = len(table[FIRST_ELEMENT][NAME])
    for index in range(len(table)):
        if len(table[index][NAME]) > longest_name:
            longest_name = len(table[index][NAME])
    for index in range(len(table)):
        if len(table[index][NAME]) == longest_name:
            longest_names.append(table[index][NAME])
    common.insertion(longest_names)
    for index in range(len(table)):
        if table[index][NAME] == longest_names[LAST_ELEMENT]:
            return table[index][ID]



# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):
    """
        Question: Which customers has subscribed to the newsletter?

        Args:
            table (list): data table to work on

        Returns:
            list: list of strings (where a string is like "email;name")
        """
    SUBSCRIBED_CHOICE = 3
    E_MAIL_USER = 2
    NAME_USER = 1
    list_subscribe = []
    for user in table:
        if user[SUBSCRIBED_CHOICE] == "1":
            email_name = "{};{}".format(user[E_MAIL_USER], user[NAME_USER])
            list_subscribe.append(email_name)

    return list_subscribe

    # your code


def get_data_to_list():
    return data_manager.get_table_from_file("model/crm/customers.csv")


def get_random_id(table):
    return common.generate_random(table)


def export_list_to_file(table):
    data_manager.write_table_to_file("model/crm/customers.csv", table)
