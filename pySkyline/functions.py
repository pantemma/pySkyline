import numpy as np
from numba import njit

@njit(fastmath=True)
def dominates_normal(a, b):
    dominates = False
    for i in range(len(a)):
        if a[i] is None or b[i] is None:
            continue
        if a[i] > b[i]:
            return False
        if a[i] < b[i]:
            dominates = True
    return dominates

@njit(fastmath=True)
def dominates_strict(a, b):
    for i in range(len(a)):
        if a[i] is None or b[i] is None:
            continue
        if a[i] >= b[i]:
            return False
    return True

@njit(fastmath=True)
def window_dominates_current_normal(window, current):
    for i in range(len(window)):
        if dominates_normal(window[i], current):
            return True
    return False

@njit(fastmath=True)
def current_dominates_window_normal(window, current):
    dominated_indexes = []
    for i in range(len(window)):
        if dominates_normal(current, window[i]):
            dominated_indexes.append(i)
    return dominated_indexes

@njit(fastmath=True)
def window_dominates_current_strict(window, current):
    for i in range(len(window)):
        if dominates_strict(window[i], current):
            return True
    return False

@njit(fastmath=True)
def current_dominates_window_strict(window, current):
    dominated_indexes = []
    for i in range(len(window)):
        if dominates_strict(current, window[i]):
            dominated_indexes.append(i)
    return dominated_indexes

"""
bnl: the classic block nested loops algorithm
---------------------------------------------
INPUT
dataset (numpy array): a 2d numpy array of the dataset
dominance (string): type of dominance - strict if 'strict', normal if anything else or empty string

OUTPUT
pareto_front (numpy array): a 1d numpy array of zeros and ones representing the corresponding paretofront
"""
def bnl(dataset, dominance):
    window_dominates_current = window_dominates_current_normal
    current_dominates_window = current_dominates_window_normal
    if dominance == 'strict':
        window_dominates_current = window_dominates_current_strict
        current_dominates_window = current_dominates_window_strict

    window_indexes = np.array([0])
    window_values = dataset[window_indexes]
    dataset_length = len(dataset)
    for i in range(1, dataset_length):
        current_value = dataset[i]
        if window_dominates_current(window_values, current_value):
            continue
        dominated_window_indexes = current_dominates_window(window_values, current_value)
        if dominated_window_indexes:
            window_indexes = np.delete(window_indexes, dominated_window_indexes)
        window_indexes = np.append(window_indexes, i)
        window_values = dataset[window_indexes]

    pareto_front = np.zeros(dataset_length, dtype=int)
    pareto_front[window_indexes] = 1
    return pareto_front

"""
skyline: the main function to call
----------------------------------
INPUT
dataset (numpy array)  : a 2d numpy array of the dataset
dominance (string): preferred type of dominance - strict if 'strict', normal if anything else or empty string
objectives (array): preferred objective for every column/dimension - 'min' for minimization, 'max' for maximization
max_depth (int)   : preferred number of iterations (i.e. number of skylines) - 0 for all skylines, other int for specific number of skylines

OUTPUT
skylines (numpy array): numpy array of integers corresponding to the skyline level
"""
def skyline(dataset, dominance, objectives, max_depth):
    max_dimensions = [i for i in range(dataset.shape[1]) if objectives[i] == 'max']
    for dimension in max_dimensions:
        dataset[:, dimension] = -dataset[:, dimension]

    skylines = np.zeros(dataset.shape[0], dtype=np.int_)
    current_skyline = 1

    if max_depth == 0:
        while 0 in skylines:
            zeros = np.where(skylines == 0)
            skylines[zeros] = bnl(dataset[zeros], dominance)*current_skyline
            current_skyline += 1
    else:
        while max_depth > current_skyline:
            zeros = np.where(skylines == 0)
            try:
                skylines[zeros] = bnl(dataset[zeros], dominance)*current_skyline
            except IndexError:
                break
            current_skyline += 1

    return skylines
