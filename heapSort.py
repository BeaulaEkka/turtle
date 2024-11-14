'''
pseudocode:
siftdown(list,parent,idx,upper):
repeat:
    if parent has two children:
        if parent > both children:
            end subroutine
    else:
        swap parent eith greater child
        set parent idx to child idx
    else if parent has one child:
        if parent>child:
            end subroutine
    else:
        swap parent with greater child
        set parent idx to child idx
    else:
        parent has no child, end subroutine

'''


class HeadSort:
    def __init__(self):
        self.heap = []

    def swap(lst, i, j):
        lst[i], lst[j] = lst[j], lst[i]

    def siftDown(lst, i, upper):
        while (True):
            l, r = i*2+1, i*2+2
            if max(l, r) < upper:
                if lst[i] >= max(lst(l), lst[r]):
                    break

    def heapsort(lst):
    pass
