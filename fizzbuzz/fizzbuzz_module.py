def fizzbuzz(number):
    if number %3 == 0:
        if number %5 == 0:
            return 'FizzBuzz'
        else:
            return 'Fizz'
    elif number %5 == 0:
        return 'Buzz'
    else:
        return number


def main():
    for i in range (1,101):
        value = fizzbuzz(i)
    return

if __name__ == '__main__':
    main()
