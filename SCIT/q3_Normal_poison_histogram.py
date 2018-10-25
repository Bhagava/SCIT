import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial
from random import sample
lamda_values=[2,10,4]
mean_values=[2,10,5]
sigma_values=[1,5,3]
def calculating_poison(lamda,x):
    poison = np.exp(-lamda)*np.power(lamda, x)/factorial(x)
    return poison
def calculating_normal(mean,sigma,x):
   normal= 1/(sigma * np.sqrt(2 * np.pi))*np.exp( - (x - mean)**2 / (2 * sigma**2) )
   return normal
for lamda in lamda_values:
    a=[]
    #print("poisson distribution")
    s=np.random.poisson(lamda,1000)
    for _ in range(100):
        a.append(np.mean(sample(list(s),100)))
    count, x, ignored = plt.hist(a, 14, density=True)
    plt.plot(x,calculating_poison(lamda,x),linewidth=4, color='b')
    plt.show()
for i in range(0,len(mean_values)):
    b=[]
    #print("Normal distribution")
    mean=mean_values[i]
    sigma=sigma_values[i]
    s = np.random.normal(mean,sigma,1000)
    for _ in range(100):
        b.append(np.mean(sample(list(s),100)))
    count, x, ignored = plt.hist(b[i], 14, normed=True)
    plt.plot(x,calculating_normal(mean,sigma,x),linewidth=4, color='b')
    plt.show()
    