#!/usr/bin/python3
alphabet = ""
for i in range(97, 123):
    if chr(i) not in ["q", "e"]:
        alphabet += "{}".format(chr(i))
print("{}".format(alphabet), end='')
