"""
Created by Taylor Richards
taylordrichards@gmail.com
July 17, 2023
"""
import time
import csv
from operator import itemgetter

def main():
    start_time = time.perf_counter()

    test_input = [[131, 673, 234, 103, 18],
                 [201, 96, 342, 965, 150],
                 [630, 803, 746, 422, 111],
                 [537, 699, 497, 121, 956],
                 [805, 732, 524, 37, 331]]

    with open('C:\\Users\\Taylo\\OneDrive\\Documents\\Project Euler\\PE82\\0082_matrix.txt') as f:
        reader = csv.reader(f)
        str_matrix = list(reader)
        matrix = [[int(entry) for entry in row] for row in str_matrix]

   
   #structure of the raw table
   #[row1, row2, ..., row80], where each row is a list of values.
   #So the "third" entry in the matrix, that is (0,2), 
   #should be found at matrix[0][2] 
   #print(str_matrix[0][2])

    def adjacency_list(table):
         
        adj_list = dict()

        for (i,row) in enumerate(table):
            for (j,_) in enumerate(row):
            
                adj_list[(i,j)] = [float('inf'), table[i][j]]
                adj_set = set()

                #moving up means i-1 
                if i-1 >= 0:
                    adj_set.add((i-1,j))
                #moving down means i+1 
                if i+1 <= len(table)-1:
                    adj_set.add((i+1,j))
                #moving left means j-1
                if j-1 >= 0:
                    adj_set.add((i,j-1))
                #and moving right means j+1
                if j+1 <= len(row)-1:
                    adj_set.add((i,j+1))

                adj_list[(i,j)].append(adj_set)

        return(adj_list)

    class Graph:
      
        def __init__(self, raw_table, start_node):
            self.raw_table = raw_table
            self.adj_list = adjacency_list(raw_table)
            self.start_node = start_node
            
        def dijkstra_algo(self):
            #stop condition: when we get to the rightmost column.
            #initialise the starting nodes running sum with itself.
            self.adj_list[self.start_node][0] = self.adj_list[self.start_node][1]
            unvisited = set(self.adj_list.keys())

            while unvisited:

                unvisited_and_sums = [(node, self.adj_list[node][0]) for node in unvisited]
                current_node = min(unvisited_and_sums, key=itemgetter(1))[0]
                potential_nodes = self.adj_list[current_node][2]

                for potential_node in potential_nodes:
                    best_sum_current_node = self.adj_list[current_node][0]
                    best_sum_potential_node = self.adj_list[potential_node][0]
                    weight_to_potential_node = self.adj_list[potential_node][1]

                    tentative_sum_potential_node = best_sum_current_node + weight_to_potential_node

                    if tentative_sum_potential_node < best_sum_potential_node:
                        best_sum_potential_node = tentative_sum_potential_node
                        self.adj_list[potential_node][0] = best_sum_potential_node
                
                unvisited.discard(current_node)

    in_table = matrix

    n = len(in_table) - 1
    bottom_right = (n,n)

    g = Graph(in_table, (0,0))
    g.dijkstra_algo()
    print(g.adj_list[(bottom_right)])
   
    end_time = time.perf_counter()
    print("--- %s seconds ---" % (end_time - start_time))

if __name__ == "__main__":
    main()