from Utility import *
import Color

class Lotto(Lotto3):
    def test(self, correct_numbers):
        print(f'Today’s Powerball winning numbers is:\n' + Color.MAGENTA, *self.user_numbers, Color.YELLOW, *self.user_powerball)
        print(Color.RESET+f'Your Lucky_numbers Result:\n' + Color.MAGENTA , *self.todays_numbers,
              Color.YELLOW , *self.td_powerball)
        print(Color.RESET + f'You got {self.correct_numbers} correct numbers')
        if self.user_powerball == self.td_powerball and correct_numbers == 0:
            print("you got 4$")
        elif self.user_powerball == self.td_powerball and correct_numbers == 1:
            print("you got 4$")
        elif self.user_powerball == self.td_powerball and correct_numbers == 2:
            print("you got 7$ ")
        elif self.user_powerball == self.td_powerball and correct_numbers == 3:
            print("you got 7$ ")
        elif self.user_powerball == self.td_powerball and correct_numbers == 3:
            print("you got 100$")
        elif self.user_powerball == self.td_powerball and correct_numbers == 4:
            print("you got 100$ ")
        elif self.user_powerball == self.td_powerball and correct_numbers == 4:
            print("you got 10000$")
        elif self.user_powerball == self.td_powerball and correct_numbers == 5:
            print("you got 1000000$")
        elif self.user_powerball == self.td_powerball and correct_numbers == 5:
            print("you got $324000000")
        else:
            print("Try again ")


