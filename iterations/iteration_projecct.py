def check_id_valid(id_number):
    """
    boolean function. check id validation
    param id_number: integer
    return: True if the id_number is valid, False otherwise
    """
    multiple_by_2_even_index = [int(num) * 2 if index % 2 == 1 else int(num)
                                for index, num in enumerate(str(id_number))]
    summed_id = sum([sum(map(int, str(num))) if num > 9 else num
                    for num in multiple_by_2_even_index])
    return summed_id % 10 == 0


def get_next_valid_id(current_id):
    """
    create next valid choice
    param: current id: integer
    return: int of the next valid id
    """
    while not check_id_valid(current_id):
        current_id += 1
    return current_id


class IDIterator:
    """
    A class used to create id's Iterator
    """
    def __init__(self, identity):
        self._id = int(identity)

    def __iter__(self):
        return self

    def __next__(self):
        self._id = get_next_valid_id(self._id + 1)
        if self._id >= 999999999:
            raise StopIteration
        return self._id


def id_generator(identify):
    """
    generator function
    param identify: integer. 9 digits as id number.
    return: generator. create valid id numbers
    """
    for i in range(int(identify), 999999999):
        if check_id_valid(i):
            yield i


def main(id1, choice):

    """
    main function to generate 10 valid id's
    the user insert an id and choose to generate id's with generator or iterator
    param: null
    return: None
    """
    choice_options = {"gen": id_generator, "it": IDIterator}
    if choice not in choice_options.keys():
        print("invalid choice")
        return

    iterable = choice_options[choice](id1)
    for i in range(10):
        print(next(iterable))


if __name__ == '__main__':
    main(
        id1=input("insert id number"),
        choice=input("Generator or Iterator? (gen/it)?")
    )
