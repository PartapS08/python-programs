# Set type is a collection which is unordered and unindexed. No duplicate members.
# Unordered means Element’s order doesn’t matter. When we gonna print the set the items will appear in a random order.
# Unindexed means we cannot access the items in a set by referring to an index.
# Elements are the values stored in the set. For eg. {1, John, 200} here 1, John, 200 are elements.
# Set items are enclosed in curly brackets {}.
# Set is mutable. Elements can be added, removed or changed from the set.
# Empty set is defined as var = set(). here type(var) will return <class 'set'>.
# Set datatype are set and frozenset. Their functions are set() and frozenset() respectively.

############ set() example #############

var = set()
var = {10, 'Hello', True}
print(var)
# Output:
# {True, 10, 'Hello'}

# There are many in-built functions to perform operations on set.
# For example, add(), update(), remove(), discard(), pop(), clear(), union(), intersection(), difference(), symmetric_difference() etc.
# Other operations are Membership operators (in, not in), Identity operators (is, is not) etc.

########## frozenset() example #########

# frozenset() is immutable version of set. Once the elements are assigned to frozenset, they cannot be changed.
var = frozenset({10, 'Hello', True})
print(var)
# Output:
# frozenset({True, 10, 'Hello'})

# There are many in-built functions to perform operations on frozenset.
# For example, union(), intersection(), difference(), symmetric_difference() etc.
# Other operations are Membership operators (in, not in), Identity operators (is, is not) etc.



