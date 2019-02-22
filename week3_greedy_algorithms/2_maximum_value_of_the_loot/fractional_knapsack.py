# Uses python3
import sys
from operator import itemgetter


def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    # evaluate value per weight
    # add highest value per weight item till either the bag is full or you use up all the item
    # repeat the same thing to the next highest value per weight item.
    # continue till the bag is full
    value_per_weight = []
    i = 0
    for weight in weights:
        value_per_weight.append({'total_weight': weight, 'value_per_weight': values[i]/weight})
        i = i + 1

    new_list = sorted(value_per_weight, key=itemgetter('value_per_weight'), reverse=True)
    available_weight = capacity

    for item in new_list:
        if available_weight != 0 and item['total_weight'] <= available_weight:
            # add everything to the sack
            value = value + item['value_per_weight'] * item['total_weight']
            available_weight = available_weight - item['total_weight']
        elif available_weight != 0 and item['total_weight'] > available_weight:
            value = value + item['value_per_weight'] * available_weight
            available_weight = 0

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
