Point = tuple[int, int, int]
Row = list[int]
Matrix = list[Row]
AdjacencyMatrix = list[tuple[int, int]]

def distance(point1 : Point, point2 : Point) -> int:
    x1, y1, z1 = map(int, point1.split(','))
    x2, y2, z2 = map(int, point2.split(','))
    return (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2 

def min_position(matrix: Matrix) -> tuple[int,int]:
    return min(
        ((r, c) for r, row in enumerate(matrix)
                for c, val in enumerate(row) if val != 0),
    key = lambda pos: matrix[pos[0]][pos[1]]
)

def other(item: int, edge: tuple[int, int]) -> int:
    if edge[0] == item:
        return edge[1]
    elif edge[1] == item:
        return edge[0]
    else:
        return None

def does_path_exist(matrix: AdjacencyMatrix, point1_index: int, point2_index : int) -> bool:
    point1_edges = [edge for edge in matrix if point1_index in edge]
    point2_edges = [edge for edge in matrix if point2_index in edge]
    if not point1_edges or not point2_edges:
        return False    
    # adjacenct points to point1
    edges_list = [other(point2_index, edge) for edge in matrix if point1_index in edge]
    
    
    for p in other_points_list:
        does_path_exist(matrix, p, point2_index)

    return False
    
# adjacency_matrix =  
with open("day08_input_test.txt") as input_file:
    point_list = input_file.readlines()

    distance_matrix : Matrix = []   
    for i in range(len(point_list)):
        row : Row = []
        for j in range(len(point_list)):
            row.extend([distance(point_list[i], point_list[j])] if j > i else [0])
        distance_matrix.append(row)

min_pos = min_position(distance_matrix) 

print(distance_matrix)
print(min_pos)