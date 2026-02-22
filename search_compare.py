import time
import random


def get_me_random_list(n):
    """Generate list of n elements in random order
    
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def sequential_search(a_list, item):
    """Sequential search with timing"""
    start_time = time.time()
    
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1

    end_time = time.time()
    return found, (end_time - start_time)


def ordered_sequential_search(a_list, item):
    """Ordered sequential search with timing"""
    start_time = time.time()
    
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1

    end_time = time.time()
    return found, (end_time - start_time)


def binary_search_iterative(a_list, item):
    """Binary search iterative with timing"""
    start_time = time.time()
    
    first = 0
    last = len(a_list) - 1
    found = False
    
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    end_time = time.time()
    return found, (end_time - start_time)

    
def binary_search_recursive(a_list, item):
    """Binary search recursive with timing"""
    start_time = time.time()
    
    def _helper(lst):
        if len(lst) == 0:
            return False
        else:
            midpoint = len(lst) // 2
            if lst[midpoint] == item:
                return True
            else:
                if item < lst[midpoint]:
                    return _helper(lst[:midpoint])
                else:
                    return _helper(lst[midpoint + 1:])
    
    found = _helper(a_list)
    end_time = time.time()
    return found, (end_time - start_time)


if __name__ == "__main__":
    """Main entry point"""
    
    # List sizes to test
    list_sizes = [500, 1000, 5000]
    
    # Target element (worst case - not in list)
    target = 99999999
    
    # Run benchmarks for each list size
    for size in list_sizes:
        print(f"List Size: {size} elements")
        
        # Test Sequential Search
        total_time = 0
        for i in range(100):
            mylist = get_me_random_list(size)
            found, time_spent = sequential_search(mylist, target)
            total_time += time_spent
        time_taken = total_time / 100
        print(f"Sequential Search took {time_taken:10.7f} seconds to run, on average")
        
        # Test Ordered Sequential Search
        total_time = 0
        for i in range(100):
            mylist = get_me_random_list(size)
            mylist = sorted(mylist)  
            found, time_spent = ordered_sequential_search(mylist, target)
            total_time += time_spent
        time_taken = total_time / 100
        print(f"Ordered Sequential Search took {time_taken:10.7f} seconds to run, on average")
        
        # Test Binary Search Iterative
        total_time = 0
        for i in range(100):
            mylist = get_me_random_list(size)
            mylist = sorted(mylist)  
            found, time_spent = binary_search_iterative(mylist, target)
            total_time += time_spent
        time_taken = total_time / 100
        print(f"Binary Search Iterative took {time_taken:10.7f} seconds to run, on average")
        
        # Test Binary Search Recursive
        total_time = 0
        for i in range(100):
            mylist = get_me_random_list(size)
            mylist = sorted(mylist)  
            found, time_spent = binary_search_recursive(mylist, target)
            total_time += time_spent
        time_taken = total_time / 100
        print(f"Binary Search Recursive took {time_taken:10.7f} seconds to run, on average")