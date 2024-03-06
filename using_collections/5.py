'cat'                               # Yes can be put in a `dict`
(3, 1, 4, 1, 5, 9, 2)               # Yes, tuple is immutable
['a', 'b']                          # No list is mutable *
{'a': 1, 'b': 2}                    # No dict is mutable *
range(5)                            # Yes
{1, 4, 9, 16, 25}                   # No set is mutable *
3                                   # Yes
0.0                                 # Yes
frozenset({1, 4, 9, 16, 25})        # Yes