
from random import randint

print("\t\33[34m\33[1m\33[4m.....PowerBall Lottery System:.....\33[0m")

class Lotto1():
    def __init__(self):
        self.user_numbers = []
        self.user_powerball = []

    def genrerate(self):
        for i in range(1):
            powerball =randint(1,10)
            self.user_powerball.append(powerball)
              # Check if this number has already been picked and ...
            while powerball in self.user_numbers :
             # ... if it has, pick a new number instead
             powerball = randint(1, 20)
        for i in range(0, 5):
            number = randint(1, 20)
            self.user_numbers.append(number)
            # Check if this number has already been picked and ...
            while number in self.user_numbers :
             # ... if it has, pick a new number instead
             number = randint(1, 20)
             self.user_numbers.sort()

class Lotto2(Lotto1):
    def __init__(self):
        super().__init__()
        self.todays_numbers = []
        self.td_powerball = []

    def user(self):
        for num in range(0, 5):
            user_num = randint(1, 20)
            self.todays_numbers.append(user_num)
        tpball = randint(1, 10)
        self.td_powerball.append(tpball)


class Lotto3(Lotto2):

    def rand(self):
        self.correct_numbers = len(set(self.user_numbers).intersection(set(self.todays_numbers)))
        return self.correct_numbers
