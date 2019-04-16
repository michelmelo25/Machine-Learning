import numpy as np

class normalize:
    
    X_min = None
    X_max = None
     
    def fit(self,X):
        self.X_max = X.max()
        self.X_min = X.min()
        
    def transform(self,X):
        return (X - self.X_min) / (self.X_max - self.X_min)

class standardize :
    
    X_avg = None
    X_std = None
     
    def fit(self,X):
        self.X_avg = X.mean()
        self.X_std = X.std()
     
    def transform(self,X):
        return (X - self.X_avg) / self.X_std