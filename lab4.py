from enum import Enum, auto
from lib230 import record


class WaterType(Enum):
    FRESH = auto()
    BRACKISH = auto()
    SALT = auto()


@record
class Fish:
    name: str
    weight_kg: float = 0
    age_days: int = 0
    species: str = 'unknown'
    water_type: WaterType = WaterType.FRESH


def get_sum(lst):
    """Sums up the floats in a list
    >>> get_sum([1.1, 2.2, 3.3, 4.4])
    11.0
    >>> get_sum([4.567])
    4.567
    >>> get_sum([])
    0.0
    """
    pass  # replace with your code


def only_non_negative_sum(lst):
    """Sums up only the non-negative floats in a list
    >>> only_non_negative_sum([1.1, -2.2, 3.3, -4.4])
    4.4
    >>> only_non_negative_sum([0.0])
    0.0
    >>> only_non_negative_sum([-1.7, -2.45, -3.1, -4.7])
    0.0
    """
    pass  # replace with your code


def copy_even(lst):
    """Makes a copy of the given list, but only with those even numbers
    >>> copy_even([1,2,3,4,5,6,7,8])
    [2,4,6,8]
    >>> copy_even([-10, 0])
    [-10, 0]
    """
    pass  # replace with your code


def copy_start_with_a(lst):
    """Makes a copy of the given list, but only with strings that start with a/A
    >>> copy_start_with_a(['Apricot', 'Banana', 'Allison', 'a cookie'])
    ['Apricot', 'Allison', 'a cookie']
    >>> copy_start_with_a(['', ' ', 'Amy'])
    ['Amy']
    """
    pass  # replace with your code


def copy_reverse(lst):
    """Makes a reverse copy of the given list, returns the copy
    >>> copy_reverse([1.1, 2.2, 3.3, 4.4])
    [4.4, 3.3, 2.2, 1.1]
    >>> copy_reverse([4.567])
    [4.567]
    >>> copy_reverse([])
    []
    """
    pass  # replace with your code


def reverse(lst):
    """Reverses the given list in place, returns nothing
    """
    pass  # replace with your code


def cartesian_product(lst1, lst2):
    """Returns a list of cartesian products of the given lists
    >>> cartesian_product([1.1, 2.2], [3.3, 4.4])
    [3.63, 9.68]
    """
    pass  # replace with your code


def sort_number(lst):
    """Sorts the given list in ascending order in place
    """
    pass  # replace with your code


def sort_fish(lst):
    """Sorts Fish in the given list by weight in descending order in place
    >>> sort_fish([Fish('Alice', 12, 50, 'Salmon', WaterType.FRESH), Fish('Bob', 7, 32, 'Catfish', WaterType.FRESH), Fish('Charlie', 2, 100, 'Goldfish', WaterType.FRESH), Fish('Dana', 20, 80, 'Shark', WaterType.SALT)])
    [Fish('Dana', 20, 80, 'Shark', WaterType.SALT), Fish('Alice', 12, 50, 'Salmon', WaterType.FRESH), Fish('Bob', 7, 32, 'Catfish', WaterType.FRESH), Fish('Charlie', 2, 100, 'Goldfish', WaterType.FRESH)]
    """
    pass  # replace with your code
