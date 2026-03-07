# Task2: Self-studied New Data Structure + New Algorithm
## Selection Description
- **New Data Structure**: Max Heap (the course only covers stack, queue, binary search tree, not heap)
- **New Algorithm**: Heap Sort (the course only covers merge/selection/bubble/pigeonhole sort, not heap sort)

### Module Description
1. heap_ds.py: Self-implemented Max Heap ADT, implement core methods of heap (insert, extract max, heapify, etc.)
2. heap_sort.py: Implement heap sort algorithm based on self-implemented heap, analyze time complexity O(nlogn)
3. test_demo.py: Joint test of heap structure and heap sort, demonstrate running effect

### Core Implementation
#### Max Heap (ADT)
- Abstract Data Type definition: clarify heap attributes and core operations
- Core methods: insert (sift up), extract max (sift down), get max, check empty/full, etc.
- Underlying implementation: based on Python list, encapsulate private attributes, provide controllable public interfaces

#### Heap Sort
- Implementation logic: build max heap → extract max in turn → reverse to get ascending array
- Time complexity: O(nlogn) (best/worst/average are all O(nlogn))
- Space complexity: O(n) for pre-submission version, will be optimized to in-place heap sort O(1) later

### Running Method
1. Test heap structure: python heap_ds.py
2. Test heap sort: python heap_sort.py
3. Joint test: python test_demo.py

### Future Plans
- Add Min Heap implementation, compare application scenarios of Max Heap and Min Heap
- Optimize heap sort to in-place heap sort, reduce space complexity to O(1)
- Add practical application cases of heap (priority queue, TopK problem)
- Improve time/space complexity analysis, add charts and comparison experiments