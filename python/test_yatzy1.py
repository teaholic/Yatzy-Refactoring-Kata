from yatzy1 import Yatzy


# These unit tests can be run using the py.test framework
# available from http://pytest.org/

def test_chance_scores_sum_of_all_dice():

    assert 15 == Yatzy(2, 3, 4, 5, 1).chance()
    assert 16 == Yatzy(3, 3, 4, 5, 1).chance()


def test_yatzy_scores_50():
    assert 50 == Yatzy(4, 4, 4, 4, 4).yatzy()
    assert 50 == Yatzy(6, 6, 6, 6, 6).yatzy()
    assert 0 == Yatzy(6, 6, 6, 6, 3).yatzy()


def test_ones():
    assert 1 == Yatzy(1, 2, 3, 4, 5).ones()
    assert 2 == Yatzy(1, 2, 1, 4, 5).ones()
    assert 0 == Yatzy(6, 2, 2, 4, 5).ones()
    assert 4 == Yatzy(1, 2, 1, 1, 1).ones()


def test_twos():
    assert 4 == Yatzy(1, 2, 3, 2, 6).twos()
    assert 10 == Yatzy(2, 2, 2, 2, 2).twos()


def test_threes():
    assert 6 == Yatzy(1, 2, 3, 2, 3).threes()
    assert 12 == Yatzy(2, 3, 3, 3, 3).threes()


def test_fours():
    assert 12 == Yatzy(4, 4, 4, 5, 5).fours()
    assert 8 == Yatzy(4, 4, 5, 5, 5).fours()
    assert 4 == Yatzy(4, 5, 5, 5, 5).fours()


def test_fives():
    assert 10 == Yatzy(4, 4, 4, 5, 5).fives()
    assert 15 == Yatzy(4, 4, 5, 5, 5).fives()
    assert 20 == Yatzy(4, 5, 5, 5, 5).fives()


def test_sixes():
    assert 0 == Yatzy(4, 4, 4, 5, 5).sixes()
    assert 6 == Yatzy(4, 4, 6, 5, 5).sixes()
    assert 18 == Yatzy(6, 5, 6, 6, 5).sixes()


def test_one_pair():
    assert 6 == Yatzy(3, 4, 3, 5, 6).one_pair()
    assert 10 == Yatzy(5, 3, 3, 3, 5).one_pair()
    assert 12 == Yatzy(5, 3, 6, 6, 5).one_pair()


def test_two_pairs():
    assert 16 == Yatzy(3, 3, 5, 4, 5).two_pairs()
    assert 18 == Yatzy(3, 3, 6, 6, 6).two_pairs()
    assert 0 == Yatzy(3, 3, 6, 5, 4).two_pairs()


def test_three_of_a_kind():
    assert 9 == Yatzy(3, 3, 3, 4, 5).three_of_a_kind()
    assert 15 == Yatzy(5, 3, 5, 4, 5).three_of_a_kind()
    assert 9 == Yatzy(3, 3, 3, 3, 5).three_of_a_kind()


def test_four_of_a_knd():
    assert 12 == Yatzy(3, 3, 3, 3, 5).four_of_a_kind()
    assert 20 == Yatzy(5, 5, 5, 4, 5).four_of_a_kind()
    assert 12 == Yatzy(3, 3, 3, 3, 3).four_of_a_kind()
    assert 0 == Yatzy(3, 3, 3, 2, 1).four_of_a_kind()


def test_smallStraight():
    assert 15 == Yatzy.smallStraight(1, 2, 3, 4, 5)
    assert 15 == Yatzy.smallStraight(2, 3, 4, 5, 1)
    assert 0 == Yatzy.smallStraight(1, 2, 2, 4, 5)


def test_largeStraight():
    assert 20 == Yatzy.largeStraight(6, 2, 3, 4, 5)
    assert 20 == Yatzy.largeStraight(2, 3, 4, 5, 6)
    assert 0 == Yatzy.largeStraight(1, 2, 2, 4, 5)


def test_fullHouse():
    assert 18 == Yatzy.fullHouse(6, 2, 2, 2, 6)
    assert 0 == Yatzy.fullHouse(2, 3, 4, 5, 6)
