
"""
There are n cities numbered from 1 to n. You are given an array edges of size n-1, where edges[i] = [ui, vi] represents a bidirectional edge between cities ui and vi. There exists a unique path between each pair of cities. In other words, the cities form a tree.

A subtree is a subset of cities where every city is reachable from every other city in the subset, where the path between each pair passes through only the cities from the subset. Two subtrees are different if there is a city in one subtree that is not present in the other.

For each d from 1 to n-1, find the number of subtrees in which the maximum distance between any two cities in the subtree is equal to d.

Return an array of size n-1 where the dth element (1-indexed) is the number of subtrees in which the maximum distance between any two cities is equal to d.

Notice that the distance between the two cities is the number of edges in the path between them.

Input: n = 4, edges = [[1,2],[2,3],[2,4]]
Output: [3,4,0]
Explanation:
The subtrees with subsets {1,2}, {2,3} and {2,4} have a max distance of 1.
The subtrees with subsets {1,2,3}, {1,2,4}, {2,3,4} and {1,2,3,4} have a max distance of 2.
No subtree has two nodes where the max distance between them is 3.

Example 2:

Input: n = 2, edges = [[1,2]]
Output: [1]

Example 3:

Input: n = 3, edges = [[1,2],[2,3]]
Output: [2,1]
"""

from collections import Counter

def flatten(S):
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])
    


edges1 = [[1,2],[2,3],[2,4]]


def leetcode_result(n, edges):
    edgemap = generate_edgemap(edges)
    subtrees = generate_subtrees(edgemap)
    distances = [get_tree_distance(s) for s in subtrees]
    distance_counts = Counter(distances)
    result = [0] * (n - 1)
    for k,v in distance_counts:
        result[k] = v
    return result


def generate_edgemap(edges):
    n = len(edges)
    edgemap = {i:[] for i in range(1, n + 2)}
    for edge in edges:
        edgemap[edge[0]].append(edge[1]);
        edgemap[edge[1]].append(edge[0]);
    return edgemap

# For convenience
e1map = generate_edgemap(edges1)

def get_distance_counts(edgemap):
    subtrees = generate_subtrees(edgemap)
    
    pass


def generate_subtrees(edgemap):
    return flatten([edgemap] + _generate_subtrees(edgemap))


def _generate_subtrees(edgemap, subtree_set = None):
    if subtree_set is None:
        subtree_set = set()
    edge_nodes = get_all_edge_nodes(edgemap)
    subtrees = []
    for node in edge_nodes:
        subtree = cull_node(edgemap, node)
        subtree_nodes = id_tree(subtree)
        if subtree_nodes not in subtree_set:
            subtrees.append(subtree)
            subtree_set.add(subtree_nodes)
    subsubs = [_generate_subtrees(subtree, subtree_set) for subtree in subtrees]
    result = flatten(subtrees + subsubs)
    result = [r for r in result if len(r) > 1]
    return result
                    
def id_tree(tree):
    return ''.join((str(v) for v in sorted(tree.keys())))


def cull_edge_node(edgemap):
    node = get_edge_node(edgemap)
    return cull_node(node)


def cull_node(edgemap, node):
    reduced_values = [[x for x in v if x != node] for v in edgemap.values()]
    reduced_edgemap = dict(zip(edgemap.keys(), reduced_values))
    reduced_edgemap.pop(node)
    return reduced_edgemap  



def get_tree_distance(edgemap):
    """Finds max distance of given tree"""
    edge_node = get_edge_node(edgemap)
    return _distance(edge_node, edgemap)
    

def get_all_edge_nodes(edgemap):
    return [k for k,v in edgemap.items() if len(v) == 1]
    
def get_edge_node(edgemap):
    for node, children in edgemap.items():
        if len(children) == 1:
            edge_node = node
            return edge_node
    
    
def _distance(node, edgemap, depth=0):
    """Finds max distance starting from node node"""
    children = edgemap[node]
    reduced_edgemap = cull_node(edgemap, node)
    try:
        branch_distances = [_distance(child, reduced_edgemap, depth) for child in children]
        depth = max(1 + branch_distances, two_largest(branch_distances))
    except ValueError:
        depth = 0
    return depth
    
def two_largest(int_list):
    m1 = max(int_list)
    int_list = int_list.copy()
    m2 = max(int_list.remove(m1))
    return m1, m2

