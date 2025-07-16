# Solution for CodeChef problem "Game (Easy)".
# Computes maximal sum for each possible starting coin count.

import sys


def compute_results(arr):
    n = len(arr)
    arr_sorted = sorted(arr, reverse=True)
    prefix = [0]
    for x in arr_sorted:
        prefix.append(prefix[-1] + x)

    max_cost = 2 * n
    ans = [-10**18] * (max_cost + 1)

    for s in range(n + 1):
        base = prefix[s]
        for b in range(s + 1):
            cost = s + b
            extra = (2 * s - b - 1) * b // 2
            val = base + extra
            if val > ans[cost]:
                ans[cost] = val

    for k in range(1, max_cost + 1):
        if ans[k] < ans[k - 1]:
            ans[k] = ans[k - 1]
    return ans[1:]


def main():
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    outputs = []
    for _ in range(t):
        n = int(next(it))
        arr = [int(next(it)) for _ in range(n)]
        res = compute_results(arr)
        outputs.append(' '.join(map(str, res)))
    sys.stdout.write("\n".join(outputs)+"\n")


if __name__ == '__main__':
    main()

