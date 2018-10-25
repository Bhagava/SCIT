import numpy as np
import matplotlib.pyplot as plt
lamda_values=[2,10,5]
for lamda in lamda_values:
    print(lamda)
    s = np.random.poisson(lamda,1000)
    count, bins, ignored = plt.hist(s, 14, density=True)
    plt.show()