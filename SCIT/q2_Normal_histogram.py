import numpy as np
import matplotlib.pyplot as plt
mean_values=[2,10,5]
standard_values=[1,5,3]
for i  in range(0,len(mean_values)):
    mean=mean_values[i]
    sigma=standard_values[i]
    s = np.random.normal(mean,sigma,1000)
    count, bins, ignored = plt.hist(s, 14, normed=True)
    plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
    np.exp( - (bins - mean)**2 / (2 * sigma**2) ),
    linewidth=4, color='b')
    plt.show()