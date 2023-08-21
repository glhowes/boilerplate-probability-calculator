import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self, **kwargs):
        self.key_list = list()
        self.value_list = list()
        self.occurrences = str()
        self.contents = list()
        self.drawn_balls = list()

        for key, value in kwargs.items():

            self.key_list.append(key)
            self.value_list.append(value)

            self.occurrences += (value * (key + " "))

            self.key = value
        
        self.contents = self.occurrences.split()

 
    def draw(self, no_of_balls):
        self.contents = self.occurrences.split()
        self.draw_count = dict()

        if no_of_balls > len(self.contents):
            no_of_balls = len(self.contents)

        for num in range(no_of_balls):
            draw = random.choice(self.contents)
            self.drawn_balls.append(draw)
            self.contents.remove(draw)
            print(draw)
            if draw in self.draw_count:
                self.draw_count[draw] += 1
            else:
                self.draw_count[draw] = 1
        return self.drawn_balls




def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = None
    success_tally = 0
    total_tally = 0
    contents_list = hat.contents
    hats = str()
    new_hat = list()

    for trial in range(num_experiments):
        hat.draw(num_balls_drawn)
        for colour, no_of_balls in expected_balls.items():
            if colour not in hat.draw_count:
                    success = False
                    break
            else:
                if hat.draw_count[colour] < no_of_balls:
                    success = False
                    break
                else:
                    success = True
        if success == True:
            success_tally += 1

    success_rate = success_tally / num_experiments
    return success_rate