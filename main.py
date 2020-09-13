from util import Util
from patient import Patient
from kfolds import KFolds
from statisticscalculator import StatisticsCalculator
from knnclassifier import KnnClassifier


K_FOLDS = 10
K_NEIGHBORS = 5

# PASSO 1: Lendo do arquivo e normalizando os valores:
data_dictionary = Util.read_file('diabetes.csv')
normalized_data_dictionary = Util.normalize_data_dictionary(data_dictionary)

# PASSO 2: O código deve realizar a divisão dos dados originais em k folds de forma estratificada.
#          O valor K a ser utilizado é o que está na variável K_FOLDS.
patients = Patient.data_dictionary_to_patient_list(normalized_data_dictionary)
k_folds_aux = KFolds.patients_to_k_folds(patients, K_FOLDS)

# PASSO 3: Iterativamente treinar um modelo utilizando k-1 folds e testá-lo no fold restante,
#          variando o fold de teste a cada repetição deste processo. O retorno do método de
#          treino dos modelos é uma lista dos resultados de cada iteração - cada modelo.
#          O valor K de vizinhos a ser utilizado é o que está na variável K_NEIGHBORS.
results_per_iteration = KnnClassifier.k_fold_cross_validation(k_folds_aux, K_NEIGHBORS)

# PASSO 4: A cada teste realizado, deverão ser calculadas e armazenadas as medidas de acurácia e F1-measure.
final_statistics = StatisticsCalculator.get_statistics(results_per_iteration)

# PASSO 5: Os valores são colocados em um formato de tabela a partir do objeto Statistics.
table = StatisticsCalculator.statistics_to_table(final_statistics)

# PASSO 6: Saída do programa.
print(table)
f = open("output.txt", "a")
f.write(table)
f.close()