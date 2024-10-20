import functions
import input_data
import timeit

input_data_set = input_data.Set_2_4


def execution_grahamscan():
    result1 = functions.grahamscan(input_data_set)
    print("<<<<<Метод Грэхема>>>>>", *result1, sep="\n")


def execution_jarvismarch():
    result2 = functions.jarvismarch(input_data_set)
    print("<<<<<Метод Джарвиса>>>>>", *result2, sep="\n")

execution_time1 = timeit.timeit(execution_grahamscan, number=1)
execution_time2 = timeit.timeit(execution_jarvismarch, number=1)
print("Время выполнения методом Грэхема: {} секунд".format(execution_time1))
print("Время выполнения методом Джарвиса: {} секунд".format(execution_time2))

