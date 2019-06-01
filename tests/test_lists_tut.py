import src.lists_tut as lists_tut

def test_change_to_uppercase():
    """

    :return:
    """
    assert(['TEST', 'TE_ST'] == lists_tut.change_to_uppercase(['tEsT','TE_St']))
    assert(['TEST'] == lists_tut.change_to_uppercase(['tEsT']))
    assert(['/////AAA'] == lists_tut.change_to_uppercase(['/////AAA']))