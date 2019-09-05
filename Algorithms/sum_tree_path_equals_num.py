def FindPath(self, root, expectNumber):
    # write code here
        if not root:
            return []
        stack = []
        stack.append([root, [root.val]])
        ans = []
        while stack:
            root, path = stack.pop()
            if not root.left and not root.right and sum(path) == expectNumber:
                if ans == []:
                    ans.append(path)
                else:
                    for i in range(len(ans)):
                        if len(ans[i]) <= len(path) or i == len(reault)-1:
                            ans.insert(i, path)
            if root.left:
                path.append(root.left.val)
                stack.append([root.left, path])
            if root.right:
                path.append(root.right.val)
                stack.append([root.right, path])
        return ans