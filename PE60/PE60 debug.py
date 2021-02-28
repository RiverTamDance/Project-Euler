subprimes = [[2,3],[2,4],[3,4],[3,5]]

flat_subprimes = {p for pair in subprimes for p in pair}
graph_dict = {node : {adj_node for edge in [edge for edge in subprimes if node in edge] 
             for adj_node in edge if adj_node != node} for node in flat_subprimes}

def cycle_delver(node, n, subgraph):

    #Hmmm i'm really not sure if this base case helps us exit properly
    
    #now I can assume that the list graph_dict[node] is sorted. which is v useful. 

    if n == 0:
        return([[node]])
    else:
        paths = []
        for adj_node in graph_dict[node]:
            if adj_node > node:
                if graph_dict[adj_node].issuperset(subgraph):
                    paths = paths + [[node] + path for path in cycle_delver(adj_node, n-1, subgraph.union({adj_node}))]

        return(paths)

        ###the issue with nogo is that [2,3,2] becomes [2,3,[]] or something and thats not permitted so it fails. need to think.
        
        #return([[node] + path for path in [more_itertools.collapse(cycle_delver(adj_node, n-1)) for adj_node in graph_dict[node]]])

# print(graph_dict[2].issuperset({}))
#print(graph_dict)
# print(set().issuperset({2}))
print(cycle_delver(2,2,{2}))