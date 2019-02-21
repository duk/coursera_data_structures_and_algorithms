# Uses python3
def calc_fib(n):
    if n <= 1:
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)


def calc_fib_iterative(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        fib_list = [0, 1]
        for x in range(2, n + 1):
            fib_list.append(fib_list[x - 2] + fib_list[x - 1])
        return fib_list[n]


if __name__ == '__main__':
    input1 = int(input())
    print(calc_fib_iterative(input1))
