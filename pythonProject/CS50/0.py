import os
import time


def validate():
    os.system("clear")
    while True:
        try:
            n = int(input("Enter a number\n-->\t"))
        except ValueError:
            print("Invalid input")
            time.sleep(1)
        else:
            return n


# end of validate()

number = validate()
print(f"The number is {number}")
print("Done")
