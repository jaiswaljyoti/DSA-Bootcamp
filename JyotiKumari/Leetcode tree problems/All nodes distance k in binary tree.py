# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(parent, child, neighbors):
            if not child:
                return
            if parent:
                neighbors[parent.val].append(child.val)
                neighbors[child.val].append(parent.val)
            dfs(child, child.left, neighbors)
            dfs(child, child.right, neighbors)

        neighbors = collections.defaultdict(list)
        dfs(None, root, neighbors)
        bfs = [target.val]
        lookup = set(bfs)
        for _ in range(k):
            bfs = [nei for node in bfs
                   for nei in neighbors[node]
                   if nei not in lookup]
            lookup |= set(bfs)
        return bfs