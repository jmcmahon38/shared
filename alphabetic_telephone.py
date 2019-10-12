"""

Many companies use telephone numbers like 555-GET-FOOD so the number
is easier for their customers to remember. On a standard telephone the
alphabetic letters are mapped to numbers in the following fashion:

A, B, C = 2
D, E, F = 3
G, H, I = 4
J, K, L = 5
M, N, O = 6
P, Q, R, S = 7
T,U, V, = 8
W, X, Y, Z = 9

Write a program that asks the user to enter a 10-character telephone number
in the format XXX-XXX-XXXX. The application should display the telephone
number with any alphabetic characters that appeared in the original
translated to their numeric equivalent.

Hint: Create a variable to hold the converted phone number and concatenate
one number at a time on to the end of it.

Suggestion: Try using Parallel Lists (see optional references).

"""


def main():

    user_input = input("give me a number")
    new_number = converter(user_input)
    print(new_number)


def converter(phonetic_number):

    alpha = ['0', '1', '2', 'A', 'B', 'C', '3', 'D', 'E', 'F', '4', 'G', 'H', 'I',
             '5', 'J', 'K', 'L', '6', 'M', 'N', 'O', '7', 'P', 'Q', 'R', 'S', '8',
             'T', 'U', 'V', '9', 'W', 'X', 'Y', 'Z', '-']

    digits = ['0', '1', '2', '2', '2', '2', '3', '3', '3', '3', '4', '4', '4', '4',
              '5', '5', '5', '5', '6', '6', '6', '6', '7', '7', '7', '7', '7', '8',
              '8', '8', '8', '9', '9', '9', '9', '9', '-']

    converted_number = ""
    for digit in phonetic_number.replace("-", ""):
        for item in range(0, len(alpha)):
            if alpha[item] == digit:
                converted_number += digits[item]

    return converted_number


main()
