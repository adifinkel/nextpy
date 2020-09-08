def translate(sentence):
    """
    param sentence: the function gets string sentence in Spanish
    return: the given sentence in English.
    # first generator func
    # to do: generate a file with wider spanish words instead of a dictionary
    """
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat',
             'casa': 'house', 'el': 'the'}
    dict_gen = (words[word] for word in sentence.split())
    for word in dict_gen:
        yield word


def is_prime(n):
    # Corner case
    if n <= 1:
        return False
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def nums():
    num = 0
    while True:
        if is_prime(num):
            yield num
        num += 1


def first_prime_over(n):
    """
    param n: integer
    return: integer. the next prime number after n.
    """
    numbers = nums()
    prime_gen = (number for number in numbers if number > n)
    print(next(prime_gen))


def parse_ranges(ranges_string):
    """
    ranges_string: string. describes a range. for example: "4-9"
    returns: generator how creates all ot hose strings
    """
    lst = []
    couple_gen = ([int(string[0]), int(string[2])]
                  for string in ranges_string.split(","))

    list_gen = (list(range(start, end+1)) for start, end in couple_gen)
    for n in list_gen:
        lst = lst + n
    print(lst)


def get_fibo():
    """
    returns a generator that generate values from fibonacci sequence
    """
    a, b = 0, 1
    yield a
    while True:
        yield b
        a, b = b, a + b


def gen_secs():
    """
    generates seconds (0-59) generator
    """
    sec = 0
    while sec < 60:
        yield sec
        sec = sec + 1


def gen_minutes():
    """
    creates minutes generator
    """
    m = 0
    while m < 60:
        yield m
        m = m + 1


def gen_hours():
    """
    creates hours generators (0-23)
    """
    hour = 0
    while hour < 24:
        yield hour
        hour = hour + 1


def two_digits(num):
    return ('0' + str(num))[-2:]


def gen_time():
    """
    generates all of the possible hours in 24 time stamps day
    """
    for hour in gen_hours():
        for minute in gen_minutes():
            for sec in gen_secs():
                yield ":".join(map(two_digits, (hour, minute, sec)))


def gen_years(year=2020):
    """
    param year: integer
    generates years from the year param
    """
    while True:
        yield year
        year = year + 1


def gen_months():
    """
    generates the months of a year
    """
    month = 1
    while month < 13:
        yield month
        month = month + 1


def gen_days(month, leap_year=True):
    """
    month: integer
    leap_year: boolean
    returns: a generator who creates the number of days in a month
    """
    feb = 29 if leap_year else 28
    month_dict = {1: 31, 2: feb, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31,
                  9: 30, 10: 31, 11: 30, 12: 31}

    for day in range(month_dict[month]):
        yield day + 1


def is_leap_year(year):
    """
    year: int
    returns true if the param is leap year, False otherwise
    """
    return (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))


def gen_date():
    """
    generates a time stamp
    """
    for year in gen_years():
        for month in gen_months():
            for day in gen_days(month, is_leap_year(year)):
                for time in gen_time():
                    yield f"{day}/{month}/{year}   {time}"


def million_div_iter(iteration=1000000):
    """
    Print the 1,000,000 iterations of gen_date
    """
    dates = gen_date()
    while True:
        _ = list(zip(dates, range(iteration)))
        yield next(dates)


def main():
    dates = million_div_iter()
    for date, i in zip(dates, range(300000000)):
        print(date)


if __name__ == '__main__':
    main()
