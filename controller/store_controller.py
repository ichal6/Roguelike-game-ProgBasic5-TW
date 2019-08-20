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
        choice = terminal_view.get_choice(options)
        if choice == "1":
            new_record = terminal_view.get_inputs(["Title: ", "Manufacturer: ", "Price: ", "In stock: "], "Please enter value: ")
            new_record.insert(0, store.get_random_id(list_of_games))
            print(store.add(list_of_games, new_record))
        elif choice == "2":
            hr_controller.run()
        elif choice == "3":
            inventory_controller.run()
        elif choice == "4":
            accounting_controller.run()
        elif choice == "5":
            sales_controller.run()
        elif choice == "6":
            crm_controller.run()
        elif choice == "0":
            pass
        else:
            terminal_view.print_error_message("There is no such choice.")
