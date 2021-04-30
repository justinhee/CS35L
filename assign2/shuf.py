#!/usr/bin/python3
"""
Output lines selected randomly from a file
"""

import argparse, random, sys

class randline:
    def __init__(self, input):
        self.lines = input
    def chooseLine(self):
        return random.choice(self.lines)
def main():

    parser = argparse.ArgumentParser(description="""Write a random permutation of the input lines to standard output.n

With no FILE, or when FILE is -, read standard input."""
)
    # collect the arguments
    group = parser.add_mutually_exclusive_group()
    
    group.add_argument("-e", "--echo",  help="treat each ARG as an input line", nargs="*", dest="ARG")
    group.add_argument("-i", "--input-range", help="treat each number LO through HI as an input line", dest="input_range", metavar="LO-HI")
    parser.add_argument("-n", "--head-count", help="output at most COUNT lines", dest="COUNT", type=int)
    parser.add_argument("-r", "--repeat", help="output lines can be repeated", action="store_true")
    parser.add_argument("FILE", nargs="?", type=argparse.FileType('r'), default=sys.stdin)

    
    args = parser.parse_args()

    #store data
    
    lines = []
    # store range from lo-hi for -i option
    if args.input_range != None:
        lo_hi = args.input_range.split('-', 1)
        if len(lo_hi) != 2:
            parser.error(f"invalid input range: '{args.input_range}'")
        try:
            low = int(lo_hi[0])
        except:
            parser.error(f"input range: '{lo_hi[0]}'")
        try:
            hi = int(lo_hi[1])
        except:
            parser.error(f"invalid input range: '{lo_hi[1]}'")
        if hi < low:
            parser.error(f"invalid input range: '{args.input_range}'")
        else:
            for i in range(int(lo_hi[0]), int(lo_hi[1])+1):
                lines.append(i)
    #store ARGs for -e option
    elif args.ARG != None:
        lines = args.ARG

    # either read in file or standard input
    else:
        for line in args.FILE:
            lines.append(line.strip('\n'))

    random.shuffle(lines)

    # print random lines
    numlines = len(lines)
    if args.COUNT != None:
        if args.COUNT < 0:
            parser.error(f"invalid line count: '{args.COUNT}'")
        numlines = args.COUNT
    
    if args.repeat:
        count = 0
        while count != args.COUNT:
            print(random.choice(lines))
            count = count + 1
    else:
        count = 0
        while count != args.COUNT and count != len(lines):
            print(lines[count])
            count = count + 1

if __name__ == '__main__':
    main()
