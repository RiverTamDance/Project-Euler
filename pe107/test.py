from collections import defaultdict
adjacency = defaultdict(set)
adjacency[1].add(2)
adjacency[1].remove(2)
adjacency[2].add(10)
print(adjacency.items())

left_neighbours = [1,2,3]

left_neighbours = set().union(*(adjacency[k] for k in left_neighbours))
print(left_neighbours)