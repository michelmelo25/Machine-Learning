import numpy as np

class normalize:
    
    vals = {}
    
    def fit(X):
        vals.clear()
        n_cols = X.shape[1]
        for i in range(n_cols):
            vals.update({i: {'min': np.min(X[:,i]),'max': np.max(X[:,i])}})
        return vals
            
    def transform(X):
        n_cols = X.shape[1]
        for i in range(n_cols):
            X[:,i] = (X[:,i] - vals[i]['min'])/(vals[i]['max'] - vals[i]['min'])
        return X

class standardize :
    
    vals = {}
    
    def fit(X):
        vals.clear()
        n_cols= X.shape[1]
        for i in range(n_cols):
            vals.update({i: {'mean': np.mean(X[:,i]),'std': np.std(X[:,i])}})
        return vals
    
    def transform(X):
        n_cols = X.shape[1]
        for i in range(n_cols):
            X[:,i] = (X[:,i] - vals[i]['mean'])/(vals[i]['std'])
        return X