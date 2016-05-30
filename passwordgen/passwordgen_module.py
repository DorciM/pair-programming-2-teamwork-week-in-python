import random
import string


def passwordgen():
    good_pw = [0,0,0,0]
    pw = []
    chars= string.ascii_letters + string.digits + "[!@#$%^&*()?]"
    for i in range(8):
        pw.append(random.choice(chars))
    for i in range(8):
        if pw[i] in string.ascii_lowercase:
            good_pw[0] = 1
        elif pw[i] in string.ascii_uppercase:
            good_pw[1] = 1
        elif pw[i] in string.digits:
            good_pw[2] = 1
        elif pw[i] in "[!@#$%^&*()?]":
            good_pw[3] = 1
    if good_pw == [1, 1, 1, 1]:
        pw = ''.join(str(i) for i in pw)
        return pw
    else:
        passwordgen()


def main():
    password = passwordgen()
    print (password)
    return


if __name__ == '__main__':
    main()
