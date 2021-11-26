# **전위 순회(pre-order)**


def preorder_traverese(t):
    if t:
        visit(t)
        preorder_traverese(t.left)
        preorder_traverese(t.right)


# **중위 순회(in-order)**
def inorder_traverese(t):
    if t:
        inorder_traverese(t.left)
        visit(t)
        inorder_traverese(t.right)


# **후위 순회(post-order)**
def postorder_traverese(t):
    if t:
        postorder_traverese(t.left)
        postorder_traverese(t.right)
        visit(t)
