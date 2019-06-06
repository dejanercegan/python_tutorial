# return the list of random numbers to correct order

def ifelse_numlist(arg_ifelse):
    """
    Changes all strings in a list to upercase
    :param arg_ifelse: List of random numbers
    :return: List of random numbers in correct order
    """
    result = []

    x = int(input("1st num: "))
    y = int(input("2nd num: "))
    z = int(input("3rd num: "))

    a1 = min(x, y, z)
    a3 = max(x, y, z)
    a2 = (x + y + z) - a1 - a3
    print(a1, a2, a3)
    return result
