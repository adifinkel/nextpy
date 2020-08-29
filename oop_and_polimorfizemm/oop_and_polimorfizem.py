class Octopus:
    COUNT_ANIMALS = 0

    def __init__(self, name="Octavio", age=0):
        self._name = name
        self._age = age
        Octopus.COUNT_ANIMALS += 1

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age


class Pixel:

    def __init__(self, x=0, y=0, green=0, red=0, blue=0):
        self._x = x
        self._y = y
        self._green = green
        self._red = red
        self._blue = blue

    def set_cords(self, x, y):
        self._x = x
        self._y = y

    def set_grayscale(self):
        avg_of_pixel = (self._blue + self._green + self._red) / 3
        self._green, self._red, self._blue = (avg_of_pixel,) * 3

    def print_pixel_info(self):
        print_string = (f"x: {self._x}, "
                        f"y: {self._y}, "
                        f"color: ({self._red}, {self._green}, {self._blue}) ")

        colors = [(color, value) for color, value in (('red', self._red),
                                                      ('green', self._green),
                                                      ('blue', self._blue))
                  if value > 0]

        if len(colors) == 1 and colors[0][1] > 50:
            print_string += colors[0][0]
        print(print_string)


class BigThing:

    def __init__(self, param):
        self._param = param

    def size(self):
        if type(self._param) in (list, dict, str):
            return len(self._param)
        return self._param


class BigCat(BigThing):

    def __init__(self, weight, *args, **kwargs):
        super(BigCat, self).__init__(*args, **kwargs)
        self._weight = weight

    def size(self):
        if self._weight > 20:
            return "very fat"
        if self._weight > 15:
            return "fat"
        return "ok"


class Animal:
    ZOO_NAME = "Hayaton"

    def __init__(self, name, hunger=0):
        self._name = name
        self._hunger = hunger

    def get_name(self):
        return self._name

    def is_hungry(self):
        return self._hunger > 0

    def feed(self):
        self._hunger -= self._hunger

    def talk(self):
        raise NotImplementedError


class Dog(Animal):
    def talk(self):
        print("woof woof")

    @staticmethod
    def fetch_stick():
        print("There you go, sir!")


class Cat(Animal):
    def talk(self):
        print("meow")

    @staticmethod
    def chaise_laser():
        print("Meeeeow")


class Skunk(Animal):

    def __init__(self, stink_count=6, *args, **kwargs):
        super(Skunk, self).__init__(*args, **kwargs)
        self._stink_count = stink_count

    def talk(self):
        print("tsssss")

    @staticmethod
    def stink():
        print("Dear lord!")


class Unicorn(Animal):
    def talk(self):
        print("Good day, darling")

    @staticmethod
    def sing():
        print("I’m not your toy...	")


class Dragon(Animal):
    def __init__(self, color="Green", *args, **kwargs):
        super(Dragon, self).__init__(*args, **kwargs)
        self._color = color

    def talk(self):
        print("Raaaawr")

    @staticmethod
    def breathe_fire():
        print("$@#$#@$")


def main():
    zoo_lst = [
        Dog(name="Brownie", hunger=10),
        Cat(name="Zelda", hunger=3),
        Skunk(name="Stinky", hunger=0),
        Unicorn(name="Kate", hunger=7),
        Dragon(name="Lizzy", hunger=1450),
        Dog(name="Doggo", hunger=80),
        Cat(name="Kitty", hunger=80),
        Skunk(name="Stinky.jr", hunger=80),
        Unicorn(name="clair", hunger=80),
        Dragon(name="McFly", hunger=80)
    ]
    for animal in zoo_lst:
        if animal.is_hungry():
            print(animal.__class__.__name__, animal.get_name())
        while animal.is_hungry():
            animal.feed()
        animal.talk()
        actions = {Dog: Dog.fetch_stick, Cat: Cat.chaise_laser,
                   Skunk: Skunk.stink, Unicorn: Unicorn.sing,
                   Dragon: Dragon.breathe_fire}
        for k, v in actions.items():
            if isinstance(animal, k):
                v()
    print(Animal.ZOO_NAME)


if __name__ == "__main__":
    main()
