"""An implementation of a min-heap with mutable keys"""

from typing import List

class Node:
    def __init__(self, data, key, index):
        self.data = data
        self.key = key
        self.index = index

class MutableHeap:

    def __init__(self):
        self._heap = list()
    
    def __len__(self):
        return len(self._heap)

    def peek(self) -> object:
        try:
            self._heap[0]
        except IndexError as err:
            err.message = "peek() on an empty heap."
            raise
    
    def pop(self) -> object:
        heap = self._heap
        try:
            self.swap(heap[0], heap[-1])
            node = self._heap.pop()
        except IndexError as err:
            err.message = "pop() on an empty heap."
            raise
        if heap:
            self.sift_down(heap, heap[0])
        return node.data
    
    def insert(self, data: object, key: object) -> object:
        heap = self._heap
        node = Node(data, key, index = len(self._heap))
        data.node = node
        heap.append(node)
        self.sift_up(heap, node)
        return data
    
    @staticmethod
    def swap(a: Node, b: Node) -> None:
        a.key, b.key = b.key, a.key
        a.data, b.data = b.data, a.data
        a.data.node = a
        b.data.node = b
    
    def sift_up(self, heap: List[Node], node: Node) -> None:
        parent = heap[(node.index - 1) // 2]

        while node.index > 0 and node.key < parent.key:
            self.swap(parent, node)
            node = parent
            parent = heap[(node.index - 1) // 2]
    
    def sift_down(self, heap: List[Node], node: Node) -> None:
        size = len(heap)
        left_child_pos = 2 * node.index + 1
        if left_child_pos < size:
            left_child = heap[left_child_pos]
        else:
            left_child = None

        right_child_pos = 2 * node.index + 2
        if right_child_pos < size:
            right_child = heap[right_child_pos]
        else:
            right_child = None
        
        while (left_child and node.key > left_child.key) or (right_child and node.key > right_child.key):
            target = min([child for child in (left_child,right_child) if child is not None], key = lambda x: x.key)
            self.swap(target, node)

            node = target
            left_child_pos = 2 * node.index + 1
            if left_child_pos < size:
                left_child = heap[left_child_pos]
            else:
                left_child = None
                    
            right_child_pos = 2 * node.index + 2
            if right_child_pos < size:
                right_child = heap[right_child_pos]
            else:
                right_child = None
    
    def change_key(self, node: Node, new_key) -> None:
        heap = self._heap
        if new_key < node.key:
            node.key = new_key
            self.sift_up(heap, node)
        elif new_key > node.key:
            node.key = new_key
            self.sift_down(heap, node)
            