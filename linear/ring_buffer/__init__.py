from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Optional

T = TypeVar("T", str, int)


class RingBuffer(ABC, Generic[T]):
    """
    Abstract class for a basic implementation of a Ring Buffer, also called as a Circular Buffer or a Circular Queue.
    The current implementation only supports items of type String and Integer
    """
    @abstractmethod
    def put(self, item: T) -> None:
        pass

    @abstractmethod
    def get(self) -> Optional[T]:
        pass

    @abstractmethod
    def _print_representation(self):
        pass

    def __str__(self):
        return self._print_representation()
