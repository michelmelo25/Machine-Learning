**Lista de Exercícios 12** (prazo final para entrega: 16/06/2019 - DOMINGO - Não é necessário enviar ao professor - Correção na segunda dia 17/06/2019)

1.  Avalie o desempenho dos algoritmos **DecisionTree, RandomForest** e **Gradient Boosting** para o dataset "[Wisconsin Diagnostic Breast Cancer (WDBC)](https://www.google.com/url?q=https%3A%2F%2Farchive.ics.uci.edu%2Fml%2Fmachine-learning-databases%2Fbreast-cancer-wisconsin%2Fwdbc.data&sa=D&sntz=1&usg=AFQjCNHGQiH_ahI6h2kbhF2AnFRjnXo7nQ)". Separe os dados em treino (60%), validação (20%) e teste (20%).
    -   Use um valor constante para o parâmetro **random_state** e teste os resultados com as seguintes combinações de hiper-parâmetros para RandomForest e Gradient Boosting usando Grid-Search:
        -   **learning_rate**: 0.1, 0.05, 0.01 (somente para o Gradient Boosting)
        -   **n_estimators**: 50, 100, 200
        -   **max_depth**: 3, 5, 7
    -   Mostre a **importância das features** de acordo com o **melhor modelo de classificação** e o **melhor modelo de regressão** encontrados dentre os 3 usados nesta lista de exercícios (DecisionTree, RandomForest e Gradient Boosting).
2.  Faça a clusterização do [dataset deste link](https://www.google.com/url?q=https%3A%2F%2Fraw.githubusercontent.com%2Fdatascienceinc%2Flearn-data-science%2Fmaster%2FIntroduction-to-K-means-Clustering%2FData%2Fdata_1024.csv&sa=D&sntz=1&usg=AFQjCNGg5vN2BMv1UVO3GsfzbkIzjqUm2g) usando o algoritmo K-Means++.
    -   O dataset possui os seguintes dados de motoristas: a distância média dirigida por dia e a média percentual do tempo que um motorista estava 5mph acima do limite de velocidade.
    -   Portanto, agrupe os motoristas pela similaridade das features acima.
    -   Use o método do cotovelo (Elbow Method) para identificar o melhor valor de k para o K-Means++.
    -   Mostre o resultado graficamente.
3.  Use Clusterização Hierárquica no mesmo dataset da questão 2 usando "complete" como critério de ligação (linkage). Mostre o dendograma.
    -   Use o parâmetro n_clusters da função scipy.cluster.hierarchy.cut_tree para obter o número de clusters igual ao melhor resultado obtido com o K-Means (Questão 2). Exemplo:

...

distance_matrix = scipy.spatial.distance.pdist(X, metric='euclidean')

cluster_model = scipy.cluster.hierarchy.complete(distance_matrix)

dendogram = scipy.cluster.hierarchy.dendrogram(cluster_model)

sensor_cluster_list = scipy.cluster.hierarchy.cut_tree(cluster_model, n_clusters=8)

-   Mostre o resultado graficamente.

4. Use o [DBScan](https://www.google.com/url?q=https%3A%2F%2Fscikit-learn.org%2Fstable%2Fmodules%2Fgenerated%2Fsklearn.cluster.DBSCAN.html&sa=D&sntz=1&usg=AFQjCNFS7U5IBgY5pf1qZNFfnoybRQG6dA) para clusterizar o mesmo dataset da questão 2 e mostre o resultado graficamente.
