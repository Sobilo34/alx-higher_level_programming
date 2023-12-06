#!/usr/bin/python3

def weight_average(lst=[]):
    sum_wt = sum(val * wt for val, wt in my_list)
    total_wt = sum(wt for _, wt in my_list)

    return (sum_wt / total_wt if total_wt != 0 else 0)
