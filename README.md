# Calculator

A simple calculator that can add, subtract and multiply values in a set of registers.

## Running the code

First clone the repository and navigate to the root folder of the project.

Running the program with file input:

```bash
python3 calculator.py path/to/file.txt
```

Running the program in interactive mode, where the input is entered line by line:

```bash
python3 calculator.py
```

Exit the program by typing `quit`.

When running the code on windows, replace `python3` with `python`. This assumes that python is installed and is added to path.

## Rules / Assumptions

* Only integer values are supported.
* Cyclic dependencies are not allowed. This means that a register cannot be defined in terms of itself.
* The default value of an undefined register is 0.
* Input is case insensitive.
* Register names must be alphanumeric, which I define as follows:
  * Register names can contain letters, numbers and underscores.
  * Register names cannot start with a number.
  * Register names must contain at least one letter or underscore.
* Lazy evaluation is used for register values. This means that the value of a register is only evaluated when it is printed.

## Syntax

The input is a set of commands, one per line, with the following syntax

```xml
<register> <operation> <value>
print <register>
quit
```

* `<register>` is the name of a register, e.g. A, B, C, etc.
* `<operation>` is either add, subtract or multiply.
* `<value>` is an integer value.

When the program is run in interactive mode, the input is entered line by line. When the program is run with file input, the input is read from the file.

In interactive mode, the program will exit when the user types `quit`. In file input mode, the program will exit when it reaches the end of the file or if the `quit` command is used.

## Examples

A few examples to highlight the syntax and functionality of the calculator. There are text files with example inputs in the `examples` folder.

To run the examples, use for example:

```bash
python3 calculator.py examples/1.txt
```

### Example 1 - Simple addition and subtraction

Input:

```bash
A add 2
A add 3
print A
B add 5
B subtract 2
print B
A add 1
print A
quit 
```

Output:

```bash
5
3
6
```

### Example 2 - lazy evaluation

Input:

```bash
result add revenue
result subtract costs
revenue add 200
costs add salaries
salaries add 20
salaries multiply 5
costs add 10
print result
QUIT 
```

Output:

```bash
90
```

### Example 3 - Cycle detection and default values

Input:

```bash
Print B
A add B
B add 2
print B
B add A
print B
```

Output:

```bash
0
2
Cyclic register definitions are not allowed.
2
```

### Example 4 - Invalid input and logging

Input:

```bash
foo bar
12 add 2
b power a
e add 2.718
quit
something after the program has quit
```

Output:

```bash
Invalid expression 'foo bar'.
Valid expressions are 'print <register>' and '<register> <operation> <value>'.
Invalid register name '12'. Register names must be alphanumeric.
Invalid operation 'power'. Valid operations are add, subtract, multiply.
Invalid value '2.718'. Values must be integers or register names.
```
