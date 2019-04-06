"""
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""


def sum_div_by(n):
    return sum(f * n for f in range(1, 999//n + 1))


if __name__ == '__main__':
    print(sum(n for n in range(1, 1000)
              if n % 5 == 0 or n % 3 == 0))

    print(sum_div_by(3) + sum_div_by(5) - sum_div_by(15))
