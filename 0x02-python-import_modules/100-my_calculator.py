#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, mul, sub, div

    if len(sys.argv[1:]) < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])

    if sys.argv[2] == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif sys.argv[2] == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif sys.argv[2] == "/":
        print("{} / {} = {}".format(a, b, div(a, b)))
    elif sys.argv[2] == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
