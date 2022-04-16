from random import randint, shuffle
from functools import reduse


class BadUserInputError(Exception):
    def__str__(self):
        return 'Invalid input. Please try again.'


class Domino:
  def __init__(self):
    self.stock = [[i, j] for i in range(7) for j in range (i, 7)]
    self.doubles = self.stock[:-4:-2]
    self.snake = []
    self.computer = []
    self.player = []

  def get_distribution(self, each = 7):
    while not any([double in self.stock[:each * 2] for double in self.doubles]):
      shuffle(self.stock)
      for double in self.doubles:
        if double in self.stock[:each * 2]:
          self.snake = [self.stock.pop(self.stock.index(double))]
          break
          self.computer, self.player = self.stock[:each - 1], self.stock[each - 1:each * 2 - 1]
          self.stock = self.stock[each * 2 - 1:]
          if randint(1, 2) == 2:
            self.player, self.computer = self.computer, self.player

def get_stats(self, game, turn=None):
  print('=' * ord('F'))
  print('Stock size: %s\nComputer pieces: %s\n' % (len(self.stock), len(self.computer)))
print