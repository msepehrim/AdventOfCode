from collections import defaultdict, deque

WHITE = "WHITE"
GRAY = "GRAY"
BLACK = "BLACK"
OUT = "out"

def BFS(graph, graph_color, start):
    graph_color[start] = GRAY
    Q = deque([start])
    path_count = 0
    dac_count = 0
    fft_count = 0
    while Q:
        u = Q.popleft()
        print(u)
        for v in graph[u]:
            # if graph_color[v] == WHITE:
            #     graph_color[v] = GRAY                
            if (v != OUT and v != start):
                Q.append(v)
            if (v == "dac"):
                dac_count += 1
            if (v == "fft"):
                fft_count += 1
            if (v == OUT):
                if dac_count == fft_count == 1:
                    path_count += 1
                dac_count = 0
                fft_count = 0
        graph_color[u] = BLACK
    return path_count




with open("day11_input_test_2.txt") as input_file:
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


print(BFS(graph, graph_color, "svr"))
# print(graph)
