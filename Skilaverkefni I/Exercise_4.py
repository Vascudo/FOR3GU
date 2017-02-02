score = 0
program = True
while program:
    print
    question1 = raw_input("Who is the current president of the USA?\n "
                          "A: Marilyn Manson\nB: Donald Trump\nC: Hillary Clinton")
    if question1 == "B" or "b":
        score += 1

    question2 = raw_input("The Earth is flat, (t)rue or (f)alse?}\n")
    if question2 == "f" or "F":
        score += 1

    question3 = int(raw_input("What is the square root of 9?\n"))
    if question3 == 3:
        score += 1

    question4 = raw_input("Who is Nero Claudius Caesar Augustus Germanicus?\n"
                          "A: A actor\nB:A Roman general\nC: A Roman emperor")
    if question4 == "C" or "c":
        score += 1

    question5 = int(raw_input("What year did Iceland gain independence?}n"))
    if question5 == 1944:
        score += 1

    print "You got " + str(score) + " of 5 questions correct!\n"

    choice = raw_input("Do you want to try again? y/n\n")

    if choice == "n" or "N":
        program = False
print "Thank you for playing."
