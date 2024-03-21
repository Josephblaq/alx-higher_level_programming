#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    allfu = dir()
    for o in range(0, len(allfu)):
        if allfu[o][:2] != "__":
            print("{:s}".format(allfu[o]))
