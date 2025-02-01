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

    ... For the rest:
    [0,0,0,1,4,5,5,5,4,9]

    So what is the root of node 3?
    It's 0. 3's parent is 1. 1's parent is 0. 0's parent is itself.

    
    And are the following sets connected? (0,3) (1,5) (7,8)
    Do 0 and 3 have the same root? Yes.
    Do 1 and 5 have the same root? No. 1's root is 0 and 5's root is itself.
    Do 7 and 8 have the same root? No. 7's root is 5 and 8's root is 4.

    And to union sets? Change the parent vertex of one of the roots. For instance:
    Union (4,8) and (5, 6, 7):
    [0,0,0,1,7,5,5,5,4,9]

    Two key functions:
    find(): finds the root by tracing through the parent vertex references.

    union(): unions two vertices, making their root nodes the same.
'''


'''
    QUICK FIND
    On paper, searching is slow because you start at the node and search for its parent. 
    Quick Find instead stores the root node in the array instead of its parent node. 
    
    The 
    trade-off is that the union operation requires an extra step: multiple vertices will 
    potentially need to be updated at once including their new parent node. This is because 
    changing a root node changes all of the downstream nodes as well

    class UnionFind:
        root[];

        UnionFind(size):
            root = [0] + size;
            for i in [0, size]:
                root[i] = i;
            
        # O(1)
        int find(x):
            return root[x];

        # O(N)
        void union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                for i in [0, root.length]:
                    if (root[i] == rootY):
                        root[i] == rootX
        
        # O(1)
        boolean connected(x, y):
            return find(x) == find(y)
'''
class QuickFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    # O(1)
    def find(self, x):
        return self.root[x]
    
    # O(N)
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            for i in range(len(self.root)):
                if self.root[i] == rootY:
                    self.root[i] = rootX

    # O(1)
    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
'''
    QUICK UNION
    Similar to quick find on the initialization. On the first pass, the value of the array 
    points to the parent node. The difference is that upon a union of (0,1,2,3) and (4,5,6), 
    only the parent node reference for 4 changes. So, the change looks like this:

    Parent node refs:  Parent & root refs:
    [0,0,0,0,4,4,4] -> [0,0,0,0,0,4,4]

    In the implementation, union only changes the root reference of y. The find method needs 
    to search the whole array. Both time complexities need to consider worst cases, which are 
    O(N) but will generally be faster.

    NOTE: quick union is generally more efficient than quick find. This is because quick union 
    is generally going to work on an array that doesn't require a full search. Quick union's 
    find function is slightly less efficient O(N) but its union function is generally better 
    and is, at worst, O(N).
'''

class QuickUnion:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x
		
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX

    def connected(self, x, y):
        return self.find(x) == self.find(y)
    

'''
    UNION BY RANK
    There's an issue with find() in Quick Union: it's potentially O(N) if a single node 
    is the root of all other nodes. Adding more nodes to this is difficult because it also 
    makes the union function O(N) as it has to iterate through the entire list. This can 
    be remedied by attempting to reduce the height of the graph. This is done by changing 
    the way that root node is chosen. Always make the root node of the taller graph the 
    root after the merge. This ensures tha the graph doesn't grow with the union.
'''
class UnionFindByRank:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
'''
    PATH COMPRESSION
    The find() function is still quite slow so another way to speed it up is to compress 
    the path from multiple connect nodes to their root. If parents nodes look like this: 
    [0,0,1,2,3]

    We know that these are all in line. all elements share a root node of 0. Find() for 
    node 4 still requires we traverse every node though. It would be better if we flatten 
    the array and represent them by their root nodes:
    [0,0,0,0,0]

    To do this, you use recursion in the find() function and, while search for the element, 
    you set the new roots.
'''

class UnionFindPathCompression:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        if x == self.root[x]:
            return x
        
        # updates to the root based on what's returned 
        # from find down the graph
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootX = self.root[x]
        rootY = self.root[y]

        if rootX != rootY:
            self.root[rootY] = rootX

    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
'''
    UNION BY RANK + FIND BY PATH COMPRESSION
    They both work on the assumption that the value of the array is the root.
'''

# UnionFind class
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        # Use a rank array to record the height of each vertex, i.e., the "rank" of each vertex.
        # The initial "rank" of each vertex is 1, because each of them is
        # a standalone vertex with no connection to other vertices.
        self.rank = [1] * size

    # The find function here is the same as that in the disjoint set with path compression.
    def find(self, x):
        if x == self.root[x]:
            return x
	# Some ranks may become obsolete so they are not updated
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    # The union function with union by rank
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)
