def get_antinode(pt1, pt2):
    x1, y1 = pt1
    x2, y2 = pt2
    new_x = x2 + (x2 - x1)
    new_y = y2 + (y2 - y1)
    if new_x < 0 or new_x >= N or new_y < 0 or new_y >= M:
        return
    antinode.add((new_x, new_y))

with open('example.txt') as f:
    city_map = [line.strip() for line in f.readlines()]

N = len(city_map)
M = len(city_map[0])

nodes = {}
antinode = set()

for i in range(N):
    for j in range(M):
        if city_map[i][j] != ".":
            if city_map[i][j] not in nodes:
                nodes[city_map[i][j]] = []
            nodes[city_map[i][j]].append((i,j))

for node in nodes.keys():
    nodes_list = nodes[node]
    for i in range(len(nodes_list)):
        for j in range(i):
            node1 = nodes_list[i]
            node2 = nodes_list[j]
            get_antinode(node1, node2)
            get_antinode(node2, node1)

print(len(antinode))
