from modules import file1


class BirthdayCard(file1.GreetingCard):
    """
    Birthday card class
    """
    def __init__(self, sender_age=0):
        super(BirthdayCard, self).__init__()
        self._sender_age = sender_age

    def greeting_msg(self):
        super().greeting_msg()
        print(f"Happy Birthday, the sender is {self._sender_age} years old")
