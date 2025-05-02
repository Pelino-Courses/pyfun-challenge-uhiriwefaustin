def calculate(*args, **kwargs):
    """
    Performs basic math operations (add, subtract, multiply, divide) on numbers.

    Positional arguments:
    - Any numbers (e.g. 5, 10, 2.5)

    Keyword arguments:
    - add=True        → Adds all numbers together
    - subtract=True   → Subtracts each next number from the first
    - multiply=True   → Multiplies all numbers
    - divide=True     → Divides the first number by each of the next ones

    Returns:
    - The result of the selected operation

    Example:
    >>> calculate(10, 5, add=True)
    15

    >>> calculate(10, 2, divide=True)
    5.0

    Notes:
    - Only one operation should be set to True at a time.
    - Raises error if invalid input or division by zero occurs.
    """
    if not args:
        raise ValueError(" You must provide at least one number.")

    if not all(isinstance(x, (int, float)) for x in args):
        raise TypeError("All inputs must be numbers.")

    if sum(bool(y) for y in kwargs.values()) != 1:
        raise ValueError("Please choose one operation to perform.")

    if kwargs.get("add"):
        return sum(args)

    elif kwargs.get("subtract"):
        result = args[0]
        for num in args[1:]:
            result -= num
        return result

    elif kwargs.get("multiply"):
        result = 1
        for num in args:
            result *= num
        return result

    elif kwargs.get("divide"):
        result = args[0]
        for num in args[1:]:
            if num == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result /= num
        return result

    else:
        raise ValueError("Unsupported operation. Use add, subtract, multiply, or divide.")
    # My Example
if __name__ == "__main__":
    try:
        print(calculate(10, 5, add=True))       # ➜ 15
        print(calculate(10, 2, multiply=True))  # ➜ 20
        print(calculate(10, 5, divide=True))    # ➜ 2.0
    except Exception as e:
        print("Error:", e)
