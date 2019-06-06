# return the list of random numbers to correct order

def ifelse_numlist(arg_ifelse):
    """
    Changes all strings in a list to upercase
    :param arg_ifelse: List of random numbers
    :return: List of random numbers in correct order
    """
    result = []

    x = int(input("num1"))
    y = int(input("num2"))
    z = int(input("num3"))
    if x < y and x < z and y < z:
        print(x)
        print(y)
        print(z)
    elif x < y and x < z and z < y:
        print(x)
        print(z)
        print(y)
    elif y < x and y < z and z < x:
        print(y)
        print(z)
        print(x)
    elif y < x and y < z and x < z:
        print(y)
        print(x)
        print(z)
    elif z < y and z < x and x < y:
        print(z)
        print(x)
        print(y)
    else:
        print(z)
        print(y)
        print(x)

    return result
