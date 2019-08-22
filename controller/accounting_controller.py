# everything you'll need is imported:
from view import terminal_view
from model.accounting import accounting
from controller import common


def ask_untill_correct():
    is_correct = False
    FIRST_ELEMENT_IN_LIST = 0
    MAX_YEAR = 2020
    while is_correct is not True:
        id_of_record = terminal_view.get_inputs(["Year of publishing: "], "Please enter value ")
        is_correct = common.check_is_number(id_of_record[FIRST_ELEMENT_IN_LIST], MAX_YEAR)
    return int(id_of_record[FIRST_ELEMENT_IN_LIST])


def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    list_of_accounting = accounting.get_data_to_list()

    # your code
    options = ["Add new record",
               "Remove a record",
               "Update record",
               "Which year has the highest profit?",
               "What is the average per item"]

    choice = None
    while choice != "0":
        choice = terminal_view.get_choice(options, "Back to main menu")
        if choice == "1":
            new_record = terminal_view.get_inputs(["Month: ", "Day: ", "Year: ", "Type: ", "Amount :"], "Please enter value: ")
            new_record.insert(0, accounting.get_random_id(list_of_accounting))
            list_of_accounting = accounting.add(list_of_accounting, new_record)
        elif choice == "2":
            id_of_record_to_remove = ask_untill_correct()
            list_of_accounting = accounting.remove(list_of_accounting, common.check_id_by_number(list_of_accounting, int(id_of_record_to_remove)))
        elif choice == "3":
            id_of_record_to_update = ask_untill_correct()
            updated_record = terminal_view.get_inputs(["Month: ", "Day: ", "Year: ", "Type: ", "Amount :"], "Please enter value: ")
            list_of_accounting = accounting.update(list_of_accounting, common.check_id_by_number(list_of_accounting, int(id_of_record_to_update)), updated_record)
        elif choice == "4":
            result = accounting.which_year_max(list_of_accounting)
            terminal_view.print_result(str(result), "Year of the highest profile ")
        elif choice == "5":
            year_of_check = ask_untill_correct()
            result = accounting.avg_amount(list_of_accounting, year_of_check)
            terminal_view.print_result(str(result), "Avernage items by year")
        elif choice == "0":
            accounting.export_list_to_file(list_of_accounting)
        else:
            terminal_view.print_error_message("There is no such choice.")  # your code
