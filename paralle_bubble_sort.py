# Alternate Threading Version
import time
import random
import threading
import itertools

# start time counter to calculate runtime
start_time = time.time()

# create a threading lock
lock = threading.Lock()


# normal bubble sort function
def bubble_sort(lst):
    # acquire a lock for thread
    lock.acquire()

    # get length of list
    n = len(lst)

    # perform bubble sort
    for i in range(n):
        swap = False
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swap = True
        if not swap:
            break

    # release the lock after calculation
    lock.release()


# create parallel bubble sort function
# this function uses normal bubble sort function

def Parallel_bubble_sort(lst):
    # get biggest element in the list
    biggest_item = max(lst)

    # set number of threads
    # as per the number of cores
    # each core can run 2 threads ideally
    no_threads = 4

    # create sublists as per number of threads
    lists = [[] for _ in range(no_threads)]

    # we use a number to divide the list
    # into class intervals for each sublist

    split_factor = biggest_item // no_threads

    # split list into sublists
    # as per no of threads
    for j in range(1, len(lists)):
        for i in lst:
            if i <= (split_factor * j):
                lists[j - 1].append(i)

                # remove the element from list
                # after adding to sublist
                # to prevent duplication
                lst = [x for x in lst if x != i]
        # include the remaining elements in list
        # in the last sublist
        lists[-1] = lst

    # start all threads for each sublist
    active_threads = []
    for list_item in lists:
        t = threading.Thread(target=bubble_sort, args=(list_item,))
        t.start()
        active_threads.append(t)

    # stop all active threads
    for thread in active_threads:
        thread.join()

    # merge all lists
    # into final list
    final_lst = itertools.chain(*lists)
    final_lst = list(final_lst)
    print(final_lst)

