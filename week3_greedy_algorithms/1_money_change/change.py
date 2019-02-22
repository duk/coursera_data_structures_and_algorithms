# Uses python3
import sys


def get_change(m):
    # write your code here
    num_of_tens = m // 10
    num_of_fives = (m % 10) // 5
    num_of_ones = m % 5
    return num_of_tens + num_of_fives + num_of_ones


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
