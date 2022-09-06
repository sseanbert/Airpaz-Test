import numpy as np

def func(waktuProsesOrder):
    a = np.array(waktuProsesOrder)
    a[1] += 2
    b = np.cumsum(a)
    c = np.sum(b)
    print(c)

func([5,4,3])
