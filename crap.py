from secrets import randbelow


def genCrap(length):

    crap = ""
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    for i in range(0, length):
        crap += chars[randbelow(len(chars))]

    return str(crap)  #just incase it's all numbers ;)
