class MaxHeap:
    def __init__(self):
        self.heap_list = [None]
        self.count = 0

    # HEAP HELPER METHODS
    # DO NOT CHANGE!
    def parent_idx(self, idx):
        return idx // 2

    def left_child_idx(self, idx):
        return idx * 2

    def right_child_idx(self, idx):
        return idx * 2 + 1

    # END OF HEAP HELPER METHODS

    def add(self, element):
        self.count += 1
        print(f'Adding: {element} to {self.heap_list}')
        self.heap_list.append(element)
        self.heapify_up()

    def heapify_up(self):
        print("Heapifying up")
        idx = self.count
        print(f'heapify idx=self.count:{idx}')
        while self.parent_idx(idx) > 0:
            child = self.heap_list[idx]
            print(f'child:{child}')
            parent = self.heap_list[self.parent_idx(idx)]
            print(f'parent:{parent}')
            if parent < child:
                print("swapping {0} with {1}".format(parent, child))
                self.heap_list[idx] = parent
                self.heap_list[self.parent_idx(idx)] = child
            idx = self.parent_idx(idx)
        print("Heap Restored {0}".format(self.heap_list))


heap = MaxHeap()
heap.add(5)
heap.add(10)


print(f'heap_list:{heap.heap_list}')
