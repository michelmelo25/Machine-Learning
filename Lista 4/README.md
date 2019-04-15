# Lista de Exercícios 04 

Nesta lista vamos fazer a predição para saber se um tumor de mama é benigno ou maligno a partir do seguinte dataset "[Wisconsin Diagnostic Breast Cancer (WDBC)](https://www.google.com/url?q=https%3A%2F%2Farchive.ics.uci.edu%2Fml%2Fmachine-learning-databases%2Fbreast-cancer-wisconsin%2Fwdbc.data&sa=D&sntz=1&usg=AFQjCNHGQiH_ahI6h2kbhF2AnFRjnXo7nQ)". Informações detalhadas sobre o dataset podem ser obtidas no [seguinte link](https://www.google.com/url?q=https%3A%2F%2Farchive.ics.uci.edu%2Fml%2Fmachine-learning-databases%2Fbreast-cancer-wisconsin%2Fwdbc.names&sa=D&sntz=1&usg=AFQjCNH7eKkmqe3M3TJAUFwZG9Gt1uZCCQ). 

1. Use 70% dos dados para treino e outros 30% para teste.

2. Crie modelos de aprendizado de máquina  usando os seguintes algoritmos:
    + [Perceptron (mesmo usado na Lista 03)](https://gist.github.com/regispires/8607f019ac4264c9de8412b172b0d0d7)
    + [Adaline com Gradiente Descendente (mesmo usado na Lista 03)](https://gist.github.com/regispires/acf2b070d243de7a2bd3308cf1c8e821)
    + Adaline com  [Gradiente Descentente Estocástico](https://gist.github.com/regispires/03c1f96458a239314cfc6385fe12e9ac)
    + Adaline com Gradiente Descendente Estocástico usando mini-batches de 20 elementos (mesmo do item anterior, mas agora com mini-batch).
        + Dica: Use partial_fit (aprendizado online) para fazer o aprendizado a cada 20 amostras do dataset de treino (mini-batch).
    + [Perceptron do Scikit Learn](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Perceptron.html)
    + [Stochastic Gradient Descent (SGD) do Scikit Learn](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html)
    + [Logistic Regression do Scikit Learn](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)
Compare os resultados obtidos entre os algoritmos acima usando a métrica acurácia.