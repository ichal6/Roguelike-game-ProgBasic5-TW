# everything you'll need is imported:
from view import terminal_view
from model.hr import hr
from controller import common


def ask_untill_correct(list_of_humans):
    is_correct = False
    FIRST_ELEMENT_IN_LIST = 0
    while is_correct is not True:
        id_of_record = terminal_view.get_inputs(["Line number: "], "Please enter value ")
        is_correct = common.check_is_number(id_of_record[FIRST_ELEMENT_IN_LIST], len(list_of_humans))
    return id_of_record[FIRST_ELEMENT_IN_LIST]


def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    list_of_humans = hr.get_data_to_list()

    # your code
    options = ["Add new record",
               "Remove a record",
               "Update record",
               "Search oldest persons",
               "Search persons closest to average"]

    choice = None
    while choice != "0":
        choice = terminal_view.get_choice(options, "Back to main menu")
        if choice == "1":
            new_record = terminal_view.get_inputs(["Name: ", "Birthyear: "], "Please enter value: ")
            new_record.insert(0, hr.get_random_id(list_of_humans))
            list_of_humans = hr.add(list_of_humans, new_record)
        elif choice == "2":
            id_of_record_to_remove = ask_untill_correct(list_of_humans)
            list_of_humans = hr.remove(list_of_humans, common.check_id_by_number(list_of_humans, int(id_of_record_to_remove)))
        elif choice == "3":
            id_of_record_to_update = ask_untill_correct(list_of_humans)
            updated_record = terminal_view.get_inputs(["Name: ", "Birthyear: "], "Please enter value: ")
            list_of_humans = hr.update(list_of_humans, common.check_id_by_number(list_of_humans, int(id_of_record_to_update)), updated_record)
        elif choice == "4":
            oldest_persons = hr.get_oldest_person(list_of_humans)
            terminal_view.print_result(oldest_persons, "List of oldest persons")
        elif choice == "5":
            pass
        elif choice == "0":
            hr.export_list_to_file(list_of_humans)
        else:
            terminal_view.print_error_message("There is no such choice.")
