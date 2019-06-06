# return the list of random numbers to correct order

def ifelse_numlist(arg_ifelse):
    """
    Changes all strings in a list to upercase
    :param arg_ifelse: List of random numbers
    :return: List of random numbers in correct order
    """
    result = []

    x = int(input("1st num"))
    y = int(input("2nd num"))
    z = int(input("3rd num"))

    for num_list in arg_ifelse:
        if x > y and y > z:
            print (['x', 'y', 'z'])

    return result
