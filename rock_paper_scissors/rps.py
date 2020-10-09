#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  options = [['rock'], ['paper'], ['scissors']]
  if n is 0:
    return [[]]
  if n is 1:
    return options
  else:
    result = rock_paper_scissors(n-1)
    new = result * 3
    for i in range(len(new)):
      j = i // 3**(n-1)
      new[i] = options[j] + new[i]
    return new


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')