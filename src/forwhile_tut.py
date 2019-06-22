# return the list of Names

def forwhile_names(a, b, c):
    """

    :param a: Srdjan
    :param b: Branislav
    :param c: Dejan
    :return:
    """
    result = []

    names = ["Branislav", "Dejan", "Srdjan"]

    for name in names:
        result.append(names)

        if name == "Dejan":
            result.append(f'{name} - sam ja')
        if name == "Branislav":
            result.append(f'{name} - prijatelj')
        if name == "Srdjan":
            result.append(f'{name} - moj brat')
        else:
            result.append(name)

    return result
