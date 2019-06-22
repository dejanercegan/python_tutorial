# return the list of Names

def forwhile_names(a, b, c):
    """

    :param a: Srdjan
    :param b: Branislav
    :param c: Dejan
    :return: "my name is: Srdjan, my name is: Branislav, my name is: Dejan"
    """
    result = []

    names = ["Branislav", "Dejan", "Srdjan"]

    for name in names:
        print(names)

        if name == "Dejan":
            print(f'{name} - sam ja')
        if name == "Branislav":
            print(f'{name} - prijatelj')
        if name == "Srdjan":
            print(f'{name} - moj brat')
        else:
            print(name)

    return result
