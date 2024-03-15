from typing import Any, List
from collections import deque


class Queue:
    """A simple implementation of a queue data structure."""

    def __init__(self):
        self._items: List[Any] = deque()

    def is_empty(self) -> bool:
        """Check if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return len(self._items) == 0

    def enqueue(self, item: Any) -> None:
        """Add an item to the end of the queue.

        Args:
            item (Any): The item to be added to the queue.
        """
        self._items.append(item)

    def dequeue(self) -> Any:
        """Remove and return the item at the front of the queue.

        Returns:
            Any: The item at the front of the queue, or None if the queue is empty.
        """
        if self.is_empty():
            return None
        return self._items.popleft()

    def size(self) -> int:
        """Get the number of items in the queue.

        Returns:
            int: The number of items in the queue.
        """
        return len(self._items)
