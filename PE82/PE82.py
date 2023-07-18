"""
PE 82
Created by Taylor Richards
taylordrichards@gmail.com
March 31, 2021 
"""

""" ---------------- PROBLEM STATEMENT ----------------

The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the 
left column and finishing in any cell in the right column, and only moving up, down, and right

"""
""" ---------------- Discussion ----------------

Because I had a looksee in the solution for PE81, I learned about Djikstra's Algorithm and Bellman-Ford. Because our matrix
doesn't contain negative values, i do not believe there is an advantage to using BF.

This does seem to clarify/simplify what I have to do. I hope.

1. determine if I can use Djikstra's algo on this problem. I think it requires me constructing a graph, where there is an
   an edge between nodes a and b if b is above, below, or to the right of a.

2. I want to write this as object, so i will finally have to try some python OOP.


"""
""" ---------------- Approach ----------------
"""

"""
I have returned for round 2, 2 years later hahahaha.

"""
"""
Created by Taylor Richards
taylordrichards@gmail.com
July 15, 2023


-----------------Plan-----------------

I believe I will proceed in two stages. 
   1. The first stage will involve data. So, loading in the table of values,
      then transforming that table of values into a nice little graph object.
         - I will use an adjacency matrix to represent my grap, I think.
   2. Stage 2 will be the application of Dijsktra's algorithm to my graph object.
   3. I will need to run the program over the 81 values in the first column and
      pick the winner.

More details:
 - I think it could be cool to try and use the @property decorator, and transform
   my graph representation that way. I will need to think about this some more.
 - Coming to think of it, I believe I will need a method that transforms that input
   table of values into some representation of a graph. Because each node (table entry)
   is adjacent to its up, down, and right neighbour.

https://stackoverflow.com/questions/7374748/whats-the-difference-between-a-python-property-and-attribute
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

      def last_column(self):
         last_column = dict()
         for (i,row) in enumerate(self.raw_table):
            last_column[(i,len(row)-1)] = self.adj_list[(i,len(row)-1)][0]
         return(last_column)


   # g = Graph(matrix, (1,0))
   # g.dijkstra_algo()
   # lc = g.last_column()
   # print(lc)
   
   best_so_far = ["start", "end", float('inf')]
   for (rownum,_) in enumerate(matrix):
      g = Graph(matrix, (rownum,0))
      g.dijkstra_algo()
      lc = g.last_column()
      if rownum == 50:
         print('here!')

      for k,v in lc.items():
         if v < best_so_far[2]:
            best_so_far = [(rownum,0), k, v]
            print(best_so_far)

   print(best_so_far)


#runtime: 875 seconds




   end_time = time.perf_counter()
   print("--- %s seconds ---" % (end_time - start_time))

if __name__ == "__main__":
   main()