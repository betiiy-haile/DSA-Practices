# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.visited = set()
        self.bfs(root)

    def find(self, target: int) -> bool:
        return target in self.visited
    
    def bfs(self, node):

        queue = deque()
        queue.append(node)
        node.val = 0

        while queue:
            curr = queue.popleft()
            self.visited.add(curr.val)
            if curr.left:
                curr.left.val = curr.val * 2 + 1
                queue.append(curr.left)
            if curr.right:
                curr.right.val = curr.val * 2 + 2
                queue.append(curr.right)

    
# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)