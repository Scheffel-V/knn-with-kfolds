import math

class KnnClassifier:
    def __init__(self, patients, n_value):
        self.patients = patients
        self.nValue = n_value

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
    def get_neighbors(train_patients, test_patient, neighbors_number):
        distances = []

        for train_patient in train_patients:
            dist = KnnClassifier.euclidean_distance(test_patient, train_patient)
            distances.append((train_patient, dist))

        distances.sort(key=lambda tup: tup[1])
        neighbors = []

        for i in range(neighbors_number):
            neighbors.append(distances[i][0])

        return neighbors

    @staticmethod
    def predict(train_patients, test_row, neighbors_number):
        neighbors = KnnClassifier.get_neighbors(train_patients, test_row, neighbors_number)
        output_values = [patient.outcome for patient in neighbors]
        prediction = max(set(output_values), key=output_values.count)

        return prediction
