from abc import ABC, abstractmethod
from enum import Enum
from typing import List
from typing import NewType


DiceValues = NewType('DiceValues', List[int])


class Category(ABC):
    @abstractmethod
    def score(self, dice:DiceValues) -> int:
        pass


class Chance(Category):
    def score(self, dice: DiceValues) -> int:
        return sum(dice)


class Yatzy(Category):
    def __init__(self):
        self.win_score = 50
        self.loose_score = 0

    def score(self, dice: DiceValues) -> int:
        if len(set(dice)) == 1:
            return self.win_score
        return self.loose_score


class Match(Category):
    def __init__(self, number: int):
        self.number = number

    def score(self, dice: DiceValues) -> int:
        return sum([v for v in dice if v == self.number])


class Repetition(Category):
    def __init__(self, same_number_times: int, frequency: int):
        self.same_number_times = same_number_times
        self.frequency = frequency
        self.loose_score = 0

    def score(self, dice:DiceValues) -> int:
        match = self._match(dice)
        if self._is_a_win(match):
            return self._assign_win_score(match)
        return self.loose_score

    def _match(self, dice:DiceValues) -> List[int]:
        counts = [[n, dice.count(n)] for n in set(dice)]
        candidates = [n for n, times in counts if times >= self.same_number_times]
        return sorted(candidates, reverse=True)[:self.frequency]

    def _is_a_win(self, match:List[int]) -> bool:
        return len(match) >= self.frequency

    def _assign_win_score(self, match: List[int]) -> int:
        return sum([n * self.same_number_times for n in match])


class StraightType(Enum):
    SMALL = 0
    LARGE = 1


class Straight(Category):
    def __init__(self, straight_type: StraightType):
        self.values = [1, 2, 3, 4, 5] if straight_type is StraightType.SMALL else [2, 3, 4, 5, 6]
        self.win_score = 15 if straight_type is StraightType.SMALL else 20
        self.loose_score = 0

    def score(self, dice:DiceValues) -> int:
        match = self._match(dice)
        if self._is_a_win(match):
            return self.win_score
        return self.loose_score

    def _match(self, dice:DiceValues) -> List[int]:
        return list(set([i for i, j in zip(self.values, sorted(dice)) if i == j]))

    def _is_a_win(self, match:List[int]) -> bool:
        return len(match) == len(self.values)


class FullHouse(Category):
    def __init__(self):
        self.repetitions = [
                Repetition(same_number_times=2, frequency=1),
                Repetition(same_number_times=3, frequency=1)
            ]
        self.loose_score = 0

    def score(self, dice:DiceValues) -> int:
        match = self._match(dice)
        if all(match):
            return sum(match)
        return self.loose_score

    def _match(self, dice: DiceValues) -> List[int]:
        if len(set(dice)) == len(self.repetitions):
            return [c.score(dice=dice) for c in self.repetitions]
        return []