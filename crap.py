from secrets import randbelow


def genCrap(length):

    crap = ""
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    for i in range(0, length):
        crap += chars[randbelow(62)]

    return crap
