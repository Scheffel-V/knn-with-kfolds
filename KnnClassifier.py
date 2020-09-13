import math
from kfolds import KFolds


class Result:
    def __init__(self, expected, got):
        self.expected = expected
        self.got = got


class KnnClassifier:

    @staticmethod
    def euclidean_distance(first_patient, second_patient):
        distance = 0.0

        distance += (first_patient.pregnancies - second_patient.pregnancies) ** 2
        distance += (first_patient.glucose - second_patient.glucose) ** 2
        distance += (first_patient.bloodPressure - second_patient.bloodPressure) ** 2
        distance += (first_patient.skinThickness - second_patient.skinThickness) ** 2
        distance += (first_patient.insulin - second_patient.insulin) ** 2
        distance += (first_patient.BMI - second_patient.BMI) ** 2
        distance += (first_patient.diabetesPedigreeFunction - second_patient.diabetesPedigreeFunction) ** 2
        distance += (first_patient.age - second_patient.age) ** 2

        return math.sqrt(distance)

    @staticmethod
    def get_neighbors(training_patients, test_patient, neighbors_number):
        distances = []

        for train_patient in training_patients:
            dist = KnnClassifier.euclidean_distance(test_patient, train_patient)
            distances.append((train_patient, dist))

        distances.sort(key=lambda tup: tup[1])
        neighbors = []

        for i in range(neighbors_number):
            neighbors.append(distances[i][0])

        return neighbors

    @staticmethod
    def predict(training_patients, testing_patients, neighbors_number):
        results = []
        
        for testing_patient in testing_patients:
            neighbors = KnnClassifier.get_neighbors(training_patients, testing_patient, neighbors_number)
            output_values = [patient.outcome for patient in neighbors]
            prediction = max(set(output_values), key=output_values.count)

            testing_patient.prediction = prediction

            results.append(Result(testing_patient.outcome, prediction))

        print("RESULTS LENGTH:" + str(len(results)))
        return results

    @staticmethod
    def k_fold_cross_validation(k_folds, k_neighbors):
        results_for_each_permutation = []

        # Iterativamente treinar um modelo:
        for i in range(len(k_folds)):
            test_fold_index = i
            # Utilizando k-1 folds de treino e 1 de teste, variando o fold de teste a cada repetição.
            training_k_folds = KFolds.join_k_folds_excluding_one(k_folds, test_fold_index)
            test_k_fold = k_folds[test_fold_index]

            # Treinamento e resultados desta iteração:
            knn_results = KnnClassifier.predict(training_k_folds, test_k_fold, k_neighbors)

            # Os resultados desta iteração são adicionados na lista:
            results_for_each_permutation.append(knn_results)

        return results_for_each_permutation
