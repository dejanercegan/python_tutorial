# return the list of random numbers to correct order

def ifelse_numlist(x, y, z):
    """

    :param x: random number
    :param y: random number
    :param z: random number
    :return: correct order of numbers
    """
    result = []

    if x < y and x < z and y < z:
        result.append(x)
        result.append(y)
        result.append(z)
    elif x < y and x < z and z < y:
        result.append(x)
        result.append(z)
        result.append(y)
    elif y < x and y < z and z < x:
        result.append(y)
        result.append(z)
        result.append(x)
    elif y < x and y < z and x < z:
        result.append(y)
        result.append(x)
        result.append(z)
    elif z < y and z < x and x < y:
        result.append(z)
        result.append(x)
        result.append(y)
    else:
        result.append(z)
        result.append(y)
        result.append(x)

    return result
