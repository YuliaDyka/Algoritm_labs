file = open("input.txt", "r")

start = tuple(map(int, file.readline().split(" ")))
end = tuple(map(int, file.readline().split(" ")))
size = tuple(map(int, file.readline().split(" ")))

matrix = []
for _ in range(size[0]):
    matrix.append(list(map(int, file.readline().split(" "))))

file.close()

graph = {}
for x in range(size[0]):
    for y in range(size[1]):
        tmp = []
        if not matrix[x][y]:
            continue
        tmp.append((x, y))
        tmp.append([])
        if x > 0:
            if matrix[x-1][y]:
                tmp[1] += [(x - 1, y)]
        if x < size[0] - 1:
            if matrix[x+1][y]:
                tmp[1] += [(x+1, y)]
        if y > 0:
            if matrix[x][y-1]:
                tmp[1] += [(x, y-1)]
        if y < size[1] - 1:
            if matrix[x][y+1]:
                tmp[1] += [(x, y+1)]
        graph[tmp[0]] = tmp[1]

#BFS function  
def main():
    neighbours_queue = []
    neighbours_queue.append(start)
    visited = []
    prev_point_dist = {}
    prev_point_dist[start] = (None, 0)
    while neighbours_queue:
        current_vertex = neighbours_queue[0]
        if current_vertex == end:
            return prev_point_dist[end][1]
        visited.append(current_vertex)
        neighbours = graph[current_vertex]
        for neighbour in neighbours:
            if neighbour not in visited:
                prev_point_dist[neighbour] = (current_vertex, prev_point_dist[current_vertex][1] + 1)
                neighbours_queue.append(neighbour)
        neighbours_queue.remove(current_vertex)
    return False

print(main())