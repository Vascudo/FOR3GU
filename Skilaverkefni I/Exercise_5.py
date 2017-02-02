import random
program = True


class LottoTicket:
    my_array = [1, 2, 3, 4, 5]

    def __init__(self, ticket):
        self.my_array[x] = ticket

    def display_array(self):
        return int(self.my_array)


class LottoMachine:
    my_array2 = [1, 2, 3, 4, 5]

    def __init__(self, machine):
        self.my_array2[x] = machine

    def display_array(self):

        return self.my_array2


class LottoChecker:
    counter = 0

    def __init__(self, y_numbers, m_numbers):

        self.y_numbers = y_numbers
        self.m_numbers = m_numbers

    def display_counter(self):
        self.counter = len(set(self.y_numbers) & set(self.m_numbers))

        return LottoChecker.counter


while program:
    print "Insert numbers into your ticket:\n"

    for x in range(0, 5):
        rng = random.randint(1, 9)
        machine_numbers = LottoMachine(machine=rng)
        your_numbers = LottoTicket(ticket=int(raw_input()))
    print str(your_numbers.my_array[0]) + "" + str(machine_numbers.my_array2[0])
    print str(your_numbers.my_array) + "" + str(machine_numbers.my_array2)
    LottoChecker(your_numbers.my_array, machine_numbers.my_array2)

    print LottoChecker.counter

    #if choice == "n":
    #    print "Thank you for playing!"
    #    program = False
