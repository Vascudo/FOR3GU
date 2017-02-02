import random
computer = [1, 2, 3, 4, 5]
player = [1, 2, 3, 4, 5]
tries = 5

while tries != 0:
    placed = 0
    correct = 0

    for x in range(0, 5):
        pc_numbers = random.randint(1, 8)
        computer[x] = pc_numbers

    for y in range(0, 5):
        print "Try to guess the numbers the computer selected:\n"
        player[y] = int(raw_input())

        if player[y] > 8:
            print "Please select a number from 1 to 8:"
            player[y] = int(raw_input())

    for i in range(0, 5):
        if computer[i] == player[i]:
            placed += 1

    for i in range(0, 5):
        for z in range(0, 5):
            if player[i] == computer[z]:
                correct += 1
                computer[z] = 0
                break
    tries -= 1
    print "You had " + str(correct) + " numbers and " + str(placed) + " were in the correct place.\n"
    print "You have " + str(tries) + " tries left."

print "GAME OVER"
