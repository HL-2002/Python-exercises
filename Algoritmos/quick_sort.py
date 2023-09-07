import random
import time


def main():
    # Initialize array to sort with random order of n range
    n = 10000000
    array = random.sample(range(n), n)
    # Print before sorting
    print(array)
    # Sort!!!
    start_time = time.time()
    array = quicksort(array)
    end_time = time.time() - start_time
    # Print the magnificent result of the quickest sorting algorithm out there!!!
    print(array)
    print(f"\n{end_time} seconds")


def quicksort(array):
    """ The idea is to sort the array based on a pivot.

    The pivot helps us to divide the array into 2, depending wether the values are lesser
    or greater than the pivot.

    Once divided, if the arrays have more than 1 number, they are quicksorted themselves, thus
    using recursion until the arrays are undivisible.

    At this stage the arrays are appended their sorting pivot, and then returned.
    
    This causes the previously called functions to return a sorted array each, giving us the
    whole sorted array at the end.
    """
    # Getting pivot
    pivot = random.choice(array)

    # Setting and Initializing arrays to separate values
    array1 = []
    array2 = []

    # Divide: Appending values to each array
    for x in array:
        if x < pivot:
            array1.append(x)
        elif x > pivot:
            array2.append(x)

    """ Add threading when I learn it to make it faster """
    # Recursion: Keep dividing until it isn't possible anymore
    if len(array1) > 1:
        array1 = quicksort(array1)
    if len(array2) > 1:
        array2 = quicksort(array2)

    # Unite: Append and extend array whenever it's ordered
    # Prioritizing 1st array
    if len(array1) > 0:
        array1.append(pivot)
        array1.extend(array2)
        return array1
    # Returning 2nd array if 1st is empty
    array2.insert(0, pivot)
    return array2


if __name__ == "__main__":
    main()