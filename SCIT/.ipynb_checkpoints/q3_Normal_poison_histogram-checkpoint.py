import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial
from random import sample
lamda_values=[2,10,4]
mean_values=[2,10,5]
sigma_values=[1,5,3]
for k in range(100):
    for lamda in lamda_values:
        a=[]
        #print("poisson distribution")
        s=np.random.poisson(lamda,1000)
        for _ in range(100):
            a.append(np.mean(sample(list(s),100)))
        count, x, ignored = plt.hist(a, 14, density=True)
        plt.show()
    for i in range(0,len(mean_values)):
        b=[]
        #print("Normal distribution")
        mean=mean_values[i]
        sigma=sigma_values[i]
        s = np.random.normal(mean,sigma,1000)
        for jk in range(100):
            b.append(np.mean(sample(list(s),100)))
        count, x, ignored = plt.hist(b[i], 14, normed=True)
        plt.show()
