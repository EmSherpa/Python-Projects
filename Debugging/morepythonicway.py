import math
import re
from enum import Enum, auto

double = float

# ---- Base class ----
class Operators:
    def calc(self, a: double, b: double = 0.0) -> double:
        raise NotImplementedError


# ---- Concrete operators ----
class Addition(Operators):
    def calc(self, a, b):
        return a + b


class Subtraction(Operators):
    def calc(self, a, b):
        return a - b


class Multiplication(Operators):
    def calc(self, a, b):
        return a * b


class Division(Operators):
    def calc(self, a, b):
        if b == 0:
            return math.nan if a == 0 else math.inf
        return a / b


class Log(Operators):
    def calc(self, a, b=0):
        if a < 0:
            return math.nan
        if a == 0:
            return -math.inf
        return math.log10(a)


class Sqrt(Operators):
    def calc(self, a, b=0):
        if a < 0:
            return math.nan
        return math.sqrt(a)


# ---- Enum (keeps C++ flavor) ----
class Op(Enum):
    ADD = auto()
    SUB = auto()
    MUL = auto()
    DIV = auto()
    LOG = auto()
    SQRT = auto()


# ---- Operator objects ----
OPS = {
    Op.ADD: Addition(),
    Op.SUB: Subtraction(),
    Op.MUL: Multiplication(),
    Op.DIV: Division(),
    Op.LOG: Log(),
    Op.SQRT: Sqrt(),
}

# ---- Symbol lookup ----
SYMBOLS = {
    "+": Op.ADD,
    "-": Op.SUB,
    "*": Op.MUL,
    "/": Op.DIV,
    "log": Op.LOG,
    "sqrt": Op.SQRT,
}


# ---- Input parser (handles 5+5, 5 + 5, sqrt9, etc.) ----
def parse(expr: str):
    expr = expr.strip().lower()

    # unary ops
    if expr.startswith("log") or expr.startswith("sqrt"):
        op = SYMBOLS[re.match(r"[a-z]+", expr).group()]
        num = float(re.findall(r"[-+]?\d*\.?\d+", expr)[0])
        return op, num, 0.0

    # binary ops
    match = re.match(r"\s*([-+]?\d*\.?\d+)\s*([+\-*/])\s*([-+]?\d*\.?\d+)\s*", expr)
    if not match:
        raise ValueError("Invalid expression")

    a, sym, b = match.groups()
    return SYMBOLS[sym], float(a), float(b)


# ---- Control (same role as C++ control class) ----
class Control:
    def run(self, op: Op, a: double, b: double):
        return OPS[op].calc(a, b)


# ---- Main ----
def main():
    ctrl = Control()
    print("Enter expressions like 5+5, 5 * 5, log10, sqrt9")
    print("Type 'exit' to quit")

    while True:
        line = input("> ")
        if line == "exit":
            break

        try:
            op, a, b = parse(line)
            result = ctrl.run(op, a, b)
            print("Result:", result)
        except Exception:
            print("Error: Invalid input")


if __name__ == "__main__":
    main()