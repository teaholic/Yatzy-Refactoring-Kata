from model import Dice, Repetition, Straight, StraightType, FullHouse, Chance
from model import Yatzy as YatzyCategory

class Yatzy:

    def __init__(self, d1:int=0, d2:int=0, d3:int=0, d4:int=0, d5:int=0):
        self.dice = Dice(values=[d1,d2,d3,d4,d5])

    def chance(self) -> int:
        return Chance().score(dice=self.dice)

    def yatzy(self) -> int:
        return YatzyCategory().score(self.dice)

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
        return Repetition(same_number_times=2, frequency=1).score(dice=self.dice)

    def two_pairs(self) -> int:
        return Repetition(same_number_times=2, frequency=2).score(dice=self.dice)

    def three_of_a_kind(self) -> int:
        return Repetition(same_number_times=3, frequency=1).score(dice=self.dice)

    def four_of_a_kind(self) -> int:
        return Repetition(same_number_times=4, frequency=1).score(dice=self.dice)

    def smallStraight(self) -> int:
        return Straight(straight_type=StraightType.SMALL).score(dice=self.dice)

    def largeStraight(self) -> int:
        return Straight(straight_type=StraightType.LARGE).score(dice=self.dice)

    def fullHouse(self) -> int:
        return FullHouse().score(dice=self.dice)

    def _score_matching(self, number:int) -> int:
        return sum([v for v in self.dice.values if v == number])
