from hamcrest import *


def taxi():
    pass

def test_moving_up():
    # assert
    token = 'u'

    # act
    result = taxi((0, 0), token)

    # assert
    assert_that(result, equal_to((0, 1)))
