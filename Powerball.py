import random
lotto_num = []
user_numbers = []
correct_num = 0



print('Welcome To Lucky Lottery Numbers')
# For generating random lucky numbers
while True:
    for num in range(5):
        random_num = random.randint(1, 20)
        lotto_num.append(random_num)
    wboll=random.randint(1,10)
    if 0 < wboll < 10:
        lotto_num.append(wboll)
    # For getting user numbers
    print('Enter 5 White Balls Numbers:',str())
    for num in range(0,5):
        user_num = int(input())
        user_numbers.append(user_num,)
    wboll=int(input("Input power ball num: "))
    if 0 < wboll < 10:
        user_numbers.append(wboll)
    # For checking if got any lucky numbers
    for lucky_num in lotto_num:
        for user_num in user_numbers:
            if user_num == lucky_num:
                correct_num = correct_num + 1
    print(f'Result user_numbers:{user_numbers}')
    print(f'Result Lucky_numbers: {lotto_num}')
    print(f'You got {correct_num} correct numbers')

    del user_numbers[:]
    del lotto_num

    if wboll !=wboll and correct_num==0:
        print("Try again ")
    elif wboll==wboll and correct_num==0:
        print("you got: 4$")
    elif wboll==wboll and correct_num==1:
        print("you got : 4$")
    elif wboll==wboll and correct_num==2:
        print("you got : 7$ ")
    elif wboll !=wboll and correct_num==3:
        print("you got :7$ ")
    elif wboll==wboll and correct_num==3:
        print("you got :100$")
    elif wboll !=wboll and correct_num==4:
        print("you got: 100$ ")
    elif wboll== wboll and correct_num ==4:
        print("you got :10000$")
    elif wboll !=wboll and correct_num==5:
        print("you got :1000000$" )
    elif wboll== wboll and correct_num==5:
        print("you got : 324000000$")
    print("do you want to continue?y/n")
    user_num = (input())
    if user_num !='y':
     break
