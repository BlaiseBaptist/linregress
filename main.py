import numpy as np
import matplotlib.pyplot as plt


class LinearRegression:
    def __init__(self, xs, ys):

        if xs is None:
            xs = np.zeros(10)

        if ys is None:
            ys = np.zeros(10)

        self.xs = xs
        self.ys = ys
        self.slope = 0
        self.inter = 10

    def loss(self, slope=None, inter=None):
        if slope is None:
            slope = self.slope
        if inter is None:
            inter = self.inter
        return np.sum((slope * self.xs + inter - self.ys) ** 2)

    def fit(self, delta=2 ** -10, gamma=1):
        for i in range(1000000):
            sgrad = (self.loss(self.slope + delta) - self.loss(self.slope - delta)) / (2 * delta)
            igrad = (self.loss(inter = self.inter + delta) - self.loss(inter = self.inter - delta)) / (2 * delta)
            slope = self.slope - gamma * sgrad
            inter = self.inter - gamma * igrad
            if self.loss(slope,inter) < self.loss():
                self.slope = slope
                print('slope', slope)
                self.inter = inter
                print('inter',inter)
            else:
                gamma /= 2



    def predict(self, xs):
        pass


def main():
    adelie_bill_len_mm = np.loadtxt("adelie.csv", delimiter=',', skiprows=1, usecols=0)
    adelie_flipper_len_mm = np.loadtxt("adelie.csv", delimiter=',', skiprows=1, usecols=1)
    lr = LinearRegression(adelie_bill_len_mm, adelie_flipper_len_mm)
    loss_xs = np.linspace(0, 10, 10000)
    loss_ys = np.array([lr.loss(a) for a in loss_xs])
    plt.plot(loss_xs, loss_ys)
    lr.fit()
    plt.show()
    print("slope", lr.slope)
    print("intercept", lr.inter)
    print('done')


if __name__ == '__main__':
    main()
