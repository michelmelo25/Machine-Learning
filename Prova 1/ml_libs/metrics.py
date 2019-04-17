import numpy as np

class metrics:

    def acuracy(y,y_pred):
        return np.sum(y == y_pred)/y_pred.shape[0]