# return the list of Names

def forwhile_names(a, b, c):
    """

    :param a: Srdjan
    :param b: Branislav
    :param c: Dejan
    :return: "my name is: Srdjan, my name is: Branislav, my name is: Dejan"
    """
    result = []

    name = ["my name is: "]
    names = ["Dejan", "Branislav", "Srdjan"]

    for x in name:
        for y in names:
            print(x, y)

    return result
