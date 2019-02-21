# Uses python3

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

def calc_fib_last_digit_iterative(n):
    if n <= 0:
        return n

    if n > 1:
        fib_list = [0, 1]
        for x in range(2, n + 1):
            fib_list.append((fib_list[x - 2] + fib_list[x - 1]) % 10)
        return fib_list[n]


if __name__ == '__main__':
    input_n = int(input())
    n = int(input_n)
    print(calc_fib_last_digit_iterative(n))
