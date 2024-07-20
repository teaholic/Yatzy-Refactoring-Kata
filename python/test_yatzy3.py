from model import Chance, Yatzy, Match, Repetition, Straight, StraightType, FullHouse
from yatzy3 import YatzyService


# These unit tests can be run using the py.test framework
# available from http://pytest.org/

def test_chance_scores_sum_of_all_dice():

    assert 15 == YatzyService(2, 3, 4, 5, 1).run(category=Chance())
    assert 16 == YatzyService(3, 3, 4, 5, 1).run(category=Chance())


def test_yatzy_scores_50():
    assert 50 == YatzyService(4, 4, 4, 4, 4).run(category=Yatzy())
    assert 50 == YatzyService(6, 6, 6, 6, 6).run(category=Yatzy())
    assert 0 == YatzyService(6, 6, 6, 6, 3).run(category=Yatzy())


def test_ones():
    assert 1 == YatzyService(1, 2, 3, 4, 5).run(category=Match(1))
    assert 2 == YatzyService(1, 2, 1, 4, 5).run(category=Match(1))
    assert 0 == YatzyService(6, 2, 2, 4, 5).run(category=Match(1))
    assert 4 == YatzyService(1, 2, 1, 1, 1).run(category=Match(1))


def test_twos():
    assert 4 == YatzyService(1, 2, 3, 2, 6).run(category=Match(2))
    assert 10 == YatzyService(2, 2, 2, 2, 2).run(category=Match(2))


def test_threes():
    assert 6 == YatzyService(1, 2, 3, 2, 3).run(category=Match(3))
    assert 12 == YatzyService(2, 3, 3, 3, 3).run(category=Match(3))


def test_fours():
    assert 12 == YatzyService(4, 4, 4, 5, 5).run(category=Match(4))
    assert 8 == YatzyService(4, 4, 5, 5, 5).run(category=Match(4))
    assert 4 == YatzyService(4, 5, 5, 5, 5).run(category=Match(4))


def test_fives():
    assert 10 == YatzyService(4, 4, 4, 5, 5).run(category=Match(5))
    assert 15 == YatzyService(4, 4, 5, 5, 5).run(category=Match(5))
    assert 20 == YatzyService(4, 5, 5, 5, 5).run(category=Match(5))


def test_sixes():
    assert 0 == YatzyService(4, 4, 4, 5, 5).run(category=Match(6))
    assert 6 == YatzyService(4, 4, 6, 5, 5).run(category=Match(6))
    assert 18 == YatzyService(6, 5, 6, 6, 5).run(category=Match(6))


def test_one_pair():
    assert 6 == YatzyService(3, 4, 3, 5, 6).run(category=Repetition(same_number_times=2, frequency=1))
    assert 10 == YatzyService(5, 3, 3, 3, 5).run(category=Repetition(same_number_times=2, frequency=1))
    assert 12 == YatzyService(5, 3, 6, 6, 5).run(category=Repetition(same_number_times=2, frequency=1))


def test_two_pairs():
    assert 16 == YatzyService(3, 3, 5, 4, 5).run(category=Repetition(same_number_times=2, frequency=2))
    assert 18 == YatzyService(3, 3, 6, 6, 6).run(category=Repetition(same_number_times=2, frequency=2))
    assert 0 == YatzyService(3, 3, 6, 5, 4).run(category=Repetition(same_number_times=2, frequency=2))


def test_three_of_a_kind():
    assert 9 == YatzyService(3, 3, 3, 4, 5).run(category=Repetition(same_number_times=3, frequency=1))
    assert 15 == YatzyService(5, 3, 5, 4, 5).run(category=Repetition(same_number_times=3, frequency=1))
    assert 9 == YatzyService(3, 3, 3, 3, 5).run(category=Repetition(same_number_times=3, frequency=1))


def test_four_of_a_knd():
    assert 12 == YatzyService(3, 3, 3, 3, 5).run(category=Repetition(same_number_times=4, frequency=1))
    assert 20 == YatzyService(5, 5, 5, 4, 5).run(category=Repetition(same_number_times=4, frequency=1))
    assert 12 == YatzyService(3, 3, 3, 3, 3).run(category=Repetition(same_number_times=4, frequency=1))
    assert 0 == YatzyService(3, 3, 3, 2, 1).run(category=Repetition(same_number_times=4, frequency=1))

def test_smallStraight():
    assert 15 == YatzyService(1, 2, 3, 4, 5).run(category=Straight(straight_type=StraightType.SMALL))
    assert 15 == YatzyService(2, 3, 4, 5, 1).run(category=Straight(straight_type=StraightType.SMALL))
    assert 0 == YatzyService(1, 2, 2, 4, 5).run(category=Straight(straight_type=StraightType.SMALL))

def test_largeStraight():
    assert 20 == YatzyService(6, 2, 3, 4, 5).run(category=Straight(straight_type=StraightType.LARGE))
    assert 20 == YatzyService(2, 3, 4, 5, 6).run(category=Straight(straight_type=StraightType.LARGE))
    assert 0 == YatzyService(1, 2, 2, 4, 5).run(category=Straight(straight_type=StraightType.LARGE))

def test_fullHouse():
    assert 18 == YatzyService(6, 2, 2, 2, 6).run(category=FullHouse())
    assert 0 == YatzyService(2, 3, 4, 5, 6).run(category=FullHouse())
