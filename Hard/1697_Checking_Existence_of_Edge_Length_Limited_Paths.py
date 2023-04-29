"""
2023-04-29

1697. Checking Existence of Edge Length Limited Paths
Hard, Acceptance Rate 60.1%

An undirected graph of n nodes is defined by edge_list, where edge_list[i] = [ui, vi, disi] denotes an edge
between nodes ui and vi with distance disi. Note that there may be multiple edges between two nodes.

Given an array queries, where queries[j] = [pj, qj, limitj], your task is to determine for each queries[j]
whether there is a path between pj and qj such that each edge on the path has a distance strictly less
than limitj .

Return a boolean array answer, where answer.length == queries.length and the jth value of answer is true
if there is a path for queries[j] is true, and false otherwise.


Example 1:
Input: n = 3, edge_list = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], queries = [[0,1,2],[0,2,5]]
Output: [false,true]
Explanation: The above figure shows the given graph. Note that there are two overlapping edges between 0
and 1 with distances 2 and 16.
For the first query, between 0 and 1 there is no path where each distance is less than 2, thus we return
false for this query.
For the second query, there is a path (0 -> 1 -> 2) of two edges with distances less than 5, thus we return
true for this query.

Example 2:
Input: n = 5, edge_list = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]], queries = [[0,4,14],[1,4,13]]
Output: [true,false]
Exaplanation: The above figure shows the given graph.


Constraints:
2 <= n <= 105
1 <= edge_list.length, queries.length <= 105
edge_list[i].length == 3
queries[j].length == 3
0 <= ui, vi, pj, qj <= n - 1
ui != vi
pj != qj
1 <= disi, limitj <= 109
There may be multiple edges between two nodes.

"""


class UnionFind:
    def __init__(self, size: int):
        self.group = [0] * size
        self.rank = [0] * size
        for i in range(size):
            self.group[i] = i

    def find(self, node: int) -> int:
        if self.group[node] != node:
            self.group[node] = self.find(self.group[node])
        return self.group[node]

    def join(self, node1: int, node2: int):
        group1 = self.find(node1)
        group2 = self.find(node2)

        # node1 and node2 already belong to same group.
        if group1 == group2:
            return

        if self.rank[group1] > self.rank[group2]:
            self.group[group2] = group1
        elif self.rank[group1] < self.rank[group2]:
            self.group[group1] = group2
        else:
            self.group[group1] = group2
            self.rank[group2] += 1

    def are_connected(self, node1: int, node2: int) -> bool:
        return self.find(node1) == self.find(node2)


class Solution:
    def distance_limited_paths_exist(self, n: int, edge_list: list[list[int]], queries: list[list[int]]) -> list[bool]:
        uf = UnionFind(n)
        queries_count = len(queries)
        answer = [False] * queries_count

        # Store original indices with all queries.
        queries_with_index = [[] for _ in range(queries_count)]
        for i in range(queries_count):
            queries_with_index[i] = queries[i]
            queries_with_index[i].append(i)

        # Sort all edges in increasing order of their edge weights.
        edge_list.sort(key=lambda x: x[2])
        # Sort all queries in increasing order of the limit of edge allowed.
        queries_with_index.sort(key=lambda x: x[2])

        edges_index = 0

        # Iterate on each query one by one.
        for [p, q, limit, query_original_index] in queries_with_index:
            # We can attach all edges which satisfy the limit given by the query.
            while edges_index < len(edge_list) and edge_list[edges_index][2] < limit:
                node1 = edge_list[edges_index][0]
                node2 = edge_list[edges_index][1]
                uf.join(node1, node2)
                edges_index += 1

            # If both nodes belong to the same component, it means we can reach them.
            answer[query_original_index] = uf.are_connected(p, q)

        return answer


assert Solution().distance_limited_paths_exist(
    n=3, edge_list=[[0, 1, 2], [1, 2, 4], [2, 0, 8], [1, 0, 16]], queries=[[0, 1, 2], [0, 2, 5]]
) == [False, True]
assert Solution().distance_limited_paths_exist(
    n=5, edge_list=[[0, 1, 10], [1, 2, 5], [2, 3, 9], [3, 4, 13]], queries=[[0, 4, 14], [1, 4, 13]]
) == [True, False]
print("OK assertion!")
