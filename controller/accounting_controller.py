# everything you'll need is imported:
from view import terminal_view
from model.accounting import accounting
from controller import common

def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    '''
    list_of_games = accounting.get_data_to_list()

    # your code
    options = ["Add new record",
               "Remove a record",
               "Update record",
               "Count games each manufacturer",
               "Average of games"]

    choice = None
    while choice != "0":
        choice = terminal_view.get_choice(options, "Back to main menu")
        if choice == "1":
            new_record = terminal_view.get_inputs(["Month: ", "Day: ", "Year: ", "Type: ", "Amount: "], "Please enter value: ")
            new_record.insert(0, accounting.get_random_id(list_of_games))
            list_of_games = accounting.add(list_of_games, new_record)
            accounting.export_list_to_file(list_of_games)
        elif choice == "2":
            pass
        elif choice == "3":
            index_to_edit = terminal_view.get_inputs(["Index"], "Please insert a index of title to edit") - 1
            
            update_record = terminal_view.get_inputs(["Month: ", "Day: ", "Year: ", "Type: ", "Amount: "], "Please enter value: ")
            update_record.insert(0, accounting.get_random_id(list_of_games))
            list_of_games = accounting.update(list_of_games, index_to_edit, update_record)
            accounting.export_list_to_file(list_of_games)
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "0":
            pass
        else:
            terminal_view.print_error_message("There is no such choice.")

    # your code
'''
