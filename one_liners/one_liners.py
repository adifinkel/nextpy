import functools


def combine_coins(coin, numbers):
    """
    :param coin: string. character of a coin. like $.
    :param numbers: list of numbers
    :return: new string of the numbers, each one with the coin symbol.
    """
    print(", ".join(([coin + str(num) for num in numbers])))


def double_letter(my_str):
    """
    :param my_str: string
    :return: new string, each char is duplicated
    """
    return "".join(map((lambda x: x + x), my_str))


def four_dividers(num):
    """
    :param num: integer number
    :return: list of numbers from 1 to num, that divide by four exactly
    """
    return list(filter(lambda x: x % 4 == 0, range(1, num + 1)))


def sum_of_digits(number):
    """
    :param number: integer
    :return: sum of the number's digits
    """
    return functools.reduce(lambda x, y: int(x) + int(y), str(number))


def intersection(list_1, list_2):
    """
    :param list_1: list
    :param list_2: list
    :return: return a new list with all the values from the firs list, and also
    in the second one
    """
    return [var for var in list_1 for var2 in list_2 if var == var2]


def is_prime(num):
    return False not in [num % x != 0 for x in range(2, num)]


def is_funny(my_str):
    """
    :param my_str: string
    :return: returns True if all of the string is just "h" and "a"
    """
    return False not in [False for char in my_str if
                         (char != "h") and (char != "a")]


def enc(password):
    """
    :param password: password(where every letter switched to the next one +1 on
    the abc)
    :return: the right words as string
    """
    # return " ".join("".join(chr(ord(letter) + 2) for letter in word) for word
    # in password.split())
    return "".join(
        chr(ord(letter) + 2) for word in password for letter in word).replace(
        "\"", " ")


def get_names(file_path):
    with open(file_path, 'r') as fp:
        return fp.read().split('\n')


def longest_str_in_file(file_path):
    """
    :param file_path: gets a file path, the file contains list of names.
    each name in a new row
    :return: the longest name
    # to do: one liner
    """
    return max(get_names(file_path), key=len)


def sum_of_chars(file_path):
    """
    :param file_path: gets a path for a file that contains list of names
    :return: the number of letters of all of the names
    # to do: one liner
    """
    return sum(map(len, get_names(file_path)))


def shortest_strings(file_path):
    """
    :param file_path: gets a path for a file that contains list of names
    :return: the shortest names
    """
    names = get_names(file_path)
    min_length = min(map(len, names))
    return list(filter(lambda x: len(x) == min_length, names))


def create_names_text_file(file_path):
    """
    :param file_path: gets a path to a python file
    :return: creates a new file, each row in the new file contains the length
     of the row in the original file
    """
    with open("names_length.txt", "w") as new_file:
        names = get_names(file_path)
        new_file.write('\n'.join(map(lambda x: str(len(x)), names)))


def name_by_length(file_path):
    """
    :param file_path: gets a path of file
    :return: None. gets a number from the user and prints the names from  file
    that has the same length as the num
    """
    num = int(input("insert a number: "))
    print(list(filter(lambda x: len(x) == num, get_names(file_path))))
