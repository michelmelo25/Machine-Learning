import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix

class metricas:

    def accuracy(_self,y_test,y_pred):
        return np.sum(y_test == y_pred) / y_pred.shape[0]
    
    def precision(_self,y_test,pred):
        mc = confusion_matrix(y_test, pred)
        dfmc = pd.DataFrame(mc)
        TP = mc.diagonal()
        FP = []
        for i in range(dfmc.shape[0]):
            FP.append(dfmc[i].sum() - mc.diagonal()[i])
        FP = np.array(FP)
        return TP.sum()/(TP.sum()+FP.sum())
    
    def recall(_self,y_test,pred):
        mc = confusion_matrix(y_test, pred)
        dfmc = pd.DataFrame(mc)
        TP = mc.diagonal()
        FN = []
        for i in range(dfmc.shape[0]):
            FN.append(dfmc.values[i].sum() - mc.diagonal()[i])
        FN = np.array(FN)
        return TP.sum()/(TP.sum()+FN.sum())
    
    def f1_measure(_self,y_test,pred):
        presc = _self.precision(y_test,pred)
        reca = _self.recall(y_test,pred)
        
        return 2*(presc*reca)/(presc+reca)
        