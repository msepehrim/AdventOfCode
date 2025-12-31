from collections import defaultdict, deque

WHITE = "WHITE"
GRAY = "GRAY"
BLACK = "BLACK"
OUT = "out"

def BFS(graph, graph_color, start):
    graph_color[start] = GRAY
    Q = deque([start])
    path_count = 0
    while Q:
        u = Q.popleft()
        for v in graph[u]:
            # if graph_color[v] == WHITE:
            #     graph_color[v] = GRAY                
            if (v != OUT and v != start):
                Q.append(v)
            if (v == OUT):
                path_count += 1
        graph_color[u] = BLACK
    return path_count




with open("day11_input.txt") as input_file:
    lines = input_file.readlines()

graph = defaultdict(set)
graph_color = defaultdict(str)
for line in lines:
    key = line.split(":")[0].strip()
    values = line.split(":")[1].strip().split(' ')
    for value in values:
        graph[key].add(value.strip())
        # graph[value].add(None)
        graph_color[value] = WHITE
        graph_color[key] = WHITE


print(BFS(graph, graph_color, "you"))
# print(graph)
