import numpy as np

# class RegressaoLinearSimples:

#     def fit(self, x, y):
#         mean_x = np.mean(x)
#         mean_y = np.mean(y)
#         sum1 = np.sum( (x - mean_x) * (y - mean_y) )
#         sum2 = np.sum( (x - mean_x) ** 2 )
#         self.w1 = sum1 / sum2
#         self.w0 = mean_y - self.w1 * mean_x

#     def predict(self, x):
#         return self.w0 + self.w1 * x

class LinearRegressionGD(object):

    def __init__(self, eta=0.001, n_iter=20):
        self.eta = eta
        self.n_iter = n_iter

    def fit(self, X, y):
        self.w_ = np.zeros(1 + X.shape[1])
        self.cost_ = []

        for i in range(self.n_iter):
            output = self.net_input(X)
            errors = (y - output)
            self.w_[1:] += self.eta * X.T.dot(errors)
            self.w_[0] += self.eta * errors.sum()
            cost = (errors**2).sum() / 2.0
            self.cost_.append(cost)
        return self

    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict(self, X):
        return self.net_input(X)