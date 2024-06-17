#!/usr/bin/env python3

if __name__ == '__main__':
    import sys

    input = sys.argv[1]
    output = sum(int(split) * (60 ** exp) for exp, split in enumerate(input.split(':')[::-1]))
    print(f'{input} is {output} seconds')
