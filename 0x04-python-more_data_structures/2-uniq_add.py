#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = list(set(my_list))
    result = 0

    for i in range(len(uniq_list)):
        result += uniq_list[i]
    return result
