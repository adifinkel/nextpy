import re


def read_file(file_name):
    """
    :param file_name: path of file
    :return: prints the contents of the file, if exist.
    """
    print("__CONTENT_START__")
    try:
        with open(file_name, "r") as fp:
            fp = fp.read()
    except IOError:
        print("__NO_SUCH_FILE__")
    else:
        print("".join(fp.split("\n")))
    finally:
        print("__CONTENT_END__")


class YoungError(Exception):
    """
    class Exception for minors
    """
    def __init__(self, age):
        self._age = age

    def __str__(self):
        return f"Provided age was {self._age}. will have to wait" \
               f" another {18-self._age} years"

    def get_age(self):
        return self._age


def send_invitation(name, age):
    """
    :param name: name of a child. string.
    :param age: age of a child. int
    :return: if the child will get an invite for adults party or not
    """
    try:
        if age < 18:
            raise YoungError(age)

    except YoungError as e:
        print("invite expected 18+ age, instead got %s" % e.get_age())

    else:
        print("You should send an invite to " + name)


class UsernameContainsIllegalCharacter(Exception):
    """
    illegal chars in username
    """
    def __init__(self, message="you can only use letters, _ and num"):
        self.message = message
        super().__init__(self.message)


class UsernameTooShort(Exception):
    """
    less then 3 chars in the username
    """
    def __init__(self, message="username length need to be greater then 3"):
        self.message = message
        super().__init__(self.message)


class UsernameTooLong(Exception):
    """
    more then 16 chars in username
    """
    def __init__(self, message="username length need to be smaller then 16"):
        self.message = message
        super().__init__(self.message)


class PasswordMissingCharacter(Exception):
    """
    the password does not have one of:
     big letter, small letter, number and sign Exception
    """
    def __init__(self, message=None):
        if message is None:
            message = "The password is missing a character"
        self.message = message


class PasswordTooShort(Exception):
    """
    less then  8 chars in password
    """
    def __init__(self, message="password length need to be greater then 8"):
        self.message = message
        super().__init__(self.message)


class PasswordTooLong(Exception):
    """
    more then 40 chars in password
    """
    def __init__(self, message="password length need to be smaller then 40"):
        self.message = message
        super().__init__(self.message)


class MissingUpper(PasswordMissingCharacter):
    """
    Missing uppercase letter in string
    """
    def __init__(self, message=None):
        super().__init__(message)
        self.message += " (Uppercase)"


class MissingLower(PasswordMissingCharacter):
    def __init__(self, message=None):
        super().__init__(message)
        self.message += " (Lowercase)"


class MissingNumber(PasswordMissingCharacter):
    def __init__(self, message=None):
        super().__init__(message)
        self.message += " (Number)"


class MissingSign(PasswordMissingCharacter):
    def __init__(self, message=None):
        super().__init__(message)
        self.message += " (Sign)"


def check_input(username, password):
    """
    :param username: string
    :param password: string
    :return: ok if the strings are valid, raise error when its not
    """
    lowercase_characters_reg = re.compile('[a-z]')
    uppercase_characters_reg = re.compile('[A-Z]')
    characters_reg = re.compile('[a-zA-Z]')
    number_reg = re.compile('[0-9]')
    special_char_reg = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    not_valid_username_char_reg = re.compile('[^a-zA-Z0-9_]')

    username_check_list = {
        lambda x: (len(x) < 3): UsernameTooShort,
        lambda x: (len(x) > 16): UsernameTooLong,
        lambda x: characters_reg.search(x) is None:
            UsernameContainsIllegalCharacter,
        lambda x: number_reg.search(x) is None:
            UsernameContainsIllegalCharacter,
        lambda x: not x.count('_'):
            UsernameContainsIllegalCharacter,
    }

    for validation_function, exception in username_check_list.items():
        if validation_function(username):
            raise exception

    invalid_username_char = not_valid_username_char_reg.search(username)
    if invalid_username_char is not None:
        character = invalid_username_char.group()
        index = invalid_username_char.span()[0]
        raise UsernameContainsIllegalCharacter(
            f"The username contains illegal character: \"{character}\" "
            f"at index: {index}")

    password_check_list = {
        lambda x: (len(x) < 8): PasswordTooShort,
        lambda x: (len(x) > 40): PasswordTooLong,
        lambda x: uppercase_characters_reg.search(x) is None:
            MissingUpper,
        lambda x: lowercase_characters_reg.search(x) is None:
            MissingLower,
        lambda x: special_char_reg.search(x) is None:
            MissingSign,
        lambda x: number_reg.search(x) is None:
            MissingNumber,
    }

    for validation_function, exception in password_check_list.items():
        if validation_function(password):
            raise exception

    return "ok"


def main():
    try:
        print(check_input(input("insert username"), input("insert password")))
    except (UsernameTooShort,
            UsernameTooLong,
            UsernameContainsIllegalCharacter,
            PasswordTooLong,
            PasswordTooShort,
            PasswordMissingCharacter) as e:
        print(e.message)


if __name__ == '__main__':
    main()
