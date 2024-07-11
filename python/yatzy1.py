from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Dice:
    values: List[int]


class Yatzy:

    def __init__(self, d1:int=0, d2:int=0, d3:int=0, d4:int=0, d5:int=0):
        self.dice = Dice(values=[d1,d2,d3,d4,d5])

    def chance(self) -> int:
        return sum(self.dice.values)

    def yatzy(self) -> int:
        if len(set(self.dice.values)) == 1:
            return 50
        return 0

    def ones(self):
        return self._score_matching(1)

    def twos(self):
        return self._score_matching(2)

    def threes(self):
        return self._score_matching(3)

    def fours(self):
        return self._score_matching(4)

    def fives(self):
        return self._score_matching(5)

    def sixes(self):
        return self._score_matching(6)

    def _score_matching(self, number) -> int:
        return sum([v for v in self.dice.values if v == number])

    def one_pair(self):
        return self._score_multiple_combinations(same_number_times = 2, frequency = 1)

    def two_pairs(self):
        return self._score_multiple_combinations(same_number_times=2, frequency=2)

    def three_of_a_kind(self):
        return self._score_multiple_combinations(same_number_times=3, frequency=1)

    def four_of_a_kind(self):
        return self._score_multiple_combinations(same_number_times = 4, frequency = 1)

    def _score_multiple_combinations(self, same_number_times:int, frequency:int):
        counts = [[n, self.dice.values.count(n)] for n in set(self.dice.values)]
        candidates = [n for n, times in counts if times >= same_number_times]
        match = sorted(candidates, reverse=True)[:frequency]
        if len(match) >= frequency:
            return sum([n * same_number_times for n in match])
        return 0

    def smallStraight(self):
        small_straight = [1,2,3,4,5]
        score = 15
        return self._score_straight(straight=small_straight, score=score)

    def largeStraight(self):
        large_straight = [2,3,4,5,6]
        score = 20
        return self._score_straight(straight=large_straight, score=score)

    def _score_straight(self, straight: List[int], score: int) -> int:
        matches = set([i for i, j in zip(straight, sorted(self.dice.values)) if i == j])
        print(matches)
        if len(matches) != len(straight):
            return 0
        else:
            return score

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
