import functions
import input_data
import timeit

input_data_set = input_data.Set_2_4

def execution_grahamscan():
    result = functions.grahamscan(input_data_set)
    print("<<<<<Метод Грэхема>>>>>", *result, sep="\n")

def execution_grahamscan_with_quicksort():
    result = functions.grahamscan_with_mergesort(input_data_set)
    print("<<<<<Метод Грэхема с сортировкой слиянием>>>>>", *result, sep="\n")

def execution_jarvismarch():
    result = functions.jarvismarch(input_data_set)
    print("<<<<<Метод Джарвиса>>>>>", *result, sep="\n")

execution_time1 = timeit.timeit(execution_grahamscan, number=1)
functions.minimal_corvex_hull(input_data_set, functions.grahamscan(input_data_set)) #   Графический интерфейс

execution_time2 = timeit.timeit(execution_grahamscan_with_quicksort, number=1)
functions.minimal_corvex_hull(input_data_set, functions.grahamscan_with_mergesort(input_data_set))

execution_time3 = timeit.timeit(execution_jarvismarch, number=1)
functions.minimal_corvex_hull(input_data_set, functions.jarvismarch(input_data_set))

print("Время выполнения методом Грэхема: {} секунд".format(execution_time1))
print("Время выполнения методом Грэхема с сортировкой слиянием: {} секунд".format(execution_time2))
print("Время выполнения методом Джарвиса: {} секунд".format(execution_time3))


