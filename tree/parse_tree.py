import re
from operator import add, sub, mul, truediv

from tree import TreeNode


OPERATIONS = {
    '+': add,
    '-': sub,
    "*": mul,
    "/": truediv
}

# The regex below tokenizes the expression string using '+', '-', '*', '/', '(', ')' as delimiters to support
# multi-digit numbers. The outermost parenthesis in regex maintains groups which preserves the delimiters as well in
# the output array of tokens after splitting the expression string
SPLIT_PATTERN = re.compile("(\(|\)|\+|-|\*|\/)")


class ParseTree:
    """
    An implementation of a Parse Tree to evaluate simple mathematical expressions
    """

    def __init__(self, expr: str):
        self._expr: str = expr
        self._root: TreeNode = TreeNode()
        self._construct_tree()

    def _construct_tree(self):
        """
        Construct the Parse Tree from given expression string
        """
        curr = self._root
        stack = [curr]
        for token in SPLIT_PATTERN.split(self._expr):
            token = token.strip()
            if token == "":
                continue
            elif token == "(":
                stack.append(curr)
                curr.left = TreeNode()
                curr = curr.left
            elif token in OPERATIONS.keys():
                curr.val = token
                stack.append(curr)
                curr.right = TreeNode()
                curr = curr.right
            elif token.isdigit():
                curr.val = int(token)
                curr = stack.pop()
            elif token == ")":
                curr = stack.pop()
            else:
                # the flow should not end up in this else block
                self._root = TreeNode()
                raise Exception("Cannot construct parse tree; expression is invalid!")
        if stack:
            self._root = TreeNode()
            raise Exception("Cannot construct parse tree; expression is invalid!")

    def evaluate(self) -> int:
        """
        Evaluate the expression represented by the Parse Tree using a recursive postorder traversal
        """
        def _postorder(node: TreeNode) -> int:
            if node:
                result_left, result_right = _postorder(node.left), _postorder(node.right)
                if result_left and result_right:
                    func = OPERATIONS[node.val]
                    return func(result_left, result_right)
                return node.val

        return _postorder(self._root)

    def get_expression(self) -> str:
        """
        Reconstruct the original expression from the Parse Tree using a recursive inorder traversal
        """
        def _inorder(node: TreeNode) -> str:
            _str_buffer = []
            if node:
                _str_buffer += ["("]
                _str_buffer += [_inorder(node.left)]
                _str_buffer += [str(node.val)]
                _str_buffer += [_inorder(node.right)]
                _str_buffer += [")"]
            return "".join(_str_buffer)

        return _inorder(self._root)


if __name__ == '__main__':
    expression = "((4 + 5) * 5)"
    print("\nExpression: {}".format(expression))
    print("\nCreating parse tree...")
    parse_tree = ParseTree(expression)
    print("\nEvaluation result: {}".format(parse_tree.evaluate()))
    print("\nReconstructing expression from parse tree")
    print(parse_tree.get_expression())
