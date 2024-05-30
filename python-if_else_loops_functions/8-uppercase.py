#!/usr/bin/python3
def uppercase(s):
    result = ""
    for char in s:
        if "a" <= char <= "z":
            result += "{}".format(chr(ord(char) - 32))
        else:
            result += "{}".format(char)
    print("{}".format(result))
