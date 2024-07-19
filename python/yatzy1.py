from dataclasses import dataclass
from enum import IntEnum
from typing import List, Optional, Union, Any


@dataclass(frozen=True)
class Dice:
    values: List[int]


class StraightType(IntEnum):
    SMALL = 0
    LARGE = 1

@dataclass(frozen=True)
class HowManyOfAKind:
    same_number_times: int
    frequency: int


@dataclass(frozen=True)
class StraightCategory:
    values: Optional[List[int]] = None
    win_score: Optional[int]=None
    loose_score: int = 0


@dataclass(frozen=True)
class RepetitionCategory:
    how_many_of_a_kind: Optional[List[HowManyOfAKind]] = None
    win_function: Optional[Union[int, Any]]=None
    loose_score: int = 0


class RuleBook:
    def __init__(self, dice:Dice):
        self.dice = dice

    @staticmethod
    def small_straight() -> StraightCategory:
        return StraightCategory(values=[1, 2, 3, 4, 5], win_score=15)

    @staticmethod
    def large_straight() -> StraightCategory:
        return StraightCategory(values=[2, 3, 4, 5, 6], win_score=20)

    @staticmethod
    def two_of_a_kind() -> RepetitionCategory:
        return RepetitionCategory(
            how_many_of_a_kind=[HowManyOfAKind(same_number_times=2, frequency=1)],
            win_function=lambda repeated_number: repeated_number*2
        )

    @staticmethod
    def full_house() -> RepetitionCategory:
        return RepetitionCategory(
            how_many_of_a_kind=[
                HowManyOfAKind(same_number_times=2, frequency=1),
                HowManyOfAKind(same_number_times=3, frequency=1)
            ],
            win_function=lambda partial_scores: sum(partial_scores)
        )

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
        straight = self.small_straight() if straight_type is StraightType.SMALL else self.large_straight()
        matches = set([i for i, j in zip(straight.values, sorted(self.dice.values)) if i == j])
        print(matches)
        if len(matches) == len(straight.values):
            return straight.win_score
        else:
            return straight.loose_score

    def score_full_house(self):
        if len(set(self.dice.values)) == len(self.full_house().how_many_of_a_kind):
            partial_scores = [self.score_multiple_combinations(same_number_times=k.same_number_times, frequency=k.frequency) for k in self.full_house().how_many_of_a_kind]
            if all(partial_scores):
                return self.full_house().win_function(partial_scores)
        return self.full_house().loose_score


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

    def fullHouse(self):
        return self.rule_book.score_full_house()
