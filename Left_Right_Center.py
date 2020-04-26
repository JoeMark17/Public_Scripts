import random

#create the number of users you want to play by copying the code below for each user
#The list will consist of the user name as [0] and the number of points the user has at [1]
user_1 = ('User Name', 3)

payer_turn = user_1

def Left_Right_Center():
    dice = ('Dot', 'Dot', 'Dot', 'Left', 'Right', 'Center')

    one_roll = random.choice(dice)
    two_roll = random.choice(dice), random.choice(dice)
    three_roll = random.choice(dice), random.choice(dice), random.choice(dice)

    if payer_turn[1] >= 3:
        print (payer_turn[0] + ' rolled')
        print three_roll
    elif payer_turn[1] == 2:
        print (payer_turn[0] + ' rolled')
        print two_roll
    elif payer_turn[1] == 1:
        print (payer_turn[0] + ' rolled')
        print one_roll
    else:
        print (payer_turn[0] + ' rolled')
        print('You are out of the game :(')

Left_Right_Center()
