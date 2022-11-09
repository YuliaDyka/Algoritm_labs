file = open("input.txt", "r")

w, h = map(int, file.readline().split(" "))
arr = [x[:w] for x in file.readlines()]

file.close()

arr_mem = [[0 for _ in range(w)] for _ in range(h)]

current = 0

for x in range(w):
    for y in range(h):
        if x == 0:
            arr_mem[y][x] = 1
            continue
        current = arr_mem[y][x-1] if arr[y][x] != arr[y][x-1] else 0

        for i in range(h):
            for j in range(x):
                if arr[y][x] == arr[i][j]:
                    current += arr_mem[i][j]

        arr_mem[y][x] = current

res = arr_mem[0][-1] + arr_mem[-1][-1] if h > 1 else arr_mem[0][-1]
print(res)

        