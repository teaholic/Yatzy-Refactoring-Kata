from abc import ABC
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


class StraightCategory:
    def __init__(self, straight_type: StraightType):
        self.values = [1, 2, 3, 4, 5] if straight_type is StraightType.SMALL else [2, 3, 4, 5, 6]
        self.win_score = 15 if straight_type is StraightType.SMALL else 20
        self.loose_score = 0

    def score(self, dice:Dice) -> int:
        match = self._match(dice)
        if self._is_a_win(match):
            return self.win_score
        return self.loose_score

    def _match(self, dice:Dice) -> List[int]:
        return list(set([i for i, j in zip(self.values, sorted(dice.values)) if i == j]))

    def _is_a_win(self, match:List[int]) -> bool:
        return len(match) == len(self.values)


@dataclass(frozen=True)
class Repetition:
    same_number_times: int
    frequency: int
    loose_score: int = 0


class RepetitionCategory:
    def __init__(self, repetition: Repetition):
        self.repetition = repetition

    def score(self, dice:Dice) -> int:
        match = self._match(dice)
        if self._is_a_win(match):
            return self._assign_win_score(match)
        return self._assign_loose_score()

    def _match(self, dice:Dice) -> List[int]:
        counts = [[n, dice.values.count(n)] for n in set(dice.values)]
        candidates = [n for n, times in counts if times >= self.repetition.same_number_times]
        return sorted(candidates, reverse=True)[:self.repetition.frequency]

    def _is_a_win(self, match:List[int]) -> bool:
        return len(match) >= self.repetition.frequency

    def _assign_win_score(self, match: List[int]) -> int:
        return sum([n * self.repetition.same_number_times for n in match])

    def _assign_loose_score(self) -> int:
        return self.repetition.loose_score


class FullHouse:
    def __init__(self, loose_score: int=0):
        self.repetitions = [
                Repetition(same_number_times=2, frequency=1),
                Repetition(same_number_times=3, frequency=1)
            ]
        self.loose_score = loose_score

    def score(self, dice:Dice) -> int:
        match = self._match(dice)
        if all(match):
            return sum(match)
        return self.loose_score

    def _match(self, dice: Dice) -> List[int]:
        if dice.number_of_unique_values() == len(self.repetitions):
            return [
                RepetitionCategory(repetition=c).score(dice=dice)
                for c in self.repetitions]
        return []


class Yatzy:

    def __init__(self, d1:int=0, d2:int=0, d3:int=0, d4:int=0, d5:int=0):
        self.dice = Dice(values=[d1,d2,d3,d4,d5])

    def chance(self) -> int:
        return sum(self.dice.values)

    def yatzy(self) -> int:
        if len(set(self.dice.values)) == 1:
            return 50
        return 0

    def ones(self) -> int:
        return self._score_matching(1)

    def twos(self) -> int:
        return self._score_matching(2)

    def threes(self) -> int:
        return self._score_matching(3)

    def fours(self) -> int:
        return self._score_matching(4)

    def fives(self) -> int:
        return self._score_matching(5)

    def sixes(self) -> int:
        return self._score_matching(6)

    def one_pair(self) -> int:
        repetition = Repetition(same_number_times=2, frequency=1)
        return RepetitionCategory(repetition=repetition).score(dice=self.dice)

    def two_pairs(self) -> int:
        repetition = Repetition(same_number_times=2, frequency=2)
        return RepetitionCategory(repetition=repetition).score(dice=self.dice)

    def three_of_a_kind(self) -> int:
        repetition = Repetition(same_number_times=3, frequency=1)
        return RepetitionCategory(repetition=repetition).score(dice=self.dice)

    def four_of_a_kind(self) -> int:
        repetition = Repetition(same_number_times=4, frequency=1)
        return RepetitionCategory(repetition=repetition).score(dice=self.dice)

    def smallStraight(self) -> int:
        return StraightCategory(straight_type=StraightType.SMALL).score(dice=self.dice)

    def largeStraight(self) -> int:
        return StraightCategory(straight_type=StraightType.LARGE).score(dice=self.dice)

    def fullHouse(self) -> int:
        return FullHouse().score(dice=self.dice)

    def _score_matching(self, number:int) -> int:
        return sum([v for v in self.dice.values if v == number])
