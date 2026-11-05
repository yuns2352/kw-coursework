# ds.py
from __future__ import annotations
from typing import Any, Optional

class ArrayList:

    def __init__(self):
        self._data: list[Any] = []

    def append(self, value: Any) -> None:
        """# Time: O(1) amortized, Space: O(1)
        Append value to the end.
        """
        self._data.append(value)

    def insert(self, index: int, value: Any) -> None:
        """# Time: O(n), Space: O(1)
        Insert value at index, shifting elements to the right.
        Raise IndexError if index is out of range [0, size].
        """
        n = len(self._data)
        if index < 0 or index > n:
            raise IndexError("ArrayList.insert : index out of range")
        self._data.insert(index, value)

    def remove(self, index: int) -> Any:
        """# Time: O(n), Space: O(1)
        Remove and return the element at index, shifting left.
        Raise IndexError if index is out of range.
        """
        n = len(self._data)
        if index < 0 or index >= n:
            raise IndexError("ArrayList.remove : index out of range")
        return self._data.pop(index)

    def get(self, index: int) -> Any:
        """# Time: O(1), Space: O(1)
        Return element at index. Raise IndexError if out of range.
        """
        n = len(self._data)
        if index < 0 or index >= n:
            raise IndexError("ArrayList.get : index out of range")
        return self._data[index]

    def size(self) -> int:
        """# Time: O(1), Space: O(1)"""
        return len(self._data)

    def __len__(self) -> int:
        return self.size()

class _Node:

    def __init__(self, value: Any, next: Optional[_Node] = None):
        self.value = value
        self.next = next


class LinkedList:

    def __init__(self):
        self._head: Optional[_Node] = None
        self._size: int = 0

    def append(self, value: Any) -> None:
        """# Time: O(n), Space: O(1)
        Append value to the end.
        """
        new_node = _Node(value)
        if self._head is None:
            self._head = new_node
        else:
            curr = self._head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
        self._size += 1

    def _node_at(self, index: int) -> _Node:
        """# Time: O(n), Space: O(1)
        Return node at index (0-based). Raise IndexError if out of range.
        """
        if index < 0 or index >= self._size:
            raise IndexError("LinkedList._node_at : index out of range")
        curr = self._head
        for _ in range(index):
            assert curr is not None # for type checker
            curr = curr.next
        assert curr is not None
        return curr

    def insert(self, index: int, value: Any) -> None:
        """# Time: O(n), Space: O(1)
        Insert value at index (0..size). Raise IndexError if out of range.
        """
        if index < 0 or index > self._size:
            raise IndexError("LinkedList.insert : index out of range")
        new_node = _Node(value)
        if index == 0:
            new_node.next = self._head
            self._head = new_node
        else:
            prev = self._node_at(index - 1)
            new_node.next = prev.next
            prev.next = new_node
        self._size += 1

    def remove(self, index: int) -> Any:
        """# Time: O(n), Space: O(1)
        Remove and return element at index. Raise IndexError if out of range.
        """
        if index < 0 or index >= self._size:
            raise IndexError("LinkedList.remove : index out of range")
        if index == 0:
            assert self._head is not None
            value = self._head.value
            self._head = self._head.next
        else:
            prev = self._node_at(index - 1)
            assert prev.next is not None
            value = prev.next.value
            prev.next = prev.next.next
        self._size -= 1
        return value

    def get(self, index: int) -> Any:
        """# Time: O(n), Space: O(1)
        Return element at index. Raise IndexError if out of range.
        """
        node = self._node_at(index)
        return node.value

    def size(self) -> int:
        """# Time: O(1), Space: O(1)"""
        return self._size

    def __len__(self) -> int:
        return self.size()


class Stack:

    def __init__(self):
        self._arr = ArrayList()

    def push(self, value: Any) -> None:
        """# Time: O(1) amortized, Space: O(1)"""
        self._arr.append(value)

    def pop(self) -> Any:
        """# Time: O(1) amortized (ArrayList remove at end), Space: O(1)
        Raise IndexError if empty.
        """
        if self._arr.size() == 0:
            raise IndexError("Stack.pop : empty stack")
        return self._arr.remove(self._arr.size() - 1)

    def peek(self) -> Any:
        """# Time: O(1), Space: O(1)
        Raise IndexError if empty.
        """
        if self._arr.size() == 0:
            raise IndexError("Stack.peek : empty stack")
        return self._arr.get(self._arr.size() - 1)

    def is_empty(self) -> bool:
        """# Time: O(1), Space: O(1)"""
        return self._arr.size() == 0

    def size(self) -> int:
        """# Time: O(1), Space: O(1)"""
        return self._arr.size()


class Queue:

    def __init__(self):
        self._head: Optional[_Node] = None
        self._tail: Optional[_Node] = None
        self._size: int = 0

    def enqueue(self, value: Any) -> None:
        """# Time: O(1), Space: O(1)"""
        node = _Node(value)
        if self._tail is None:
            # empty
            self._head = self._tail = node
        else:
            self._tail.next = node
            self._tail = node
        self._size += 1

    def dequeue(self) -> Any:
        """# Time: O(1), Space: O(1)
        Remove and return front element. Raise IndexError if empty.
        """
        if self._head is None:
            raise IndexError("Queue.dequeue : empty queue")
        value = self._head.value
        self._head = self._head.next
        if self._head is None:
            self._tail = None
        self._size -= 1
        return value

    def peek(self) -> Any:
        """# Time: O(1), Space: O(1)
        Return front element without removing. Raise IndexError if empty.
        """
        if self._head is None:
            raise IndexError("Queue.peek : empty queue")
        return self._head.value

    def is_empty(self) -> bool:
        """# Time: O(1), Space: O(1)"""
        return self._size == 0

    def size(self) -> int:
        """# Time: O(1), Space: O(1)"""
        return self._size
