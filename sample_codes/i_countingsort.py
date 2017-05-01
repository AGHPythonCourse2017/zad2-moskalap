from collections import defaultdict
def countingSort(array, mn, mx):
    count = defaultdict(int)
    for i in array:
        count[i] += 1
    result = []
    for j in range(mn, mx + 1):
        result += [j] * count[j]
    return result

import random
array = [random.randint(0,1000000) for i in range(__N__)]

mn,mx = min(array),max(array)
