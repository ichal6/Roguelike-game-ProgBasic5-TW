# everything you'll need is imported:
from view import terminal_view
from model.sales import sales
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
    list_of_games = sales.get_data_to_list()

    # your code
    options = ["Add new record",
               "Remove a record",
               "Update record",
               "Id of the item that was sold for the lowest price",
               "Items are sold between two given dates",
               "Print table"]

    choice = None

    title_list = ["ID", "TITLE", "SALES", "MONTH", "DAY", "YEAR"]

    while choice != "0":
        # terminal_view.print_table(table, title_list
        choice = terminal_view.get_choice(options, "Back to main menu")
        if choice == "1":
            new_record = terminal_view.get_inputs(["Title: ", "Price: ", "Month: ", "Day: ", "Year: "], "Please enter value: ")
            new_record.insert(0, sales.get_random_id(list_of_games))
            list_of_games = sales.add(list_of_games, new_record)
        elif choice == "2":
            id_of_record_to_remove = ask_untill_correct(list_of_games)
            list_of_games = sales.remove(list_of_games, common.check_id_by_number(list_of_games, int(id_of_record_to_remove)))
        elif choice == "3":
            id_of_record_to_update = ask_untill_correct(list_of_games)
            updated_record = terminal_view.get_inputs(["Title: ", "Price: ", "Month: ", "Day: ", "Year: "], "Please enter value: ")
            list_of_games = sales.update(list_of_games, common.check_id_by_number(list_of_games, int(id_of_record_to_update)), updated_record)
        elif choice == "4":
            label = "What is the id of the item that was sold for the lowest price?"
            result = str(sales.get_lowest_price_item_id(list_of_games))
            terminal_view.print_result(result, label)
        elif choice == "5":
            label = "Which items are sold between two given dates? (from_date < sale_date < to_date)"
            month_from = terminal_view.get_inputs(['Month from'], "Please give starting month.")
            day_from = terminal_view.get_inputs(['Day from'], "Please give starting day.")
            year_from = terminal_view.get_inputs(['Year from'], "Please give starting year.")
            month_to = terminal_view.get_inputs(['Month to'], "Please give ending month.")
            day_to = terminal_view.get_inputs(['Day to'], "Please give ending day.")
            year_to = terminal_view.get_inputs(['Year to'], "Please give ending year.")
            month_from = int(month_from[0])
            day_from = int(day_from[0])  
            year_from = int(year_from[0])
            month_to = int(month_to[0])
            day_to = int(day_to[0])
            year_to = int(year_to[0])
            result = str(sales.get_items_sold_between(list_of_games, month_from, day_from, year_from, month_to, day_to, year_to))
            terminal_view.print_result(result, label)
        elif choice == "6":
            terminal_view.print_table(list_of_games, title_list)
        elif choice == "0":
            sales.export_list_to_file(list_of_games)
        else:
            terminal_view.print_error_message("There is no such choice.")  #
