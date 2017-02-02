import random


dice_program = True
score_pc = 0
score_player = 0

while dice_program:
    score_pc = 0
    for z in range(0, 5):
        dice_number = random.randint(1, 6)
        score_pc = score_pc + dice_number

    for x in range(1, 3):
        score_player = 0
        for y in range(0, 5):
            dice_number = random.randint(1, 6)
            score_player = score_player + dice_number

        print "Your score is " + str(score_player) + " points, do you want to try for a higher one? y/n"
        choice = raw_input()
        if choice == "n":
            break

    print "You got " + str(score_player) + " points and the PC got " + str(score_pc)

    if score_player > score_pc:
        print "You win!"

    elif score_player < score_pc:
        print "You lose!"

    else:
        "It's a draw!"

    print "Do you want try again? y/n"
    choice2 = raw_input()
    if choice2 == "n":
        print "Thank you for playing!"
        dice_program = False
