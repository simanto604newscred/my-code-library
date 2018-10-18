__author__ = 'MAK'
import sys
# http://maqe.github.io/maqe-bot.html


DIRECTIONS = ['North', 'East', 'South', 'West']
STEP_FORMULA = [(0, 1), (1, 0), (0, -1), (-1, 0)]


class MaqeBot:

    def __init__(self):
        self.x_cordinate = 0
        self.y_cordinate = 0
        self.steps = ''
        self.direction = 0
        self.change_direction = {'R': lambda direction_index: direction_index+1 if direction_index < 3 else 0,
                                 'L': lambda direction_index: direction_index-1 if direction_index > 0 else 3,
                                 }

    def complete_steps(self):
        step = int(self.steps)
        self.x_cordinate += STEP_FORMULA[self.direction][0] * step
        self.y_cordinate += STEP_FORMULA[self.direction][1] * step
        self.steps = ''

    def complete_input(self, input_path):
        index = 0

        while index < len(input_path):

            if input_path[index] == 'W':
                index += 1

                while index < len(input_path) and input_path[index].isdigit():
                    self.steps += input_path[index]
                    index += 1
                self.complete_steps()

            elif input_path[index] == 'R' or input_path[index] == 'L':
                self.direction = self.change_direction[input_path[index]](self.direction)
                index += 1


if __name__ == '__main__':
    input_path = sys.argv[1]
    bot = MaqeBot()
    bot.complete_input(input_path)
    print('X: {} Y: {} Direction: {}'.format(bot.x_cordinate, bot.y_cordinate, DIRECTIONS[bot.direction]))





