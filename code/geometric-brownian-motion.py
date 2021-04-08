import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import timeit

plt.style.use('seaborn')
sns.set_style("darkgrid")

# So    :   initial stock price
# dt    :   time increment (a day)
# T     :   length of the prediction time horizon
# N     :   number of time points in the prediction time horizon -> T/dt
# t     :   array for time points in the prediction time horizon [1, 2, 3, .. , N]
# mu    :   mean of historical daily returns
# sigma :   standard deviation of historical daily returns
# b     :   array for brownian increments
# W     :   array for brownian path
# sims  :   number of simulations

sims = 10000

s0 = 10
T = 100
dt = 1
N = T / dt
t = np.arange(1, int(N) + 1)
mu = 0
sigma = 0.009

# Dictionary Implementation
np.random.seed(123)

start = timeit.default_timer()

b = {str(i): np.random.normal(0, np.sqrt(dt), int(N)) for i in range(sims)}
W = {str(i): np.cumsum(b[str(i)]) for i in range(sims)}
drift = (mu - 0.5 * sigma**2) * t
diffusion = {str(i): sigma * W[str(i)] for i in range(sims)}

S = np.array([s0 * np.exp(drift + diffusion[str(i)]) for i in range(sims)]) 
S = np.hstack((np.array([[s0] for i in range(sims)]), S))

end = timeit.default_timer()
print("Time {:,.3f} seconds".format(end - start))

fig, ax = plt.subplots(figsize=(8,5))
for i in range(sims):
    ax.plot(S[i, :], label="_nolabel_")
ax.plot(S[0, :], color="k", label="Actual Path")
ax.set(title="Geometric Brownian Motion", xlabel="days", ylabel="Stock Price, £")
plt.legend()
plt.show()


# Array Implementation
np.random.seed(123)

start = timeit.default_timer()

b = np.random.normal(0, np.sqrt(dt), (sims, int(N)))
W = np.cumsum(b, axis=1)
drift = (mu - 0.5 * sigma**2) * t
diffusion = sigma * W

S = np.array(s0 * np.exp(drift + diffusion))
S = np.vstack((np.array([[s0] * sims]), S.T))

end = timeit.default_timer()
print("Time {:,.3f} seconds".format(end - start))

fig, ax = plt.subplots(figsize=(8,5))
ax.plot(S, alpha=0.5, label="_nolabel_")
ax.plot(S[:, 0], color="k", label="Actual Path")
ax.set(title="Geometric Brownian Motion", xlabel="days", ylabel="Stock Price, £")
plt.legend()
plt.show()

fig, ax = plt.subplots(figsize=(8,5))
ax.hist(S[-1, :], bins = 20)
ax.set(title="Geometric Brownian Motion", xlabel="days", ylabel="Stock Price, £")
plt.show()


# Drift

def brownianMotion(sims, T, dt, seed):

    '''
    int sims    : number of simulations
    int T       : number of time points to predict
    float dt    : time increment
    return b, W : b - Brownian increment, W - Brownian path
    '''

    np.random.seed(seed)
    N = int(T / dt)
    b = np.random.normal(0, 1, (sims, N))*np.sqrt(dt)
    W = np.cumsum(b, axis=1)

    return b, W

b, W = brownianMotion(1, 252, 1, 123)

fig, ax = plt.subplots(figsize=(16,5), ncols=2, nrows=1)
ax[0].plot(b.T)
ax[0].set(title="Brownian Increment", xlabel="days", ylabel="Random Variate")
ax[1].plot(W.T)
ax[1].set(title="Brownian Path", xlabel="days", ylabel="Random Variate")
plt.show()


def GBM(sims, T, dt, s0, mu, sigma, seed):

    '''
    int sims    : number of simulations
    int T       : number of time points to predict
    float dt    : time increment
    float s0    : initial stock price
    float mu    : drift coefficient
    float sigma : diffusion coefficient
    return S    : stock price simulations
    '''

    # Calculate the simulation range
    N = int(T / dt)
    t = np.arange(1, N + 1)

    # Calculate Brownian random paths
    b, W = brownianMotion(sims, T, dt, seed)

    # Calculate drift and diffusion
    drift = (mu - 0.5 * sigma**2) * t
    diffusion = sigma * W

    # Simulate stock price
    S = np.array(s0 * np.exp(drift + diffusion))
    S = np.vstack((np.array([[s0] * sims]), S.T))

    return S

S = GBM(sims=1, T=252, dt=1, s0=10, mu=0, sigma=0.01, seed=10)

fig, ax = plt.subplots(figsize=(16,5), ncols=2, nrows=1)
for mu in [-0.001, 0, 0.001]:
    S = GBM(sims=1, T=252, dt=1, s0=10, mu=mu, sigma=0.01, seed=10)
    ax[0].plot(S, label=f"$\mu = ${mu}")
    ax[0].set(title="Drift Coefficient Sensitivity", xlabel="days", ylabel="Stock Price, £")
ax[0].legend()
for sigma in [0.01, 0.05, 0.1]:
    S = GBM(sims=1, T=252, dt=1, s0=10, mu=0, sigma=sigma, seed=10)
    ax[1].plot(S, label=f"$\sigma = ${sigma}")
ax[1].set(title="Diffusion Coefficient Sensitivity", xlabel="days", ylabel="Stock Price, £")
plt.legend()
plt.show()
