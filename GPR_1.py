import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


import scipy.stats as stats

data=pd.read_csv('GPR.csv',usecols=['Distance','DeltaC'])
data.head()

x=np.array(data['Distance']).reshape(-1,1)
y=np.array(data['DeltaC'])

plt.plot(x, y, label=r"$Distance Vs Delta C$", linestyle="dotted")
plt.legend()
plt.xlabel("$Distance$")
plt.ylabel("$Delta C$")
_ = plt.title("data")

rng = np.random.RandomState(1)
training_indices = rng.choice(np.arange(y.size), size=6, replace=False)
x_train, y_train = x[training_indices], y[training_indices]

from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF

kernel = 1 * RBF(length_scale=1.0, length_scale_bounds=(1e-2, 1e2))
gaussian_process = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=9)
gaussian_process.fit(x_train, y_train)
gaussian_process.kernel_

mean_prediction, std_prediction = gaussian_process.predict(x, return_std=True)


plt.plot(x, y, label=r"$data$", linestyle="dotted")
plt.scatter(x_train, y_train, label="Observations")
plt.plot(x, mean_prediction, label="Mean prediction")
plt.fill_between(
    x.ravel(),
    mean_prediction - 1.96 * std_prediction,
    mean_prediction + 1.96 * std_prediction,
    alpha=0.5,
    label=r"95% confidence interval",
)
plt.legend()
plt.xlabel("$Distance$")
plt.ylabel("$Delta C$")
_ = plt.title("Noiseless Gaussian process regression")

# std_prediction

noise_std = 0.0015
y_train_noisy = y_train + rng.normal(loc=0.0, scale=noise_std, size=y_train.shape)

gaussian_process = GaussianProcessRegressor(kernel=kernel, alpha=noise_std ** 2, n_restarts_optimizer=9)
gaussian_process.fit(x_train, y_train_noisy)
mean_prediction, std_prediction = gaussian_process.predict(x, return_std=True)

# defining a class for prediction
def prediction(a):
    mean_prediction, std_prediction = gaussian_process.predict([a], return_std=True)
    y = mean_prediction
    return y
 
mean_prediction

plt.plot(x, y, label=r"$Distance Vs Delta C$", linestyle="dotted")
plt.errorbar(
    x_train,
    y_train_noisy,
    noise_std,
    linestyle="None",
    color="tab:red",
    marker=".",
    markersize=10,
    label="Observations",
)
plt.plot(x, mean_prediction, label="Mean prediction")
plt.fill_between(
    x.ravel(),
    mean_prediction - 1.96 * std_prediction,
    mean_prediction + 1.96 * std_prediction,
    color="tab:purple",
    alpha=0.5,
    label=r"95% confidence interval",
)
# # plt.legend().print
# plt.xlabel("$Distance$")
# plt.ylabel("$DeltaC$")
# _ = plt.title("Gaussian process regression on a noisy dataset")

mean_prediction

# std_prediction
# def print_output(s):
#     w = print(prediction[s])