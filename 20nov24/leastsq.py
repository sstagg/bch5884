#!/usr/bin/env python3

import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import leastsq

def modeleq(x,t):
	return x[0]+x[1]*np.exp(x[2]*t)

def residuals(coeffs,t,y):
	return modeleq(coeffs,t)-y

def gen_data(t,a,b,c, noise=0, n_outliers=0, random_state=0):
	y=a+b*np.exp(t*c)
	rnd=np.random.RandomState(random_state)
	error=noise*rnd.randn(t.size)
	outliers=rnd.randint(0,t.size,n_outliers)
	error[outliers]*=10
	return y+error
	
a=0.5
b=2.0
c=-1

t_min=0
t_max=10
n_points=100

t_train=np.linspace(t_min,t_max,n_points)
y_train=gen_data(t_train,a,b,c,noise=0.1,n_outliers=10)

x0 = np.array([1.0, 1.0, 0.0])
res_lsq=leastsq(residuals, x0, args=(t_train,y_train))
print (res_lsq)

t_test= np.linspace(t_min,t_max,n_points*10)
y_true= gen_data(t_test, a,b,c)
y_lsq= gen_data(t_test, *res_lsq[0])
resid=y_train-gen_data(t_train, *res_lsq[0])

plt.plot(t_train,y_train,'o')
plt.plot(t_test, y_true, 'k', linewidth=2, label='true')
plt.plot(t_test,y_lsq, label='fitted')
plt.plot(t_train, resid,'ro')
plt.xlabel('t')
plt.ylabel('y')
plt.show()
