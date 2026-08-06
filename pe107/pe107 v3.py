from collections.abc import Iterable
def prims(graph):
    
    #get initial edge
    pass


class BinaryHeap():
    """This is a min-heap, so the root is the smallest element """


    def __init__(self, input: list[int]) -> None:
        self.heap = []
        self._heapify(input)


    def _heapify(self, items):
        for value in items:
            self.insert(value)


    def insert(self, value):
        #this is the index of the leftmost open space

        idx = len(self.heap)
        parent_idx = (idx-1)//2
        self.heap.append(value)

        # percolate_up
        while self.heap[idx] < self.heap[max(parent_idx,0)]:
            #swap
            self.heap[parent_idx], self.heap[idx] = self.heap[idx], self.heap[parent_idx]
            idx = parent_idx
            parent_idx = (idx-1)//2
            

    def extract(self):
        pass

    def __repr__(self):
        return(repr(self.heap))

test_data = [36, 1,25, 7, 100, 19, 2, 17,3]

print(BinaryHeap(test_data))