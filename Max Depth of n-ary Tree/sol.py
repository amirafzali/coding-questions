def maxDepth(self, root):
    if not root: return 0
    longest = 0
    for child in root.children: longest = max(self.maxDepth(child), longest)
    return 1 + longest