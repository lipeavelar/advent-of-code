def get_antinode(pt1, pt2):
    x1, y1 = pt1
    x2, y2 = pt2
    delta_x = x2 - x1
    delta_y = y2 - y1
    new_x = x2 + delta_x
    new_y = y2 + delta_y
    antinode.add((x2, y2))
    while 0 <= new_x < N and 0 <= new_y < M:
      antinode.add((new_x, new_y))
      new_x = new_x + delta_x
      new_y = new_y + delta_y

with open('input.txt') as f:
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
