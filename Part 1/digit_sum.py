def digit_sum(n):
    """
    Problem 4 — Recursive Digit Sum
    Write a recursive function digit_sum(n) that:
    ● takes a non-negative integer n
    ● returns the sum of its digits
    ● must use recursion, not loops
    Example:
    digit_sum(5029) → 16
    """
    if n < 10:
        return n
    else:
        return (n%10) + digit_sum(n//10)


def main():
    n = 5029
    print(digit_sum(n))


main()