class GreetingCard:
    """
    class for greeting cards
    attributes: recipient name, sender name
    function: print greeting msg
    """
    def __init__(self, recipient="Dana", sender="Eyal"):
        self._recipient = recipient
        self._sender = sender

    def greeting_msg(self):
        print(f"{self._recipient} is the recipient and,"
              f" {self._sender} is the sender")
