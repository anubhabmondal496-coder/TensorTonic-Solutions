import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    x = np.array(x)
    p = np.array(p)
    l = len(x)
    sum = 0
    for i in range(0,l):
        sum += x[i] * p[i]

    return float(sum)