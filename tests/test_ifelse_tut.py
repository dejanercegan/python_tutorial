import src.ifelse_tut as ifelse_tut

def test_ifelse_numlist():
    """

    :return:
    """
    assert(ifelse_tut.ifelse_numlist(['x', 'z', 'y']) == (['x', 'y', 'z']))