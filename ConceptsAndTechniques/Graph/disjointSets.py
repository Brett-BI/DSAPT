# index = vertex
# value = parent vertex
# [0,1,2,3,4,5,6,7,8,9]

# das union: (0,1), (0,2) (1,3) (4,8) (5,6) (5,7) THEN (0,3) (1,5) (7,8)
'''
    For (0, 1) union:
    [0,1,2,3,4,5,6,7,8,9] -> [0,0,2,3,4,5,6,7,8,9]

    For (0,2) union:
    [0,0,2,3,4,5,6,7,8,9] -> [0,0,0,3,4,5,6,7,8,9]

    For (1,3) union:
    [0,0,0,3,4,5,6,7,8,9] -> [0,0,0,1,4,5,6,7,8,9]

    So what is the root of node 3?
    It's 0. 3's parent is 1. 1's parent is 0. 0's parent is itself.
'''