def serialize(self, root):
    res = []
    if not root: return ""
    def buildRes(root):
        if not root: 
            res.append('None,')
            return
        res.append(str(root.val)+',')
        buildRes(root.left)
        buildRes(root.right)
        
    buildRes(root)
    return "".join(res)[:-1]
    

def deserialize(self, data):
    if not data: return None
    res = data.split(",")

    def build():
        if res[0] == 'None':
            res.pop(0)
            return None
        
        node = TreeNode(int(res.pop(0)))
        node.left = build()
        node.right = build()
        
        return node
        
    return build()