def palindrome(str):
    str2 = str.lower()
    str2 = str2.replace(" ", "")
    str = str.replace(" ", "")
    if str.lower() == str2[::-1]:
        #  print "True"
        return True
    else:
        return False


def main():
    sentence = str(input("Please input a string\n"))
    x = palindrome(sentence)
    return


if __name__ == '__main__':
    main()
