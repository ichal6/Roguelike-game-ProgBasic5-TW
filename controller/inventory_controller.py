# everything you'll need is imported:
from view import terminal_view
from model.inventory import inventory
from controller import common


def ask_untill_correct(list_of_inventory):
    is_correct = False
    FIRST_ELEMENT_IN_LIST = 0
    while is_correct is not True:
        id_of_record = terminal_view.get_inputs(["Line number: "], "Please enter value ")
        is_correct = common.check_is_number(id_of_record[FIRST_ELEMENT_IN_LIST], len(list_of_inventory))
    return id_of_record[FIRST_ELEMENT_IN_LIST]


def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    list_of_inventory = inventory.get_data_to_list()

    # your code
    options = ["Add new record",
               "Remove a record",
               "Update record",
               "Display available items",
               "Get average durability by manufacturers"]

    choice = None
    while choice != "0":
        choice = terminal_view.get_choice(options, "Back to main menu")
        if choice == "1":
            new_record = terminal_view.get_inputs(["Name: ", "Manufacturer: ", "Purchase year: ", "Durability: "], "Please enter value: ")
            new_record.insert(0, inventory.get_random_id(list_of_inventory))
            list_of_inventory = inventory.add(list_of_inventory, new_record)
        elif choice == "2":
            id_of_record_to_remove = ask_untill_correct(list_of_inventory)
            list_of_inventory = inventory.remove(list_of_inventory, common.check_id_by_number(list_of_inventory, int(id_of_record_to_remove)))
        elif choice == "3":
            id_of_record_to_update = ask_untill_correct(list_of_inventory)
            updated_record = terminal_view.get_inputs(["Name: ", "Manufacturer: ", "Purchase year: ", "Durability: "], "Please enter value: ")
            list_of_inventory = inventory.update(list_of_inventory, common.check_id_by_number(list_of_inventory, int(id_of_record_to_update)), updated_record)
        elif choice == "4":
            available_items = inventory.get_available_items(list_of_inventory)
            terminal_view.print_result(available_items, "Available items")
        elif choice == "5":
            average_durability = inventory.get_average_durability_by_manufacturers(list_of_inventory)
            terminal_view.print_result(average_durability, "Average durability by manufacturers")
        elif choice == "0":
            inventory.export_list_to_file(list_of_inventory)
        else:
            terminal_view.print_error_message("There is no such choice.")