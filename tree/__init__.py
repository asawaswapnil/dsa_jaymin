from typing import Dict


class TreeNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val


class BinaryTree:
    def __init__(self, root: TreeNode, metadata: Dict[str, str] = None):
        self.root = root
        self.metadata = metadata


# ----- Utilities -----

def _print(val):
    print(val, end=' ')


# ----- Sample Trees -----

# Metadata Keys
VISUAL_STRUCTURE = "structure"
IN_ORDER = "in_order"
PRE_ORDER = "pre_order"
POST_ORDER = "post_order"
LEVEL_ORDER = "level_order"
LEVEL_ORDER_GROUPED = "level_order_grouped"


class SampleTrees:

    @staticmethod
    def full_binary_tree():
        _root = TreeNode(1)
        _root.left = TreeNode(2)
        _root.right = TreeNode(3)
        _root.left.left = TreeNode(4)
        _root.left.right = TreeNode(5)
        _root.right.left = TreeNode(6)
        _root.right.right = TreeNode(7)

        _structure = """
                1\n
              /    \\\n
            2        3\n
          /   \     /  \\\n
        4      5   6     7
        """

        _metadata = {
            VISUAL_STRUCTURE: _structure,
            IN_ORDER: "4 2 5 1 6 3 7",
            PRE_ORDER: "1 2 4 5 3 6 7",
            POST_ORDER: "4 5 2 6 7 3 1",
            LEVEL_ORDER: "1 2 3 4 5 6 7",
            LEVEL_ORDER_GROUPED: "[[1], [2, 3], [4, 5, 6, 7]]"
        }

        return BinaryTree(root=_root, metadata=_metadata)
