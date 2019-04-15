# Lista de Exercícios 05

Nesta lista vamos fazer a predição para obter o preço de venda de um imóvel a partir do seguinte dataset "[Boston House Price Dataset](https://www.google.com/url?q=https%3A%2F%2Farchive.ics.uci.edu%2Fml%2Fmachine-learning-databases%2Fhousing%2Fhousing.data&sa=D&sntz=1&usg=AFQjCNEke-pt5MM0sLtzR9aSXgkHVT_K8A)". Informações detalhadas sobre o dataset podem ser obtidas no [seguinte link](https://www.google.com/url?q=https%3A%2F%2Farchive.ics.uci.edu%2Fml%2Fmachine-learning-databases%2Fhousing%2Fhousing.names&sa=D&sntz=1&usg=AFQjCNGCmwFf8uUyRkfSExJ7seLiHZMDOw). Use 70% dos dados para treino e outros 30% para teste.

1. Use 70% dos dados para treino e outros 30% para teste.
2. Crie modelos de aprendizado de máquina  usando os seguintes algoritmos:
    + [Regressão Linear com Gradiente Descendente](https://gist.github.com/regispires/e5847329a1c0b75b944434367e7d5089) (implemente em um módulo Python externo ao Jupyter Notebook.
    + [Linear Regression do Scikit-Learn ](https://www.google.com/url?q=https%3A%2F%2Fscikit-learn.org%2Fstable%2Fmodules%2Fgenerated%2Fsklearn.linear_model.LinearRegression.html&sa=D&sntz=1&usg=AFQjCNF5YpX-NcRPr9PfEHySe3XfI19lBQ)
    + [Stochastic Gradient Descent Regressor (SGDRegressor) do Scikit-Learn](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html)
3. Compare os resultados obtidos entre os algoritmos acima usando a métrica RMSE (implemente-a em um módulo Python externo ao Jupyter Notebook).
    + Compare também os resultados usando os seguintes escalonamentos de features: Normalização e Standardization (implemente-os em um módulo Python externo ao Jupyter Notebook).
        + Mais informações em: http://sebastianraschka.com/Articles/2014_about_feature_scaling.html