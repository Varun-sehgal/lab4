from lab4 import *


def test_get_sum():
    assert get_sum([1.1, 2.2, 3.3, 4.4]) == 11.0, "get_sum() failed"
    assert get_sum([4.567]) == 4.567, "get_sum() failed"
    assert get_sum([]) == 0.0, "get_sum() failed"


def test_only_non_negative_sum():
    assert only_non_negative_sum([1.1, -2.2, 3.3, -4.4]) == 4.4, "only_non_negative_sum() failed"
    assert only_non_negative_sum([1.12, -10.8, -11.0567, 2.1, 4.6]) == 7.82, "only_non_negative_sum() failed"
    assert only_non_negative_sum([0.0]) == 0.0, "only_non_negative_sum() failed"
    assert only_non_negative_sum([-1.7, -2.45, -3.1, -4.7]) == 0.0, "only_non_negative_sum() failed"


def test_copy_even():
    assert copy_even([1, 2, 3, 4, 5, 6, 7, 8]) == [2, 4, 6, 8], "copy_even() failed"
    assert copy_even([-10, 0]) == [-10, 0], "copy_even() failed"


def test_copy_start_with_a():
    lst1 = ["Apricot", "Banana", "Allison", "a cookie"]
    copy_start_with_a(lst1)
    assert lst1 == ["Apricot", "Allison", "a cookie"], "copy_start_with_a() failed"
    lst2 = ["", " ", "Amy"]
    copy_start_with_a(lst2)
    assert lst2 == ["Amy"], "copy_start_with_a() failed"


def test_copy_reverse():
    assert copy_reverse([1.1, 2.2, 3.3, 4.4]) == [4.4, 3.3, 2.2, 1.1], "copy_reverse() failed"
    assert copy_reverse([4.567]) == [4.567], "copy_reverse() failed"
    assert copy_reverse([]) == [], "copy_reverse() failed"


def test_reverse():
    lst1 = [1.1, 2.2, 3.3, 4.4]
    reverse(lst1)
    assert lst1 == [4.4, 3.3, 2.2, 1.1], "reverse() failed"


def test_cartesian_product():
    assert cartesian_product([1.1, 2.2], [3.3, 4.4]) == [3.63, 9.68], "cartesian_product() failed"


def test_sort_number():
    lst1 = [4, 7, 8, 1, -2]
    sort_number(lst1)
    assert lst1 == [-2, 1, 4, 7, 8], "sort_number() failed"
    lst2 = [-10]
    sort_number(lst2)
    assert lst2 == [-10], "sort_number() failed"


def sort_sort_fish():
    fish_lst = [Fish("Alice", 12, 50, "Salmon", "Fresh"), Fish("Bob", 7, 32, "Catfish", "Fresh"), Fish("Charlie", 2, 100, "Goldfish", "Fresh"), Fish("Dana", 20, 80, "Shark", "Salt")]
    sort_fish(fish_lst)
    assert fish_lst == [Fish("Dana", 20, 80, "Shark", "Salt"), Fish("Alice", 12, 50, "Salmon", "Fresh"), Fish("Bob", 7, 32, "Catfish", "Fresh"), Fish("Charlie", 2, 100, "Goldfish", "Fresh")], "sort_fish() failed"
