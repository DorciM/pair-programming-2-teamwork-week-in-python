import random
import string


def passwordgen():
    good_pw = [0, 0, 0, 0]
    pw = []
    chars = string.ascii_letters + string.digits + "[!@#$%^&*()?]"
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
        return passwordgen()


def main():
    choice = str(input("Press 'w' for weak or 's' for strong password\n"))
    weak_pw = ["01234", "password", "pw", "12345", "invalid", "qwerty", "baseball",
               "letmein", "access", "batman", "superman", "696969", "trustno"]
    if choice == 's':
        password = passwordgen()
    elif choice == 'w':
        password = random.choice(weak_pw)
    else:
        print("You're so retarded you don't deserve to have a password.")
    print(password)
    return


if __name__ == '__main__':
    main()
