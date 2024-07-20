from dataclasses import dataclass
from enum import IntEnum
from typing import List


@dataclass(frozen=True)
class Dice:
    values: List[int]

    def number_of_unique_values(self) -> int:
        return len(set(self.values))


class StraightType(IntEnum):
    SMALL = 0
    LARGE = 1


@dataclass(frozen=True)
class StraightCategory:
    values: List[int]
    win_score: int
    loose_score: int = 0


class StraightFactory:
    @staticmethod
    def create(straight_type: StraightType) -> StraightCategory:
        if straight_type is StraightType.SMALL:
            return StraightCategory(values=[1, 2, 3, 4, 5], win_score=15)
        return StraightCategory(values=[2, 3, 4, 5, 6], win_score=20)


@dataclass(frozen=True)
class RepetitionCategory:
    same_number_times: int
    frequency: int
    loose_score: int = 0

    def _win_function(self, repeated_number:int) -> int:
        return repeated_number * self.same_number_times


@dataclass(frozen=True)
class FullHouseCategory:
    categories: List[RepetitionCategory]
    loose_score: int


class FullHouseCategoryFactory:
    @staticmethod
    def create() -> FullHouseCategory:
        return FullHouseCategory(
            categories=[
                RepetitionCategory(same_number_times=2, frequency=1),
                RepetitionCategory(same_number_times=3, frequency=1)
            ],
            loose_score=0
        )


class RuleBook:
    def __init__(self, dice:Dice):
        self.dice = dice
        self.straight_factory = StraightFactory()

    def score_chance(self) -> int:
        return sum(self.dice.values)

    def score_yatzy(self) -> int:
        if len(set(self.dice.values)) == 1:
            return 50
        return 0

    def score_matching(self, number) -> int:
        return sum([v for v in self.dice.values if v == number])

    def score_repetition(self, category:RepetitionCategory):
        counts = [[n, self.dice.values.count(n)] for n in set(self.dice.values)]
        candidates = [n for n, times in counts if times >= category.same_number_times]
        match = sorted(candidates, reverse=True)[:category.frequency]
        if len(match) >= category.frequency:
            return sum([n * category.same_number_times for n in match])
        return 0

    def score_straight(self, straight_type: StraightType) -> int:
        straight = self.straight_factory.create(straight_type=straight_type)
        matches = set([i for i, j in zip(straight.values, sorted(self.dice.values)) if i == j])
        if len(matches) == len(straight.values):
            return straight.win_score
        else:
            return straight.loose_score

    def score_full_house(self):
        full_house = FullHouseCategoryFactory().create()
        if self.dice.number_of_unique_values() == len(full_house.categories):
            partial_scores = [
                self.score_repetition(c)
                for c in full_house.categories]
            if all(partial_scores):
                return sum(partial_scores)
        return full_house.loose_score


class Yatzy:

    def __init__(self, d1:int=0, d2:int=0, d3:int=0, d4:int=0, d5:int=0):
        self.dice = Dice(values=[d1,d2,d3,d4,d5])
        self.rule_book = RuleBook(self.dice)

    def chance(self) -> int:
        return self.rule_book.score_chance()

    def yatzy(self) -> int:
        return self.rule_book.score_yatzy()

    def ones(self) -> int:
        return self.rule_book.score_matching(1)

    def twos(self) -> int:
        return self.rule_book.score_matching(2)

    def threes(self) -> int:
        return self.rule_book.score_matching(3)

    def fours(self) -> int:
        return self.rule_book.score_matching(4)

    def fives(self) -> int:
        return self.rule_book.score_matching(5)

    def sixes(self) -> int:
        return self.rule_book.score_matching(6)

    def one_pair(self) -> int:
        return self.rule_book.score_repetition(RepetitionCategory(same_number_times=2, frequency=1))

    def two_pairs(self) -> int:
        return self.rule_book.score_repetition(RepetitionCategory(same_number_times=2, frequency=2))

    def three_of_a_kind(self) -> int:
        return self.rule_book.score_repetition(RepetitionCategory(same_number_times=3, frequency=1))

    def four_of_a_kind(self) -> int:
        return self.rule_book.score_repetition(RepetitionCategory(same_number_times=4, frequency=1))

    def smallStraight(self) -> int:
        return self.rule_book.score_straight(straight_type=StraightType.SMALL)

    def largeStraight(self) -> int:
        return self.rule_book.score_straight(straight_type=StraightType.LARGE)

    def fullHouse(self) -> int:
        return self.rule_book.score_full_house()
