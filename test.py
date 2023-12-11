from main import *
import pytest

# Фікстура для створення нового об'єкту DynamicArray для кожного тесту
@pytest.fixture
def dynamic_array():
    return DynamicArray()

def test_initialization():
    arr = DynamicArray()
    assert arr.size() == 0

def test_insert_and_get_element(dynamic_array):
    dynamic_array.insert(0, 5)
    assert dynamic_array[0] == 5

def test_insert_out_of_range(dynamic_array):
    with pytest.raises(IndexError):
        dynamic_array.insert(5, 10)

def test_delete_element(dynamic_array):
    dynamic_array.insert(0, 8)
    dynamic_array.delete(0)
    assert dynamic_array.size() == 0

def test_delete_out_of_range(dynamic_array):
    with pytest.raises(IndexError):
        dynamic_array.delete(5)

def test_resize(dynamic_array):
    for i in range(12):
        dynamic_array.insert(i, i)
    assert dynamic_array.size() == 12
    assert dynamic_array._capacity == 20
