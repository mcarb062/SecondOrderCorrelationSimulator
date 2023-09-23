# -*- coding: utf-8 -*-
"""
reated on Tue Jun  6 13:14:06 2023

@author: celestecarbonell
"""
import numpy as np
import matplotlib.pyplot as plt

plt.close(all)

def second_order_correlation(x, max_tau=None):
    """Calculate the second-order correlation function for a set of values x"""
    n = len(x)
    if max_tau is None:
        max_tau = n - 1
    g2 = np.zeros(2*max_tau + 1)
    tau_values = range(-max_tau, max_tau + 1)

    for idx, tau in enumerate(tau_values):
        if tau < 0:
            g2[idx] = np.mean(x[:tau] * x[-tau:])
        elif tau == 0:
            g2[idx] = np.mean(x * x)
        else:
            g2[idx] = np.mean(x[:-tau] * x[tau:])

    g2 /= np.mean(x) ** 2
    return g2, tau_values

# Parameters
tau_char = 100  # Characteristic lifetime for exponential decay
p = 0.05  # Probability to get excited

# Generate photon stream
x = np.zeros(10000)
for i in range(10000):
    # Check if source gets excited
    if np.random.rand() < p:
        # If excited, generate photon based on exponential decay probability
        if np.random.rand() < 1 - np.exp(-i/tau_char):
            x[i] = 1

g2, tau_values = second_order_correlation(x, max_tau=80)

# Since g^2(0) for an ideal single-photon source should be 0, set the value at tau=0 to 0
g2[tau_values.index(0)] = 0

# Plotting
plt.plot(tau_values, g2)
plt.xlabel('Time delay')
plt.ylabel('g^2')
plt.title('Second-Order Correlation Function with Exponential Decay and Randomness')
plt.show()
