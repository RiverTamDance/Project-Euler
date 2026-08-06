import time
from collections import defaultdict

def cycle_detector(edge):
    left_node, right_node = edge[:2]
    #Get new left and right neighbours. if any neighbour sets are empty, break the loop

    left_neighbours = {node for node in adjacency[left_node] if node != right_node}
    seen = {left_node}

    while left_neighbours:

        if right_node in left_neighbours:
            return True
        else:
            seen |= left_neighbours
            left_neighbours = set().union(*(adjacency[k] for k in left_neighbours))
            left_neighbours -= seen
    
    return False
    

if __name__ == "__main__":
    start_time = time.time()
    with open("network.txt",'r') as f:
        adj_matrix = f.readlines()
        adj_matrix = [row.strip() for row in adj_matrix]
        adj_matrix = [row.split(',') for row in adj_matrix]
        adj_matrix = [
            [0 if n=='-' else int(n) for n in row]
            for row in adj_matrix 
        ]

    adjacency_list = []
    for n1, row in enumerate(adj_matrix):
        for n2, weight in enumerate(row[n1+1:]):
            n2 = n2 + n1 +1
            if weight != 0:
                adjacency_list.append((n1,n2,weight))
    
    adjacency_list.sort(key = lambda x: x[2], reverse = True)

    adjacency = defaultdict(set)
    for n1, n2, _ in adjacency_list:
        adjacency[n1].add(n2)
        adjacency[n2].add(n1)

    retained_edges = []
    for i, edge in enumerate(adjacency_list):
        if not cycle_detector(edge):
            retained_edges.append(edge)
        else:
            adjacency[edge[0]].remove(edge[1])
            adjacency[edge[1]].remove(edge[0])

    print(len(retained_edges))
    print(retained_edges)
    weight_old = sum([edge[2] for edge in adjacency_list])
    weight_new = sum([edge[2] for edge in retained_edges])
    savings = weight_old - weight_new
    print(savings)

    print("total time: %s seconds" % (time.time() - start_time))
    