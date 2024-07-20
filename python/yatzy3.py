from model import DiceValues, Category


class YatzyService:

    def __init__(self, d1:int=0, d2:int=0, d3:int=0, d4:int=0, d5:int=0):
        self.dice = DiceValues([d1,d2,d3,d4,d5])

    def run(self, category: Category):
        return category.score(self.dice)
