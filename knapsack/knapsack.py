#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
    items = [dict(i._asdict()) for i in items]
    for i in items:
      i['ratio'] = i['value']/i['size']

    items.sort(key=lambda x: x['ratio'], reverse=True)

    sack = []
    weight = 0
    value = 0
    i = 0
    while i < len(items):
      if weight + items[i]['size'] > capacity:
        i += 1
      else:
        weight += items[i]['size']
        sack.append(items[i]['index'])
        value += (items[i]['value'])
        i += 1
    return {'Value': value, 'Chosen': sorted(sack)}



if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')