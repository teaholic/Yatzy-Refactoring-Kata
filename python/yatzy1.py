from model import DiceValues, Yatzy, Repetition, Straight, StraightType, FullHouse, Chance, Match

class YatzyGame:

    def __init__(self, d1:int=0, d2:int=0, d3:int=0, d4:int=0, d5:int=0):
        self.dice = DiceValues([d1,d2,d3,d4,d5])

    def chance(self) -> int:
        return Chance().score(dice=self.dice)

    def yatzy(self) -> int:
        return Yatzy().score(self.dice)

    def ones(self) -> int:
        return Match(1).score(dice=self.dice)

    def twos(self) -> int:
        return Match(2).score(dice=self.dice)

    def threes(self) -> int:
        return Match(3).score(dice=self.dice)

    def fours(self) -> int:
        return Match(4).score(dice=self.dice)

    def fives(self) -> int:
        return Match(5).score(dice=self.dice)

    def sixes(self) -> int:
        return Match(6).score(dice=self.dice)

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
