import random


program = True
score = 0
while program:
    tries = 8
    points = 1280
    number = random.randint(1, 100)
    print "Pick a number between 1 and 100"

    for i in range(0, 8):
        winnings = points / pow(2, i)
        user_decision = int(raw_input())
        if user_decision == number:
            tries = (tries - 1)
            score = (score + winnings)

            print str(number) + " is correct!, you got " + str(winnings) + " points!"
            break

        if user_decision > number:
            tries = (tries - 1)
            print "The number is too high, you have " + str(tries) + " left."

        if user_decision < number:
            tries = (tries - 1)
            print "The number is too low, you have " + str(tries) + " tries left."

    if tries == 0:
        print "You ran out of tries"
    print "Your score is " + str(score) + " points.\n"
    print "Try again? y / n"
    quit_game = raw_input()

    if quit_game == "n":
        program = False

print "Thank you for playing!"
