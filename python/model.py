from dataclasses import dataclass
from enum import Enum
from typing import List


@dataclass(frozen=True)
class Dice:
    values: List[int]


class StraightType(Enum):
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


class RepetitionCategory:
    def __init__(self, same_number_times: int, frequency: int):
        self.same_number_times = same_number_times
        self.frequency = frequency
        self.loose_score = 0

    def score(self, dice:Dice) -> int:
        match = self._match(dice)
        if self._is_a_win(match):
            return self._assign_win_score(match)
        return self.loose_score

    def _match(self, dice:Dice) -> List[int]:
        counts = [[n, dice.values.count(n)] for n in set(dice.values)]
        candidates = [n for n, times in counts if times >= self.same_number_times]
        return sorted(candidates, reverse=True)[:self.frequency]

    def _is_a_win(self, match:List[int]) -> bool:
        return len(match) >= self.frequency

    def _assign_win_score(self, match: List[int]) -> int:
        return sum([n * self.same_number_times for n in match])


class FullHouseCategory:
    def __init__(self):
        self.repetitions = [
                RepetitionCategory(same_number_times=2, frequency=1),
                RepetitionCategory(same_number_times=3, frequency=1)
            ]
        self.loose_score = 0

    def score(self, dice:Dice) -> int:
        match = self._match(dice)
        if all(match):
            return sum(match)
        return self.loose_score

    def _match(self, dice: Dice) -> List[int]:
        if len(set(dice.values)) == len(self.repetitions):
            return [c.score(dice=dice) for c in self.repetitions]
        return []