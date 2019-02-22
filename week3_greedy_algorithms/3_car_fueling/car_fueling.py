# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    # add initial start point 0

    if tank >= distance:
        return 0

    num_refills = 0
    current_refill = 0
    stops.insert(0, 0)
    stops.append(distance)
    num_stops = len(stops) - 2
    while current_refill <= num_stops:
        last_refill = current_refill
        #  and stops[current_refill + 1] - stops[last_refill] <= tank
        while current_refill <= num_stops and stops[current_refill + 1] - stops[last_refill] <= tank:
            current_refill = current_refill + 1

        if current_refill == last_refill:
            return -1
        if current_refill <= num_stops:
            num_refills = num_refills + 1

    return num_refills


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
