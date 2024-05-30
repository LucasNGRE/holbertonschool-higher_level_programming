#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        end_numb = ", "
        if i == 8 and j == 9:
            end_numb = "\n"
        print("{:d}{:d}".format(i, j), end=end_numb)
