import numpy as np

def sample_var_std(x: list) -> dict:
    n = len(x)
    if n <= 1:
        return {"variance": 0.0, "std_dev": 0.0}
    sum = 0
    for i in range(0,n):
        sum += x[i]
    avg = sum / n
    sum2 = 0
    for i in range(0,n):
        sum2 += pow((x[i] - avg),2)

    varx = sum2 / (n-1)
    std_ = pow(varx,0.5)

    return {"variance" : varx,"standard_deviation" : std_}