from modules import file1, file2

"""
objects from GreetingCard class and BirthdayCard class (imported from files)
"""
card = file1.GreetingCard()
b_card = file2.BirthdayCard()


def main():
    card.greeting_msg()
    b_card.greeting_msg()


if __name__ == '__main__':
    main()
