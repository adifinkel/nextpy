import itertools


def combinations_creator(amount, one_hundred, fifty, twenty, ten, five, one):
    """
    the function gets wanted amount of money, number of dollar bills and prints
    all the difference combinations possible
    """
    wallet = {100: one_hundred, 50: fifty, 20: twenty, 10: ten, 5: five, 1: one}
    lst = []
    sum1 = 0
    for k, v in wallet.items():
        lst += [k] * v
        sum1 += v
    for i in range(len(lst)):
        for combo in set(itertools.combinations(lst, i)):
            if sum(combo) == amount:
                print(combo)


class MusicNotes:
    """
    music iterator class. creates the frequencies of the different notes.
    creates by octaves order
    """
    NOTES = {
        "La": 55, "Si": 61.74, "Do": 65.41,
        "Re": 73.42, "Mi": 82.41, "Fa": 87.31,
        "Sol": 98
    }

    MAX_OCTAVE = 5

    def __init__(self):
        self._current_note = -1

    def __iter__(self):
        return self

    @property
    def max_note(self):
        return len(self.NOTES)

    def get_octave(self):
        octave = int(self._current_note / self.max_note)
        if octave >= self.MAX_OCTAVE:
            raise StopIteration
        return octave

    def get_note_index(self):
        return self._current_note % self.max_note

    def get_note(self):
        return list(self.NOTES.values())[self.get_note_index()]

    def __next__(self):
        self._current_note += 1
        return self.get_note() * 2 ** self.get_octave()


if __name__ == '__main__':
    notes_iter = iter(MusicNotes())
    for freq in notes_iter:
        print(freq)
