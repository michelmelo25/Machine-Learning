import numpy as np

class KNN():
    
    dist = None
    
    def __init__(_self, dist='euclidean'):
        _self.dist = dist
    
    def obter_idx_kNN(_self,X, linha, k):
        distan = _self.cal_dist(X, linha)
        idx_sort = np.argsort(distan)
        return idx_sort[0:k]
    
    def classifica(_self,X, y, linha, k):
        idx_kNN = _self.obter_idx_kNN(X, linha, k=k)
        count = np.bincount(np.int64(y[idx_kNN]))
        return np.argmax(count)

    def regressao(_self,X, y, linha, k):
        idx_kNN = _self.obter_idx_kNN(X, linha, k=k)
        return np.mean(y[idx_kNN])
    
    def dist_euclidiana(_self,X, linha):
        X_ = (X - linha) ** 2
        return np.sqrt( np.float64(np.sum(X_, axis=1)) )
    
    def manhattan_distance(_self,X, linha):
        X_ = np.abs(X - linha)
        return np.sum(X_, axis=1)
    
    def chebyshev_distance(_self,X, linha):
        X_ = np.max(np.abs(X - linha))
        return np.sum(X_)
    
    def minkowski_distance(_self,X, linha, p=2):
        X_ =  np.abs(X - linha) ** p
        return np.sum(X_,axis=1) ** (1/p)
    
    def cal_dist(_self,X, linha):
        if(_self.dist == 'euclidean'):
            return _self.dist_euclidiana(X, linha)
        if(_self.dist == 'manhattan'):
            return _self.manhattan_distance(X, linha)
        if(_self.dist == 'chebyshev'):
            return _self.chebyshev_distance(X, linha)
        if(_self.dist == 'minkowski'):
            return _self.minkowski_distance(X, linha)