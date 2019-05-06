import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix

class metricas:

    def accuracy(_self,y_test,y_pred):
        return np.sum(y_test == y_pred) / y_pred.shape[0]
    
    def precision(_self,y_test,pred):
        mc = confusion_matrix(y_test, pred)
        pond = np.unique(y_test, return_counts=True)[1]
        pred = []
        for i in range(mc.shape[0]):
                pred.append(pond[i] * mc.diagonal()[i]/mc[:,i].sum())
        return np.sum(pred)/pond.sum()
    
    def recall(_self,y_test,pred):
        mc = confusion_matrix(y_test, pred)
        pond = np.unique(y_test, return_counts=True)[1]
        pred = []
        for i in range(mc.shape[0]):
            pred.append(pond[i] * mc.diagonal()[i]/mc[i].sum())
        return np.sum(pred)/pond.sum()
    
    def f1_measure(_self,y_test,pred):
        presc = _self.precision(y_test,pred)
        reca = _self.recall(y_test,pred)
        return 2*(presc*reca)/(presc+reca)
        