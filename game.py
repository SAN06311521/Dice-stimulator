# This is a beginner level game constructed for practising random module of python 
# The dice keep on rolling and displaying different number everytime till you enter "y"(yes).

import sys
import random  # importing "random module" for accessing random numbers.
print("This is a Dice Rolling simple program.")
x = "y"

while x == "y":
    number = random.randint(1,6)

    if number == 1:
        print(" ________")
        print("|        |")
        print("|        |")
        print("|    *   |")
        print("|        |")
        print("|________|")
    if number == 2:
        print(" ________")
        print("|        |")
        print("|      * |")
        print("|        |")
        print("| *      |")
        print("|________|")
    if number == 3:
        print(" ________")
        print("|        |")
        print("|      * |")
        print("|    *   |")
        print("|  *     |")
        print("|________|")
    if number == 4:
        print(" ________")
        print("|        |")
        print("| *    * |")
        print("|        |")
        print("| *    * |")
        print("|________|")
    if number == 5:
        print(" ________")
        print("|        |")
        print("| *    * |")
        print("|    *   |")
        print("| *    * |")
        print("|________|")
    if number == 6:
        print(" ________")
        print("|        |")
        print("| *    * |")
        print("| *    * |")
        print("| *    * |")
        print("|________|")
    x = input("Press 'y' to roll again and 'n' to take a exit. Enter ur answer: ")
    if x == "n":
        sys.exit(0)

