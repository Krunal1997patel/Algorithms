#!/usr/bin/python

import argparse


def find_max_profit(prices):
    low = prices[0]
    high = prices[1] - low

    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[j] - prices[i] > high:
                high = prices[j] - prices[i]

    return high


# print(find_max_profit([10000, 1000, 5900, 50, 5000, 10]))

if __name__ == "__main__":
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description="Find max profit from prices.")
    parser.add_argument(
        "integers", metavar="N", type=int, nargs="+", help="an integer price"
    )
    args = parser.parse_args()

    print(
        "A profit of ${profit} can be made from the stock prices {prices}.".format(
            profit=find_max_profit(args.integers), prices=args.integers
        )
    )

