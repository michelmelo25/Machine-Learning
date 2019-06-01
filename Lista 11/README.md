#Lista 11
-  O [dataset de renda de americanos dos Estados Unidos](https://www.google.com/url?q=https%3A%2F%2Farchive.ics.uci.edu%2Fml%2Fdatasets%2FAdult&sa=D&sntz=1&usg=AFQjCNFwLJllpmdZIOWlRLLkk_9ZSNZKqQ) tem como rótulo se a pessoa ganha ou não mais de 50.000 dólares por ano.
    -   O dataset contém dados categóricos e valores faltando.
    -   Faça o melhor pre-processamento possível para tornar tal dataset adequado para uso em diversos algoritmos de aprendizagem de máquina.
    -   Faça atribuição da média da coluna para valores faltantes, caso o percentual de valores faltantes da coluna não seja muito grande.
    -   Transforme categorias usadas nas features e label em números. Categorias que não possuem uma ordem implícita devem ser transformadas em features binárias.
-   Use **5-Fold Cross Validation Estratificada** para obter a **Accuracy** através do uso dos seguintes algoritmos: Perceptron, Adaline, [Stochastic Gradient Descent (SGD)](https://www.google.com/url?q=https%3A%2F%2Fscikit-learn.org%2Fstable%2Fmodules%2Fgenerated%2Fsklearn.linear_model.SGDClassifier.html&sa=D&sntz=1&usg=AFQjCNHNizufqsePtlkU73O8H1xFJ8YPvw), Logistic Regression, kNN, Naive Bayes, SVM e [Árvore de Decisão (Decision Tree)](https://www.google.com/url?q=https%3A%2F%2Fscikit-learn.org%2Fstable%2Fmodules%2Fgenerated%2Fsklearn.tree.DecisionTreeClassifier.html&sa=D&sntz=1&usg=AFQjCNEUbQwnKReDZGb8C8jKYm7m2RxfZw).
    -   Faça Standardization dos dados (fit para o conjunto de treino e transform para treino e teste).
    -   Compare os modelos e indique o melhor resultado obtido.

