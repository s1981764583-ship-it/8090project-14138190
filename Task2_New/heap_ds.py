class MaxHeap:
    def __init__(self, capacity=10):
        self.__capacity = capacity
        self.__heap = []
        self.__size = 0

    def __parent(self, idx):
        return (idx - 1) // 2

    def __left_child(self, idx):
        return 2 * idx + 1

    def __right_child(self, idx):
        return 2 * idx + 2

    def __swap(self, i, j):
        self.__heap[i], self.__heap[j] = self.__heap[j], self.__heap[i]

    def __sift_up(self, idx):
        while idx > 0 and self.__heap[idx] > self.__heap[self.__parent(idx)]:
            self.__swap(idx, self.__parent(idx))
            idx = self.__parent(idx)

    def __sift_down(self, idx):
        max_idx = idx
        left = self.__left_child(idx)
        if left < self.__size and self.__heap[left] > self.__heap[max_idx]:
            max_idx = left
        right = self.__right_child(idx)
        if right < self.__size and self.__heap[right] > self.__heap[max_idx]:
            max_idx = right
        if idx != max_idx:
            self.__swap(idx, max_idx)
            self.__sift_down(max_idx)

    def insert(self, value):
        if self.__size >= self.__capacity:
            raise IndexError("Heap is full, cannot insert new element")
        self.__heap.append(value)
        self.__size += 1
        self.__sift_up(self.__size - 1)

    def extract_max(self):
        if self.is_empty():
            raise IndexError("Heap is empty, cannot extract max element")
        max_val = self.__heap[0]
        self.__heap[0] = self.__heap[-1]
        self.__heap.pop()
        self.__size -= 1
        self.__sift_down(0)
        return max_val

    def get_max(self):
        if self.is_empty():
            raise IndexError("Heap is empty, no max element")
        return self.__heap[0]

    def is_empty(self):
        return self.__size == 0

    def get_size(self):
        return self.__size

    def print_heap(self):
        print(f"Max Heap (Capacity: {self.__capacity}, Size: {self.__size}): {self.__heap}")