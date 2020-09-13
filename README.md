# knn-with-kfolds

## Implementação da validação cruzada para avaliação de modelos de classificação

### Considerações sobre o programa

O programa foi desenvolvido na linguagem Python versão 3.8.4, e utiliza os módulo: 
1. numpy, para realizar o cálculo de desvio padrão.
2. tabulate, para formatar o texto em formato de tabela.

### Execução

Para executar o programa, basta estar na pasta raiz do repositório e executar o comando:
**py main.py**.

### Estrutura do código

O código está organizado em torno de 6 arquivos:
1. **main.py**: classe principal que utiliza das outras para rodar o algoritmo como um todo.
2. **patient.py**: classe auxiliar Patient, que guarda como atributos os valores de cada linha da tabela de dados fornecida como input.
3. **util.py**: classe estática auxiliar Util, utilizada para ler o arquivo de entrada e normalizar os valores.
4. **kfolds.py**: classe KFolds, utilizada para particionar os pacientes (linhas) em K-Folds, e também manipular esses K-Folds.
5. **knnclassifier.py**: classe KnnClassifier, utilizada para realizar a distância euclidiana, o método dos vizinhos mais próximos, as predições e o cross validation.
6. **statisticscalculator.py**: classe StatisticsCalculator, utilizada para calcular todas as estatísticas requeridas pelo trabalho, assim como transformá-las em uma tabela.
