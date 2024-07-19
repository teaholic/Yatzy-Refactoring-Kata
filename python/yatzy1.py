from dataclasses import dataclass
from enum import IntEnum
from typing import List


@dataclass(frozen=True)
class Dice:
    values: List[int]


class StraightType(IntEnum):
    SMALL = 0
    LARGE = 1


@dataclass(frozen=True)
class Straight:
    values: List[int]
    win_score: int
    loose_score: int = 0


class RuleBook:
    def __init__(self, dice:Dice):
        self.dice = dice
        self.small_straight = Straight(values=[1,2,3,4,5], win_score=15)
        self.large_straight = Straight(values=[2,3,4,5,6], win_score=20)

    def score_matching(self, number) -> int:
        return sum([v for v in self.dice.values if v == number])

    def score_multiple_combinations(self, same_number_times:int, frequency:int):
        counts = [[n, self.dice.values.count(n)] for n in set(self.dice.values)]
        candidates = [n for n, times in counts if times >= same_number_times]
        match = sorted(candidates, reverse=True)[:frequency]
        if len(match) >= frequency:
            return sum([n * same_number_times for n in match])
        return 0

    def score_straight(self, straight_type: StraightType) -> int:
        straight = self.small_straight if straight_type is StraightType.SMALL else self.large_straight
        matches = set([i for i, j in zip(straight.values, sorted(self.dice.values)) if i == j])
        print(matches)
        if len(matches) == len(straight.values):
            return straight.win_score
        else:
            return straight.loose_score


class Yatzy:

    def __init__(self, d1:int=0, d2:int=0, d3:int=0, d4:int=0, d5:int=0):
        self.dice = Dice(values=[d1,d2,d3,d4,d5])
        self.rule_book = RuleBook(self.dice)

    def chance(self) -> int:
        return sum(self.dice.values)

    def yatzy(self) -> int:
        if len(set(self.dice.values)) == 1:
            return 50
        return 0

    def ones(self):
        return self.rule_book.score_matching(1)

    def twos(self):
        return self.rule_book.score_matching(2)

    def threes(self):
        return self.rule_book.score_matching(3)

    def fours(self):
        return self.rule_book.score_matching(4)

    def fives(self):
        return self.rule_book.score_matching(5)

    def sixes(self):
        return self.rule_book.score_matching(6)

    def one_pair(self):
        return self.rule_book.score_multiple_combinations(same_number_times = 2, frequency = 1)

    def two_pairs(self):
        return self.rule_book.score_multiple_combinations(same_number_times=2, frequency=2)

    def three_of_a_kind(self):
        return self.rule_book.score_multiple_combinations(same_number_times=3, frequency=1)

    def four_of_a_kind(self):
        return self.rule_book.score_multiple_combinations(same_number_times = 4, frequency = 1)

    def smallStraight(self):
        return self.rule_book.score_straight(straight_type=StraightType.SMALL)

    def largeStraight(self):
        return self.rule_book.score_straight(straight_type=StraightType.LARGE)

    @staticmethod
    def fullHouse(d1, d2, d3, d4, d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1

        for i in range(6):
            if (tallies[i] == 2):
                _2 = True
                _2_at = i + 1

        for i in range(6):
            if (tallies[i] == 3):
                _3 = True
                _3_at = i + 1

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0
