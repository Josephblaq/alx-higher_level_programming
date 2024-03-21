#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = sys.argv[1:]
    args_numbs = len(arguments)
    if args_numbs == 0:
        print("0 arguments.")
    elif args_numbs == 1:
        print("{} argument:".format(args_numbs))
    else:
        print("{} arguments: ".format(args_numbs))
    for o in range(args_numbs):
        print("{}: {}".format(o+1, arguments[o]))
