import datetime


def years(age):
    year = 2016 - age + 100
    return year


def main():
    name = str(input("What is your name? \n"))
    age = int(input("How old are you? \n"))
    number = int(input("Choose a number between 1-10: \n"))
    result = years(age)
    print(("Dear %s you will turn 100 years old in %d") * number % ((name, result) *number))
    for i in range(number):
        print("Dear %s you will turn 100 years old in %d" % (name, result))
    return


if __name__ == '__main__':
    main()
