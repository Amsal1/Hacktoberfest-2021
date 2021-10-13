def grid_traveler(m, n, memo={}):
    key = f'{m},{n}'
    if key in memo:
        return memo[key]

    elif m == 0 or n == 0:
        return 0

    elif m == 1 and n == 1:
        return 1

    else:
        memo[key] = grid_traveler(m - 1, n, memo) + grid_traveler(m, n - 1, memo)
        return memo[key]
