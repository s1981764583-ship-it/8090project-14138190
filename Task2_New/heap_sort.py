from heap_ds import MaxHeap

def heap_sort(arr):
    if not isinstance(arr, list) or len(arr) <= 1:
        return arr
    heap = MaxHeap(capacity=len(arr))
    for num in arr:
        heap.insert(num)
    sorted_res = []
    while not heap.is_empty():
        sorted_res.append(heap.extract_max())
    return sorted_res[::-1]

# Time complexity analysis: O(nlogn)