"""
PyTest Test Cases

LC-0146: LRU Cache
"""

import pytest

from pathlib import Path
import importlib.util

solution_path = Path(__file__).parent / "solution.py"

spec = importlib.util.spec_from_file_location(
    "student_solution",
    solution_path,
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

LRUCache = module.LRUCache


def test_example_case():
    cache = LRUCache(2)

    cache.put(1, 1)
    cache.put(2, 2)

    assert cache.get(1) == 1

    cache.put(3, 3)

    assert cache.get(2) == -1

    cache.put(4, 4)

    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4


def test_update_existing_key():
    cache = LRUCache(2)

    cache.put(1, 1)
    cache.put(1, 10)

    assert cache.get(1) == 10


def test_capacity_one():
    cache = LRUCache(1)

    cache.put(1, 1)
    cache.put(2, 2)

    assert cache.get(1) == -1
    assert cache.get(2) == 2


def test_missing_key():
    cache = LRUCache(2)

    assert cache.get(100) == -1


def test_recent_access():
    cache = LRUCache(2)

    cache.put(1, 1)
    cache.put(2, 2)

    cache.get(1)

    cache.put(3, 3)

    assert cache.get(1) == 1
    assert cache.get(2) == -1


def test_return_type():
    cache = LRUCache(2)

    cache.put(1, 1)

    assert isinstance(cache.get(1), int)
