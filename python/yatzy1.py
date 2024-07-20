from model import Dice, RepetitionCategory, StraightCategory, StraightType, FullHouseCategory


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
        return RepetitionCategory(same_number_times=2, frequency=1).score(dice=self.dice)

    def two_pairs(self) -> int:
        return RepetitionCategory(same_number_times=2, frequency=2).score(dice=self.dice)

    def three_of_a_kind(self) -> int:
        return RepetitionCategory(same_number_times=3, frequency=1).score(dice=self.dice)

    def four_of_a_kind(self) -> int:
        return RepetitionCategory(same_number_times=4, frequency=1).score(dice=self.dice)

    def smallStraight(self) -> int:
        return StraightCategory(straight_type=StraightType.SMALL).score(dice=self.dice)

    def largeStraight(self) -> int:
        return StraightCategory(straight_type=StraightType.LARGE).score(dice=self.dice)

    def fullHouse(self) -> int:
        return FullHouseCategory().score(dice=self.dice)

    def _score_matching(self, number:int) -> int:
        return sum([v for v in self.dice.values if v == number])
