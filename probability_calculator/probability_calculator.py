import copy
import random


class Hat:
    def __init__(self, **kwargs):

        self.contents = []
        for k, v in kwargs.items():
            for i in range(v):
                self.contents.append(k)

        self.__initial_contents = copy.copy(self.contents)

    def reset(self):
        self.contents = copy.copy(self.__initial_contents)

    def draw(self, num_balls):
        # If the number of balls to draw is greater than or equal to the available balls, return all balls
        if num_balls >= len(self.contents):
            drawn_balls = self.contents.copy()
            self.contents.clear()  # Empty the hat since all balls were drawn
            return drawn_balls

        # Draw random balls without replacement if number of balls requested is less than available
        drawn_balls = random.sample(self.contents, num_balls)

        # Remove the drawn balls from the contents
        for ball in drawn_balls:
            self.contents.remove(ball)

        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected_count = 0
    for i in range(num_experiments):
        expected_balls_working_copy = copy.copy(expected_balls)
        hat.reset()
        returned_balls = hat.draw(num_balls_drawn)
        for ball_color, ball_count in expected_balls.items():
            for _ in range(ball_count):
                if ball_color in returned_balls:
                    returned_balls.remove(ball_color)
                    expected_balls_working_copy[ball_color] -= 1

        if sum(v for v in expected_balls_working_copy.values()) == 0:
            expected_count += 1

    probability = expected_count / num_experiments
    return probability
