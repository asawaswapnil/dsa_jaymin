from typing import Callable
from collections import deque

from tree import SampleTrees, TreeNode, _print
from tree import VISUAL_STRUCTURE, IN_ORDER, PRE_ORDER, POST_ORDER, LEVEL_ORDER, LEVEL_ORDER_GROUPED


def in_order_recursive(node: TreeNode, func: Callable) -> None:
    """
    Simple recursive inorder traversal – left -> node -> right
    """
    if node:
        in_order_recursive(node.left, func)
        func(node.val)
        in_order_recursive(node.right, func)


def in_order_iterative(node: TreeNode, func: Callable) -> None:
    """
    Iterative inorder traversal using stack
    - start with empty stack and curr as node
    - keep pushing to stack until leftmost node found
    - once curr is None, leftmost reached
    - pop off the stack and visit
    - set curr as the right node of the most recent popped node and repeat
    """
    stack, curr = [], node
    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
            continue
        _node = stack.pop()
        func(_node.val)
        curr = _node.right


def pre_order_recursive(node: TreeNode, func: Callable) -> None:
    """
    Simple recursive preorder traversal – node -> left -> right
    """
    if node:
        func(node.val)
        pre_order_recursive(node.left, func)
        pre_order_recursive(node.right, func)


def pre_order_iterative(node: TreeNode, func: Callable) -> None:
    """
    Iterative preorder traversal using stack
    - start with stack as [node]
    - while stack is not empty, pop from stack
    - if last popped node (curr) is not None, visit the curr
    - push the right child of curr to the stack followed by the left child of curr
    """
    stack = [node]
    while stack:
        curr = stack.pop()
        if curr:
            func(curr.val)
            stack.extend([curr.right, curr.left])


def post_order_recursive(node: TreeNode, func: Callable) -> None:
    """
    Simple recursive postorder traversal – left -> right -> node
    """
    if node:
        post_order_recursive(node.left, func)
        post_order_recursive(node.right, func)
        func(node.val)


def post_order_iterative_using_accumulator_stack(node: TreeNode, func: Callable) -> None:
    """
    Iterative preorder traversal using two stacks, one for traversal and one as an accumulator
    - start traversal stack as [node] and an empty accumulator stack
    - while stack is not empty, pop from stack
    - if last popped (curr) is not None, add its value to accumulator stack (but do not visit yet)
    - push left child of curr to stack followed by right child of curr
    - the order of pushing depending on traversal type and how its implemented
    - once the traversal stack if empty, the accumulator should have all node's value in a  postorder fashion
    - start popping from accumulator stack and visit
    """
    stack, accumulator = [node], []
    while stack:
        curr = stack.pop()
        if curr:
            accumulator.append(curr.val)
            stack.extend([curr.left, curr.right])
    while accumulator:
        func(accumulator.pop())


def post_order_iterative_using_accumulator_queue(node: TreeNode, func: Callable) -> None:
    """
    Iterative preorder traversal using a traversal stack and accumulator queue
    - the idea here is the same, but we use deque as the accumulator buffer
    - while storing values of curr in accumulator, append from left
    - while visiting values from accumulator, pop from right
    """
    stack, accumulator = [node], deque([])
    while stack:
        curr = stack.pop()
        if curr:
            accumulator.appendleft(curr.val)
            stack.extend([curr.left, curr.right])
    while accumulator:
        func(accumulator.popleft())


def post_order_iterative_using_single_stack(node: TreeNode, func: Callable) -> None:
    """
    Iterative preorder traversal using a single stack
    """
    raise NotImplementedError()


def level_order(node: TreeNode, func: Callable) -> None:
    """
    Iterative levelorder traversal using a queue
    """
    queue = deque([node])
    while queue:
        curr = queue.popleft()
        if curr:
            func(curr.val)
            queue.extend([curr.left, curr.right])


def level_order_grouped(node: TreeNode, func: Callable) -> None:
    """
    Iterative grouped levelorder traversal using a queue
    Slight change to the levelorder traversal above, before visiting nodes from next level, visit all nodes from
    the current level first. Maintain a level-wise grouping and if there is a node found in current level, add the
    grouping to the results
    """
    queue = deque([node])
    grouped_values = []
    while queue:
        level, size = [], len(queue)
        for _ in range(size):
            curr = queue.popleft()
            if curr:
                level.append(curr.val)
                queue.extend([curr.left, curr.right])
        if level:
            grouped_values.append(level)
    func(grouped_values)


if __name__ == '__main__':
    tree = SampleTrees.full_binary_tree()
    root, metadata = tree._root, tree.metadata

    print("\nVisual Structure")
    print(metadata.get(VISUAL_STRUCTURE))

    print("\nTraversals")
    print("{}: {}".format(IN_ORDER, metadata.get(IN_ORDER)))
    print("{}: {}".format(PRE_ORDER, metadata.get(PRE_ORDER)))
    print("{}: {}".format(POST_ORDER, metadata.get(POST_ORDER)))
    print("{}: {}".format(LEVEL_ORDER, metadata.get(LEVEL_ORDER)))
    print("{}: {}".format(LEVEL_ORDER_GROUPED, metadata.get(LEVEL_ORDER_GROUPED)))

    print("\n=> Inorder Recursive")
    in_order_recursive(node=root, func=_print)

    print("\n\n=> Inorder Iterative")
    in_order_iterative(node=root, func=_print)

    print("\n\n=> Preorder Recursive")
    pre_order_recursive(node=root, func=_print)

    print("\n\n=> Preorder Iterative")
    pre_order_iterative(node=root, func=_print)

    print("\n\n=> Postorder Recursive")
    post_order_recursive(node=root, func=_print)

    print("\n\n=> Postorder Iterative with Accumulator Stack")
    post_order_iterative_using_accumulator_stack(node=root, func=_print)

    print("\n\n=> Postorder Iterative with Accumulator Queue")
    post_order_iterative_using_accumulator_queue(node=root, func=_print)

    print("\n\n=> Levelorder")
    level_order(node=root, func=_print)

    print("\n\n=> Levelorder Grouped")
    level_order_grouped(node=root, func=_print)
