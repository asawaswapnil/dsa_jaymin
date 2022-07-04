from typing import List, Union, Optional

from linear.ring_buffer import RingBuffer, T


class RingBufferBasic(RingBuffer[T]):
    """
    A basic implementation of a Ring Buffer, also called as a Circular Buffer or a Circular Queue using Python List.
    All operations are O(1) except for the initialization which take O(n). This can be improved to using just one
    pointer and appending to the list but since this is just for illustrative purpose, it is kept as-is.
    There is a more optimized version that use a Deque, check out `RingBufferOptimized` below

    Reference: https://en.wikipedia.org/wiki/Circular_buffer
    """

    def __init__(self, capacity: int, allow_override: bool = True):
        self._buffer: List[Union[T, None]] = [None for _ in range(capacity)]
        self._capacity = capacity
        self._allow_override = allow_override
        self._size = 0
        self._head = 0
        self._tail = 0

    def put(self, item: T) -> None:
        """
        Put/add/enqueue an item to the ring buffer
        """
        if not self._allow_override and self._size == self._capacity:
            raise OverflowError("RingBuffer is full, unable to put item!")
        self._buffer[self._tail] = item
        self._size = min(self._size + 1, self._capacity)
        self._tail = (self._tail + 1) % self._capacity

    def get(self) -> Optional[T]:
        """
        Get/remove/dequeue the oldest item from the ring buffer
        """
        if self._size == self._capacity:
            self._head = self._tail
        item = self._buffer[self._head]
        self._buffer[self._head] = None
        self._size = max(self._size - 1, 0)
        self._head = (self._head + 1) % self._capacity
        return item

    def _print_representation(self):
        return "RingBuffer[{}]@{}: {}\n-> Buffer: {}\n-> Size: {}\n-> Start: {}\n-> End: {}".format(
            self._capacity,
            id(self),
            self._allow_override and "With Override" or "Without Override",
            self._buffer,
            self._size,
            self._head,
            self._tail
        )


if __name__ == '__main__':
    rb = RingBufferBasic[str](4)
    print(rb)

    print("\nPut 'A'")
    rb.put("A")
    print(rb)

    print("\nPut 'B'")
    rb.put("B")
    print(rb)

    print("\nPut 'C'")
    rb.put("C")
    print(rb)

    print("\nPut 'D'")
    rb.put("D")
    print(rb)

    print("\nPut 'E'")
    rb.put("E")
    print(rb)

    print("\nPut 'F'")
    rb.put("F")
    print(rb)

    print("\nGet")
    print(rb.get())  # should be "C"
    print(rb)
