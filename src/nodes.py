from dataclasses import dataclass


@dataclass
class NumberNode:
    value: float

    def __repr__(self) -> str:
        return f"{self.value}"


@dataclass
class AddNode:
    node_a: NumberNode
    node_b: NumberNode

    def __repr__(self) -> str:
        return f"({self.node_a} + {self.node_b})"


@dataclass
class SubtractNode:
    node_a: NumberNode
    node_b: NumberNode

    def __repr__(self) -> str:
        return f"({self.node_a} - {self.node_b})"


@dataclass
class MultiplyNode:
    node_a: NumberNode
    node_b: NumberNode

    def __repr__(self) -> str:
        return f"({self.node_a} * {self.node_b})"


@dataclass
class DivideNode:
    node_a: NumberNode
    node_b: NumberNode

    def __repr__(self) -> str:
        return f"({self.node_a} / {self.node_b})"


@dataclass
class PowerNode:
    node_a: NumberNode
    node_b: NumberNode

    def __repr__(self) -> str:
        return f"({self.node_a} ** {self.node_b})"


@dataclass
class PlusNode:
    node: NumberNode

    def __repr__(self) -> str:
        return f"+({self.node})"


@dataclass
class MinusNode:
    node: NumberNode

    def __repr__(self) -> str:
        return f"-({self.node})"
