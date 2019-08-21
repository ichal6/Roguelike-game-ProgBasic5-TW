# everything you'll need is imported:
from model.store import store
from view import terminal_view
from controller import common


def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    list_of_games = store.get_data_to_list()

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
            new_record = terminal_view.get_inputs(["Title: ", "Manufacturer: ", "Price: ", "In stock: "], "Please enter value: ")
            new_record.insert(0, store.get_random_id(list_of_games))
            store.export_list_to_file(store.add(list_of_games, new_record))
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "0":
            pass
        else:
            terminal_view.print_error_message("There is no such choice.")
