targetsum = 7
arr = [5, 3, 4, 7]


def bestsum(targetsum, arr):
    if targetsum == 0:
        return []
    if targetsum < 0:
        return None
    shortest = None
    for num in arr:
        reminder = targetsum - num
        result = bestsum(reminder, arr)
        if result != None:
            comb = [num, *result]
            if shortest == None or len(comb) < len(shortest):
                shortest = comb
    return shortest


print(bestsum(targetsum, arr))
