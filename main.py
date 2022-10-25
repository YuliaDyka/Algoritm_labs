n, b = 3, 4
prefer = ["NYNN", "NYNY", "YNYN"]

format_prefer = [[] for _ in range (n)]

for x in range(n):
    for y in range(b):
        if prefer[x][y] == "Y":
            format_prefer[x].append(y)

def main(format_prefer: list, n: int, b: int, multiplier: int):
    if n <= 1:
        return 1 + multiplier

    split_prefer = [[],[]]

    for x in format_prefer:
        if len(x) == 1:
            split_prefer[0].append(x[0])
        else:
            split_prefer[1].append(x)


    if not split_prefer[0]:
        join_prefer = []
        same = []
        
        for x in split_prefer[1]:
            join_prefer += x

        for x in split_prefer[1]:
            same += get_same(join_prefer, x)
            print(same)
            split_prefer[0].append(max(set(same), key=same.count))
            same = []

    split_prefer[0] = del_equal(split_prefer[0])
        
    if len(split_prefer[1]) == 0:
        return len(split_prefer[0] + multiplier)

    tmp = []
    c = []

    for x in range(b):
        for y in range(len(split_prefer[1])):
            if x in split_prefer[0] and x in split_prefer[1][y]:
                c += [y] 

    c = del_equal(c)

    if len(split_prefer[1]) == len(c):
        return len(split_prefer[0]) + multiplier
    
    for x in range(len(split_prefer[1])):
        if x not in c:
            tmp += [split_prefer[1][x]]
            
    return main(tmp, len(tmp), b, len(split_prefer[0])+multiplier)

def get_same(arr1: list, arr2: list):
    res = []
    for x in arr1:
        if x in arr2:
            res += [x]
    return res

def del_equal(arr: list):
    if not arr:
        return []
    arr.sort()
    a = [arr[0]]
    for x in range(1, len(arr)):
        if not(arr[x] == arr[x-1]):
            a.append(arr[x])
    return a

print(main(format_prefer, n, b, 0))