from random import randint

while True:

    for _ in range(1):
        fret = randint(0, 12)
        print("Fret: " + str(fret))

    for _ in range(1):
        string = randint(1, 6)
        print("String: " + str(string))

        repeat = input("Do you want to repeat? (y/n)")

        if repeat.lower() != "y":
            break
