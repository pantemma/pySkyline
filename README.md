# pySkyline
Python package for computing all skylines (aka pareto fronts) of a dataset

## Skyline computation
The skyline of a multidimensional dataset are those points that are not dominated by any other point.

A point dominates another point if it is at least as good in all dimensions and better in at least one dimension, 
where "better" can be either greater than or less than depending on the problem. Furthermore, the definition of
domination can be restricted to only those points that are better in all dimensions.

Calculating the skyline of a dataset repeatedly, removing already calculated skylines, results in a skyline ranking known as rainbow ranking.

## Installation
The library is publicly available through PyPI. You can install it using pip.
```
pip install pySkyline
```

## Usage
**INPUT**

dataset (numpy array)  : *a 2d numpy array of the dataset*

dominance (string): *preferred type of dominance - strict if 'strict', normal if anything else or empty string*

objectives (array): *preferred objective for every column/dimension - 'min' for minimization, 'max' for maximization*

max_depth (int)   : *preferred number of iterations (i.e. number of skylines) - 0 for all skylines, other int for specific number of skylines*

**OUTPUT**

skylines (numpy array): *numpy array of integers corresponding to the skyline level*

**EXAMPLE**

Given a comma separated csv file containing a dataset with 4 dimensions (attributes), we want to use the normal domination function, minimize the first three attributes
and maximize the last one for all skyline levels.
```python
from pySkyline import skyline
import pandas as pd

dataset = (pd.read_csv('my_dataset.csv', sep=',', header=None)).values
skyline(dataset, 'normal', ['min', 'min', 'min', 'max'], 0)
```
The returned array from the skyline function should look like this:
```
[2 2 1 ... 3 1 2]
```
