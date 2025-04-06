import grovers
import random as r
import unittest as u

global rand_nums
global rand_nums_set
global nums_duplicates
global nums_duplicates_set
global nums_no_duplicates
global nums_no_duplicates_set
empty = []

MIN_NUM = -100000
MAX_NUM = 100000

def _generate_random_num_list(min_size, max_size):
    """
    Generates a list of random size with random float values
    """
    size = r.randint(min_size, max_size)

    return [r.uniform(MIN_NUM, MAX_NUM) for _ in range(size)]

def _generate_random_num_set(min_size, max_size):
    """
    Generates a set of random size with random float values
    """
    size = r.randint(min_size, max_size)
    res = set()

    while len(res) != size:
        set.add(r.uniform(MIN_NUM, MAX_NUM))

    return res

def _insert_duplicates(min_dups, max_dups, lst):
    """
    Inserts a random number of preexisting list values into random positions in that list
    """
    dups = r.randint(min_dups, max_dups)

    for _ in dups:
        pos = r.randint(0, len(lst) - 1)
        lst.insert(pos, r.uniform(MIN_NUM, MAX_NUM))

def _get_random_elem(lst):
    """
    Gets a random element from a list
    """
    idx = r.randint(0, len(lst) - 1)

    return lst[idx]

def init_tests():
    """
    Prepares all global variables to be used by testing
    """
    global rand_nums
    global rand_nums_set
    global nums_duplicates
    global nums_duplicates_set
    global nums_no_duplicates
    global nums_no_duplicates_set

    rand_nums = _generate_random_num_list(1000, 5000)
    rand_nums_set = set(rand_nums)
    nums_no_duplicates_set = _generate_random_num_set(1000, 5000)
    nums_no_duplicates = list(nums_duplicates_set)
    nums_duplicates_set = _generate_random_num_set(1000, 5000)
    nums_duplicates = list(nums_duplicates_set)
    _insert_duplicates(nums_duplicates)

def test_found_numbers():
    """
    Looks for a number that is in the list
    """
    e = _get_random_elem(rand_nums)

    u.assertTrue(grovers.search(rand_nums, e))

def test_not_found_numbers():
    """
    Looks for a number that is not in the list
    """
    e = r.uniform(MIN_NUM, MAX_NUM)

    while e in rand_nums_set:
        e = r.uniform(MIN_NUM, MAX_NUM)

    u.assertFalse(grovers.search(rand_nums, e))

def test_empty():
    """
    Looks for something in an empty list
    """
    e = r.uniform(MIN_NUM, MAX_NUM)

    u.assertFalse(grovers.search(empty, e))

def test_found_duplicates():
    """
    Test finding an element that exists in a list with duplicates
    """
    e = _get_random_elem(nums_duplicates)

    u.assertTrue(grovers.search(nums_duplicates, e))

def test_not_found_duplicates():
    """
    Test finding an element that doesn't exist in list with duplicates
    """
    e = r.uniform(MIN_NUM, MAX_NUM)
    
    while e in nums_duplicates_set:
        e = r.uniform(MIN_NUM, MAX_NUM)

    u.assertFalse(grovers.search(nums_duplicates, e))

def test_found_unique():
    """
    Test finding an element that exists in a list without duplicates
    """
    e = _get_random_elem(nums_no_duplicates)

    u.assertTrue(grovers.search(nums_no_duplicates, e))

def test_not_found_unique():
    """
    Test finding an element that doesn't exist in list without duplicates
    """
    e = r.uniform(MIN_NUM, MAX_NUM)
    
    while e in nums_no_duplicates_set:
        e = r.uniform(MIN_NUM, MAX_NUM)

    u.assertFalse(grovers.search(nums_no_duplicates, e))

init_tests()

# TESTS WITH NUMBERS
test_empty()
test_found_numbers()
test_not_found_numbers()
test_found_duplicates()
test_not_found_duplicates()
test_found_duplicates()
test_not_found_duplicates()

# TESTS WITH OTHER OBJECTS

# TESTS SEARCHING FOR MULTIPLE ITEMS (AND GETTING ALL OF THEM BACK)