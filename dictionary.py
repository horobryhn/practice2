import sys
from random import randint
from collections import Counter
from itertools import product


def dict_memory(number_of_elements):
    d = {}
    last_number = -1
    for i in range(number_of_elements):
        d[i] = randint(1, 1000)
        size = sys.getsizeof(d)
        if size > last_number:
            print("Size of dictionary grew when added an element number " + str(i + 1))
        last_number = size


def most_common(string):
    most_common_symbol = Counter(string).most_common(1)[0]
    print("Most common symbol is " + most_common_symbol[0])
    print("Most common word is " + Counter(string.split(' ')).most_common(1)[0][0])
    print("Most common symbol in words occurs " + str(most_common_symbol[1] / len(string.split(' '))) + " times on average")


def palindrome(number_of_letters, alphabet):
    for k in range(number_of_letters + 1):
        for x in product(alphabet, repeat=k):
            s = ''.join(x)
            if 2 * k <= number_of_letters:
                print(s + s[::-1])
        for x in product(alphabet, repeat=k):
            s = ''.join(x)
            if 2 * k - 1 <= number_of_letters:
                print(s + s[::-1][1:])


dict_memory(550)
most_common("Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful.")
palindrome(6, ['o', 'p', 'q', 'r', 's'])