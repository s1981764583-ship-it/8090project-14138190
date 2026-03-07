from heap_ds import MaxHeap
from heap_sort import heap_sort

if __name__ == "__main__":
    print("===== Self-implemented Max Heap Test =====")
    heap = MaxHeap(10)
    for num in [8,5,6,2,9,1,7]:
        heap.insert(num)
    heap.print_heap()
    print(f"Max Element: {heap.get_max()}, Heap Size: {heap.get_size()}")
    print(f"Extract Max: {heap.extract_max()}")
    heap.print_heap()

    print("\n===== Self-implemented Heap Sort Test =====")
    test_cases = [
        [5,2,9,1,5,6],
        [9,8,7,6,5,4],
        [1,2,3,4,5,6],
        []
    ]
    for case in test_cases:
        print(f"Original: {case} → Sorted: {heap_sort(case)}")