# everything you'll need is imported:
from model.store import store
from view import terminal_view
from controller import common


def ask_untill_correct(list_of_games):
    is_correct = False
    FIRST_ELEMENT_IN_LIST = 0
    while is_correct is not True:
        id_of_record = terminal_view.get_inputs(["Line number: "], "Please enter value ")
        is_correct = common.check_is_number(id_of_record[FIRST_ELEMENT_IN_LIST], len(list_of_games))
    return id_of_record[FIRST_ELEMENT_IN_LIST]


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

    title_list = ["ID", "TITLE", "MANUFACTURER", "PRICE", "IN STOCK"]

    while choice != "0":
        choice = terminal_view.get_choice(options, "Back to main menu")
        if choice == "1":
            new_record = terminal_view.get_inputs(["Title: ", "Manufacturer: ", "Price: ", "In stock: "], "Please enter value: ")
            new_record.insert(0, store.get_random_id(list_of_games))
            list_of_games = store.add(list_of_games, new_record)
        elif choice == "2":
            id_of_record_to_remove = ask_untill_correct(list_of_games)
            list_of_games = store.remove(list_of_games, common.check_id_by_number(list_of_games, int(id_of_record_to_remove)))
        elif choice == "3":
            id_of_record_to_update = ask_untill_correct(list_of_games)
            updated_record = terminal_view.get_inputs(["Title: ", "Manufacturer: ", "Price: ", "In stock: "], "Please enter value: ")
            list_of_games = store.update(list_of_games, common.check_id_by_number(list_of_games, int(id_of_record_to_update)), updated_record)
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "0":
            store.export_list_to_file(list_of_games)
        elif choice == "*":
            terminal_view.print_table(list_of_games, title_list)
        else:
            terminal_view.print_error_message("There is no such choice.")
