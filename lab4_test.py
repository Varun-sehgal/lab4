from lab4 import *


def test_get_sum():
    assert get_sum([3.5, 1.2, 0, 8]) == 12.7, "get_sum() failed"
    assert get_sum([11.04]) == 11.04, "get_sum() failed"
    assert get_sum([]) == 0.0, "get_sum() failed"


def test_only_non_negative_sum():
    assert only_non_negative_sum([-1.2, 5, -0.4]) == 5, "only_non_negative_sum() failed"
    assert only_non_negative_sum([-8.7, -2.15, -3.67, -4.80754]) == 0.0, "only_non_negative_sum() failed"


def test_copy_even():
    assert copy_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14]) == [2, 4, 6, 8, 10, 12, 14], "copy_even() failed"
    assert copy_even([-10, 0]) == [-10, 0], "copy_even() failed"


def test_copy_start_with_a():
    lst1 = ['haha', 'hehe', 'ahaha', 'a book']
    assert copy_start_with_a(lst1) == ['ahaha', 'a book'], "copy_start_with_a() failed"
    lst2 = ['', 'Alex', ' ']
    assert copy_start_with_a(lst2) == ['Alex'], "copy_start_with_a() failed"


def test_copy_reverse():
    assert copy_reverse([1.1, 2.2, 3.3, 4.4]) == [4.4, 3.3, 2.2, 1.1], "copy_reverse() failed"
    assert copy_reverse([4.567]) == [4.567], "copy_reverse() failed"
    assert copy_reverse([]) == [], "copy_reverse() failed"


def test_reverse():
    lst1 = [0.7, 2, 1, 13.4]
    reverse(lst1)
    assert lst1 == [13.4, 1, 2, 0.7], "reverse() failed"


def test_cartesian_product():
    assert cartesian_product([1.1, 2.2, 8], [3.3, 4.6, 2]) == [3.63, 10.12, 16], "cartesian_product() failed"


def test_sort_number():
    lst1 = [3, 2, 1]
    sort_number(lst1)
    assert lst1 == [1, 2, 3], "sort_number() failed"
    lst2 = [-10]
    sort_number(lst2)
    assert lst2 == [-10], "sort_number() failed"


def sort_sort_fish():
    fish_lst = [Fish("Alice", 12, 50, "Salmon", "Fresh"), Fish("Bob", 7, 32, "Catfish", "Fresh"), Fish("Charlie", 2, 100, "Goldfish", "Fresh"), Fish("Dana", 20, 80, "Shark", "Salt")]
    sort_fish(fish_lst)
    assert fish_lst == [Fish("Dana", 20, 80, "Shark", "Salt"), Fish("Alice", 12, 50, "Salmon", "Fresh"), Fish("Bob", 7, 32, "Catfish", "Fresh"), Fish("Charlie", 2, 100, "Goldfish", "Fresh")], "sort_fish() failed"
