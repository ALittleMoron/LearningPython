import re


def check(password:str, pattern:bool = False) -> (str, bool):
    """check for secure password (8 symbols with upper- and lowercase)
    
    returns tuple of note and bool valid like ("Password must contain atleast 8 characters", False)

    Keyword argument:
    password -- yes, it is.
    pattern -- with (1) or without (0) special symbols (+-/*!&$#?=@<>)
    """

    if not password or type(password) is not str:
        raise Exception('put password. NOT ANYTHING ELSE!')
    if type(pattern) is (not bool or not int):
        raise Exception("use 0 or 1, True or False")

    eight_symbs = re.compile(r'\w{8,}')
    lower_symbs = re.compile(r'[a-z]+')
    upper_symbs = re.compile(r'[A-Z]+')
    digit_symbs = re.compile(r'[0-9]+')

    if pattern:
        special_symbs = re.compile(r'[+-/*!&$#?=@<>]+')

        if eight_symbs.findall(password) == []:
            return ('Password must contain atleast 8 characters', False)
        elif lower_symbs.findall(password) == []:
            return ('Password must contain atleast one lowercase character', False)
        elif upper_symbs.findall(password) == []:
            return ('Password must contain atleast one uppercase character', False)
        elif digit_symbs.findall(password) == []:
            return ('Password must contain atleast one digit character', False)
        elif special_symbs.findall(password) == []:
            return ('Your password is not strong but valid. add some special symbols to make it strong', True)
        else:
            return ('Your password is Strong', True)
    else:
        if eight_symbs.findall(password) == []:
            return ('Password must contain atleast 8 characters', False)
        elif lower_symbs.findall(password) == []:
            return ('Password must contain atleast one lowercase character', False)
        elif upper_symbs.findall(password) == []:
            return ('Password must contain atleast one uppercase character', False)
        elif digit_symbs.findall(password) == []:
            return ('Password must contain atleast one digit character', False)
        else:
            return ('Your password is not strong but valid. add some special symbols to make it strong', True)


if __name__ == "__main__":
    a = check('1252125asgAG@', 1)
    print(a)