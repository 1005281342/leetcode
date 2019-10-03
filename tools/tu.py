from typing import List
from collections import defaultdict


def arr2undirected_graph(arr: List[List]):
    """
    二维数组变无向图
    :param arr:
    :return:
    """
    dd = defaultdict(list)
    for k, v in arr:
        dd[k].append(v)
    return dd


def arr2directed_graph(arr: List[List]):
    """
    二维数组变有向图
    :param arr:
    :return:
    """
    dd = defaultdict(list)
    for k, v in arr:
        dd[k].append(v)
        dd[v].append(k)
    return dd
