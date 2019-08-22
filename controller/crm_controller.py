# everything you'll need is imported:
from view import terminal_view
from model.crm import crm
from controller import common


def ask_untill_correct(list_of_customers):
    is_correct = False
    FIRST_ELEMENT_IN_LIST = 0
    while is_correct is not True:
        id_of_record = terminal_view.get_inputs(["Line number: "], "Please enter value ")
        is_correct = common.check_is_number(id_of_record[FIRST_ELEMENT_IN_LIST], len(list_of_customers))
    return id_of_record[FIRST_ELEMENT_IN_LIST]


def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    list_of_customers = crm.get_data_to_list()

    # your code
    options = ["Add new record",
               "Remove a record",
               "Update record",
               "Id of the customer with the longest name",
               "Customers has subscribed to the newsletter",
               "Print table"]

    title_list = ["ID", "Name", "e-mail", "subscribed"]

    choice = None
    while choice != "0":
        choice = terminal_view.get_choice(options, "Back to main menu")
        if choice == "1":
            new_record = terminal_view.get_inputs(["Name: ", "e-mail: ", "subscribed: "], "Please enter value: ")
            new_record.insert(0, crm.get_random_id(list_of_customers))
            list_of_customers = crm.add(list_of_customers, new_record)
        elif choice == "2":
            id_of_record_to_remove = ask_untill_correct(list_of_customers)
            list_of_customers = crm.remove(list_of_customers, common.check_id_by_number(list_of_customers, int(id_of_record_to_remove)))
        elif choice == "3":
            id_of_record_to_update = ask_untill_correct(list_of_customers)
            updated_record = terminal_view.get_inputs(["Name: ", "e-mail: ", "subscribed: "], "Please enter value: ")
            list_of_customers = crm.update(list_of_customers, common.check_id_by_number(list_of_customers, int(id_of_record_to_update)), updated_record)
        elif choice == "4":
            terminal_view.print_result(crm.get_longest_name_id(list_of_customers), "Longest person's ID")
        elif choice == "5":
            terminal_view.print_result(crm.get_subscribed_emails(list_of_customers), "List of subsrcibe user")
        elif choice == "6":
            terminal_view.print_table(list_of_customers, title_list)
        elif choice == "0":
            crm.export_list_to_file(list_of_customers)
        
        else:
            terminal_view.print_error_message("There is no such choice.")  # your code


    # your code
