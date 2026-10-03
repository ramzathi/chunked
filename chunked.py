"""Split a sequence into fixed-size pieces."""
from __future__ import annotations

from typing import TypeVar

T = TypeVar("T")


def chunks(items: list[T], size: int) -> list[list[T]]:
    if size < 1:
        raise ValueError("每段至少 1 个")
    return [items[i : i + size] for i in range(0, len(items), size)]


def remainder(items: list[T], size: int) -> int:
    if size < 1:
        raise ValueError("每段至少 1 个")
    if not items:
        return 0
    return len(items) % size


def chunk_count(items: list[T], size: int) -> int:
    return len(chunks(items, size))
