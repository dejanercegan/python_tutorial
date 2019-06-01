# change every member of the list to uppercase

def change_to_uppercase(arg_list):
    """
    Changes all strings in a list to upercase
    :param arg_list: List with strings
    :return: List with uppercase strings
    """
    result = []

    for element_list in arg_list:
        result.append(element_list.upper())

    return result
