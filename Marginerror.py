import math

while True:
    try:
        z = float(
            input("What is the confidence level, 95, 97, 99 or 99.9 percent? Choose one: "))
        if z not in [95, 97, 99, 99.9]:
            raise ValueError
        break
    except ValueError:
        print("Write only one of these 4 values and not a string. Please try again.")

while True:
    try:
        n = int(input("What is the sample size? "))
        if n <= 0:
            raise ValueError
        break
    except ValueError:
        print("Write a positive integer. Please try again.")

p = None
while p is None:
    try:
        p = float(input(
            "If a party's rate is 1 percent at a poll, then write 1. For calculating maximum margin of error, choose 50. "))
        if p < 0 or p > 100:
            print("Expected value should be between 0 and 100. Please try again.")
            p = None
        else:
            p = p / 100  # for showing it as percentage
    except ValueError:
        print("Please enter a valid number between 0 and 100.")

zy = 0
if z == 95:
    zy = 1.96
elif z == 97:
    zy = 2.17
elif z == 99:
    zy = 2.576
elif z == 99.9:
    zy = 3.29

try:
    margin_of_error = (zy * math.sqrt(p * (1 - p) / n) * 100)
    print("Margin of error at percentage: ±{:.2f}%".format(margin_of_error))
except Exception as e:
    print("An error occurred: " + str(e))

min_value = p*100-margin_of_error
max_value = p*100+margin_of_error

print("The party can take this values at {:.2f}%".format(
    z) + " confidence level: {:.2f}%".format(min_value) + "-{:.2f}%".format(max_value))
