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
        same_number_times = 2
        frequency = 1
        counts = [[n,self.dice.values.count(n)] for n in set(self.dice.values)]
        candidates = [n for n, times in counts if times >= same_number_times]
        match = sorted(candidates, reverse=True)[:frequency]
        if len(match) >= frequency:
            return sum([n * same_number_times for n in match])
        return 0

    def two_pairs(self):
        same_number_times = 2
        frequency = 2
        counts = [[n, self.dice.values.count(n)] for n in set(self.dice.values)]
        candidates = [n for n, times in counts if times >= same_number_times]
        match = sorted(candidates, reverse=True)[:frequency]
        if len(match) >= frequency:
            return sum([n * same_number_times for n in match])
        return 0

    def four_of_a_kind(self):
        same_number_times = 4
        frequency = 1
        counts = [[n, self.dice.values.count(n)] for n in set(self.dice.values)]
        candidates = [n for n, times in counts if times >= same_number_times]
        match = sorted(candidates, reverse=True)[:frequency]
        if len(match) >= frequency:
            return sum([n * same_number_times for n in match])
        return 0

    @staticmethod
    def three_of_a_kind(d1, d2, d3, d4, d5):
        t = [0] * 6
        t[d1 - 1] += 1
        t[d2 - 1] += 1
        t[d3 - 1] += 1
        t[d4 - 1] += 1
        t[d5 - 1] += 1
        for i in range(6):
            if (t[i] >= 3):
                return (i + 1) * 3
        return 0

    @staticmethod
    def smallStraight(d1, d2, d3, d4, d5):
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        if (tallies[0] == 1 and
                tallies[1] == 1 and
                tallies[2] == 1 and
                tallies[3] == 1 and
                tallies[4] == 1):
            return 15
        return 0

    @staticmethod
    def largeStraight(d1, d2, d3, d4, d5):
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        if (tallies[1] == 1 and
                tallies[2] == 1 and
                tallies[3] == 1 and
                tallies[4] == 1
                and tallies[5] == 1):
            return 20
        return 0

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
