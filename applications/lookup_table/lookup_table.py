import math, random

results = dict()
powers = dict()
factorials = dict()

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

def slowfun_v1(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """

    if (x, y) in results:
        return results[(x, y)]

    if (x, y) in powers:
        power = powers[(x, y)]
    else:
        power = math.pow(x, y)

    if power in factorials:
        factorial = factorials[power]
    else:
        factorial = math.factorial(power)

    result = factorial // (x + y)
    result %= 982451653

    results[(x, y)] = result

    return result

# because there are only 36 combinations, compute them ahead of time
precomputed_values = dict()

for x in range(2, 14):

    for y in range(3, 6):

        result = math.pow(x, y)
        result = math.factorial(result)
        result //= (x + y)
        result %= 982451653

        precomputed_values[(x, y)] = result

    print("stored all possibilities for x = ", x)

def slowfun(x, y):

    return precomputed_values[(x, y)]
    

# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')