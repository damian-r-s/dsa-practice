#!/bin/python3

import math
import os
import random
import re
import sys

from itertools import combinations

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topic):
    # Write your code here    
    combi = list(combinations(topic, 2))    
    groups = 0
    maxi = 0
    
    for c in combi:        
        sumator = 0
        for j in range(len(c[0])):
            a = c[0][j]
            b = c[1][j]
            
            if(a == "1" or b == "1"):
                sumator = sumator + 1
            
        if(sumator > maxi):
            maxi = sumator
            groups = 1
        elif (sumator == maxi):
            groups += 1
        
    return maxi, groups

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
