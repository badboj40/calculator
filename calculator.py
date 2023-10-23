import sys

class Calculator:
    """A simple calculator that supports registers and basic integer operations"""

    def __init__(self) -> None:
        self.operations = ["add", "subtract", "multiply"]
        self.registers = dict() # {register: [(operation, value), ...]}

    def perform_operation(self, x: int, operation: str, y: int) -> int:
        """Perform an operation on two values"""
        if operation == "add":
            return x + y
        elif operation == "subtract":
            return x - y
        elif operation == "multiply":
            return x * y

    def evaluate(self, x) -> int:
        """Recursively evaluate x, which may be a register or a numeric value"""
        # Base case - x has a numeric value
        if isinstance(x, int) or isinstance(x, str) and x.isdigit():
            return int(x)

        # Base case - x is an undefined register, evaluate to 0
        if x not in self.registers:
            return 0    

        # Recursive case - x is a register that should be evaluated
        result = 0
        for operation, value in self.registers[x]:
            value = self.evaluate(value)
            result = self.perform_operation(result, operation, value)
        return result

    def update_register(self, register: str, operation: str, value: str) -> None:
        """Update the value of a register"""
        # Check for invalid input
        if not register.isidentifier():
            print(f"Invalid register name '{register}'. Register names must be alphanumeric.")
            return
        if operation not in self.operations:
            print(f"Invalid operation '{operation}'. Valid operations are {', '.join(self.operations)}.")
            return
        if not value.isdigit() and not value.isidentifier():
            print(f"Invalid value '{value}'. Values must be integers or register names.")
            return

        # Update the register
        if not register in self.registers:
            self.registers[register] = []
        self.registers[register].append((operation, value))

        # If the new register definition is cyclic, undo the update
        try:
            result = self.evaluate(register)
        except RecursionError:
            print(f"Cyclic register definitions are not allowed.")
            self.registers[register].pop()
    
    def execute(self, expression: str) -> None:
        """Execute an expression"""
        ex = expression.lower().split()

        # quit
        if len(ex) == 1 and ex[0] == "quit":
            sys.exit()
        
        # print <register>
        elif len(ex) == 2 and ex[0] == "print":
            register = ex[1]
            if register.isidentifier():
                print(self.evaluate(register))
            else:
                print(f"Invalid register name '{register}'. Register names must be alphanumeric.")

        # <register> <operation> <value>
        elif len(ex) == 3:
            register, operation, value = ex
            self.update_register(register, operation, value)

        # Invalid expression
        else:
            print(f"Invalid expression '{expression}'.")
            print("Valid expressions are 'print <register>' and '<register> <operation> <value>'.")


def main() -> None:
    calc = Calculator()
    # If a filename is provided, read the file and evaluate each line
    if sys.argv[1:]:
        filename = sys.argv[1]
        with open(filename, "r") as f:
            indata = f.readlines()
        for expression in indata:
            calc.execute(expression.strip().lower())
        return

    # Otherwise, read from stdin
    while True:
        try:
            expression = input()
        except EOFError:
            break
        calc.execute(expression)


if __name__ == '__main__':
    main()