from src.nodes import *
from src.values import Number


class Interpreter:
    def visit(self, node):
        method_name = f"visit_{type(node).__name__}"
        visitor = getattr(self, method_name, self.visit_default)
        return visitor(node)

    def visit_default(self, node):
        raise Exception(f"No visitor for {type(node).__name__}")

    def visit_NumberNode(self, node: NumberNode):
        return node.value

    def visit_AddNode(self, node: AddNode):
        return Number(self.visit(node.node_a) + self.visit(node.node_b))

    def visit_SubtractNode(self, node: SubtractNode):
        return Number(self.visit(node.node_a) - self.visit(node.node_b))

    def visit_MultiplyNode(self, node: MultiplyNode):
        return Number(self.visit(node.node_a) * self.visit(node.node_b))

    def visit_DivideNode(self, node: DivideNode):
        try:
            res = Number(self.visit(node.node_a) / self.visit(node.node_b))
            return res
        except ZeroDivisionError:
            raise Exception("Run time math error")

    def visit_PlusNode(self, node: PlusNode):
        return Number(self.visit(node.node))

    def visit_MinusNode(self, node: MinusNode):
        return Number(self.visit(node.node).value * -1)
