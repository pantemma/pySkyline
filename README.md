# pySkyline
Python package for computing all skylines (aka pareto fronts) of a dataset

## Skyline computation
The skyline of a multidimensional dataset are those points that are not dominated by any other point.

A point dominates another point if it is at least as good in all dimensions and better in at least one dimension, 
where "better" can be either greater than or less than depending on the problem. Furthermore, the definition of
domination can be restricted to only those points that are better in all dimensions.

Calculating the skyline of a dataset repeatedly, removing already calculated skylines, results in a skyline ranking known as rainbow ranking.
