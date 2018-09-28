import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spo

def f(X):
    Y = (X - 1.5)**2 + 0.5
    print("X = {}, Y= {}".format(X,Y))
    return Y

def test_run():
    Xguess = 2.0
    min_result = spo.minimize(f, Xguess, method='SLSQP' ,options={'disp':True})
    print('Min Result found at: X = {}, Y = {}'.format(min_result.x,min_result.fun))

    Xplot = np.linspace(0.5,2.5,21)
    Yplot = f(Xplot)
    plt.plot(Xplot,Yplot)
    plt.plot(min_result.x,min_result.fun,'ro')
    plt.show()

if __name__ == '__main__':
    test_run()