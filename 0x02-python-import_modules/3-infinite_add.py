#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    numbers = 0
    for j in range(1, len(argv)):
        numbers += int(argv[j])
    print("{}".format(numbers))
