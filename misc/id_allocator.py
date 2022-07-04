from typing import List


class IdAllocator:
    """
    An efficient implementation of an ID Allocator using a Binary Heap.

    The simplest implementation of an ID Allocator would be to use a set to store allocated IDs and a Deque to
    store released IDs. Both `allocate` and `release` take O(1) time but this implementation requires a lot of
    space. What if the IDs are 10-digit phone numbers and there can be a 10 million phone numbers?

    Another version to optimize space is to use a simple Bitset. We can keep an array for each possible ID value and
    set a bit at position MAX_VAL - MIN_VAL + ID if the ID is allocated and unset when it is released. For this
    implementation, both `allocate` and `release` take O(n) time.

    Am optimization to the above Bitset version is to use a heapified Bitset to reduce `allocate` and `release` times
    to be O(log n). The idea is to create a Bitset of size twice the range of IDs. Using the property of Heap that each
    level can contain twice as many nodes as it's previous level, the last level (second-half of array) stores the
    information regarding whether an ID is allocated or not. All the levels above (first-half of array) has nodes that
    are set only if both children are set (allocated). This way, we try to find an available ID by checking subtrees
    instead of full tree. We are storing twice as many bits O(2n), but it's still linear and much less than the first
    implementation and has logarithmic time complexity for both operations.

    Python does not have a built-in Bitset, so we use an array of Booleans instead of a 0/1 Integer array because `bool`
    takes less space than `int` in Python.
    """
    def __init__(self, max_val: int):
        self._max_val: int = max_val
        self._heap_bitset: List[bool] = [False] * (2 * max_val)

    @property
    def max_value(self) -> int:
        return self._max_val

    def allocate(self) -> int:
        idx = 0
        if self._heap_bitset[idx]:
            raise Exception("No IDs available!")

        while idx < self.max_value:
            left = 2 * idx + 1
            right = 2 * idx + 2
            if left < len(self._heap_bitset) and not self._heap_bitset[left]:  # there's an unallocated ID in the left subtree
                idx = left
            elif right < len(self._heap_bitset) and not self._heap_bitset[right]:  # there's an unallocated ID in the right subtree
                idx = right
            else:
                # both subtrees below are fully allocated, the best available position is current `idx`
                break

        id_value = self.get_id_value_from_id_position(idx)
        self._heap_bitset[idx] = True
        self._update_tree(idx)
        return id_value

    def release(self, id_value: int) -> None:
        if not 0 <= id_value < self.max_value:
            raise Exception("The ID '{}' cannot be released, invalid ID".format(id_value))

        id_position = self.get_id_position_from_id_value(id_value)
        if not self._heap_bitset[id_position]:
            raise Exception("The ID '{}' cannot be released, ID is not allocated".format(id_value))

        self._heap_bitset[id_position] = False
        self._update_tree(id_position)

    def get_id_position_from_id_value(self, id_value: int) -> int:
        return id_value + self.max_value

    def get_id_value_from_id_position(self, id_position: int) -> int:
        return id_position - self.max_value

    def _update_tree(self, idx: int) -> None:
        while idx > 0:
            parent = (idx - 1) // 2
            left, right = 2 * parent + 1, 2 * parent + 2
            self._heap_bitset[parent] = False
            if (left >= len(self._heap_bitset) or self._heap_bitset[left]) and (right >= len(self._heap_bitset) or self._heap_bitset[right]):
                self._heap_bitset[parent] = True
            idx = parent
        self._heap_bitset[0] = self._heap_bitset[1] and self._heap_bitset[2]


if __name__ == '__main__':
    ida = IdAllocator(max_val=5)
    print(ida.allocate())
    print(ida.allocate())
    print(ida.allocate())
    print(ida.allocate())
    print(ida.allocate())
    ida.release(4)
    print(ida.allocate())
    ida.release(4)
    print(ida.allocate())
    ida.release(4)
    print(ida.allocate())
    ida.release(3)
    print(ida.allocate())
