from collections import deque
from typing import Optional, Deque

from linear.ring_buffer import RingBuffer, T


class RingBufferOptimized(RingBuffer[T]):
    """
    An optimized version of Ring Buffer using collections.deque
    All operations are O(1)
    """

    def __init__(self, capacity: int, allow_override: bool = True):
        self._buffer: Deque[T] = deque([], maxlen=capacity)
        self._capacity = capacity
        self._allow_override = allow_override

    def put(self, item: T) -> None:
        """
        Put/add/enqueue an item to the ring buffer
        """
        if not self._allow_override and len(self._buffer) == self._capacity:
            raise OverflowError("RingBuffer is full, unable to put item!")
        self._buffer.append(item)

    def get(self) -> Optional[T]:
        """
        Get/remove/dequeue the oldest item from the ring buffer
        """
        return self._buffer.popleft()

    def _print_representation(self):
        return "RingBufferOptimized[{}]@{}: {}\n-> Buffer: {}\n-> Size: {}".format(
            self._capacity,
            id(self),
            self._allow_override and "With Override" or "Without Override",
            list(self._buffer),
            len(self._buffer)
        )


if __name__ == '__main__':
    rb = RingBufferOptimized[str](4)
    print(rb)
    rb.put("A")
    print(rb)
    rb.put("B")
    print(rb)
    rb.put("C")
    print(rb)
    rb.put("D")
    print(rb)
    rb.put("E")
    print(rb)
    rb.put("F")
    print(rb)
    print(rb.get())  # should be "C"
    print(rb)
