""" Terminal view module """

def sum_position(table):
    sum_pos = 0
    for i in range(len(table)):
        sum_pos += float(table[i])

    return sum_pos

def print_table(table, title_list):
    """
    Prints table with data.

    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your goes code
    title_list.insert(0,'NUMBER')

    count = 0

    for row in table:
        count += 1
        row.insert(0, str(count))

    table.insert(0, title_list)

    

    len_col = []
    index = 0
    for row in table:
        len_col.append([])
        for number in range(len(row)):
            longest_name = len(row[number])
            len_col[index].append(longest_name)
        index += 1

    max_line_len = []
    for number in range(len(title_list)):
        max_line_len.append([])
        for col in len_col:
            max_line_len[number].append(col[number])

    max_line_len = [(max(line)) for line in max_line_len]
    max_line = sum_position(max_line_len)

    dashed_line = ("═" * int(max_line + 1 + len(title_list)))
    head = [(title_list[index].rjust(max_line_len[index])+'│') for index in range(len(title_list))]
    header = '│' + ''.join(head)
    table.pop(0)
    print(dashed_line)
    print(header)
    print(dashed_line)
    
    
    for row in table:
        body_list = [(row[index].rjust(max_line_len[index])+'│') for index in range(len(row))]
        body = '│' + ''.join(body_list)
        print(body)
    print(dashed_line)

def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    
    # your code

    if isinstance(result, dict):
        print('{0:>35}'.format(label))
        to_print_a = [[item[0], item[1]] for item in result.items()]
        to_print_b = [('{0:>35} : {1:>1}'.format(item[0], item[1])) for item in to_print_a]
        [print(element) for element in to_print_b]
    elif isinstance(result, list):
        if isinstance(result[0], list):
            print('{0:>20}'.format(label))
            for i in range(len(result)):
                for j in range(len(result[i])):
                    result[i][j] = str(result[i][j])
            for i in result:
                body_list = [('{0:^21}-'.format(i[q])) for q in range(len(i))]
                body = '-' + ''.join(body_list)
                print(body)
        else:
            print('{0:>20}'.format(label))
            [print('{0:>20}'.format(item)) for item in result]

    elif isinstance(result, str):
        print('{} : {}'.format(label, result))
        

def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    print("{}:".format(title))
    for list_index in range(len(list_options)):
        print("\t({}) {}".format(list_index+1, list_options[list_index]))
    print("\t(0) {}".format(exit_message))


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    # your code
    inputs = []

    print(title)
    for label in list_labels:
        data_user = input(label + " ")
        inputs.append(data_user)

    return inputs


def get_choice(options, exit_message):
    print_menu("Main menu", options, exit_message)
    inputs = get_inputs(["Please enter a number: "], "")
    return inputs[0]


def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    print("``Error: @{}``".format(message))
