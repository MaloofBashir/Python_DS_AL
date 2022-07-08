N = 2
A = [1]


def MissingNumber(array, n):
    new_arr = [False] * n
    for i in array:
        new_arr[i - 1] = True
    for i in range(len(new_arr)):
        if new_arr[i] == False:
            return i + 1


print(MissingNumber(A, N))
