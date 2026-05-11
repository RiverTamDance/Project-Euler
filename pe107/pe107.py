import numpy as np

def search(current, target, seen=None):
    neighbours = {node for edge in adjacency for node in edge if current in edge}
    neighbours.remove(current)
    if not seen:
        seen = {current}
        return any(search(n,target, seen) for n in neighbours if n != target)
    
    if target in neighbours:
        return True
    elif neighbours.issubset(seen):
        return False
    else:
        seen = seen | {current}
        return any([search(n,target, seen) for n in neighbours if n not in seen])

if __name__ == "__main__":
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

    adjacency = {(n[0],n[1]) for n in adjacency_list if n[2] != 0}

    i=0
    for edge in adjacency_list:
        n1, n2, _ = edge
        i+=1
        print(f"considering {i}")
        if search(n1, n2):
            print(f"{n1},{n2} removed")
            adjacency.remove((n1,n2))
    
    print(len(adjacency))

    print(sum([edge[2] for edge in adjacency_list]))