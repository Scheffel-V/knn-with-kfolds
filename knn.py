import csv
import Patient as PATIENT
import KnnClassifier as KNNCLASSIFIER
import KFolds as KFOLDS


def read_file():
    data_dictionary = {}

    data_file = open('diabetes.csv', 'r')
    spam_reader = csv.reader(data_file)

    attributes = spam_reader.__next__()

    for attribute in attributes:
        data_dictionary[attribute] = []

    for line in spam_reader:
        for i in range(0, 9):
            data_dictionary[attributes[i]].append(float(line[i]))

    return data_dictionary


def normalize_data_dictionary(data_dictionary):
    for attribute in data_dictionary.keys():
        attribute_max_value = max(data_dictionary[attribute])
        for i in range(0, len(data_dictionary[attribute])):
            data_dictionary[attribute][i] = data_dictionary[attribute][i] / attribute_max_value

    return data_dictionary


data_dict = normalize_data_dictionary(read_file())
patients = PATIENT.Patient.data_dictionary_to_patient_list(data_dict)
k_folds = KFOLDS.KFolds.patients_to_k_folds(patients, 20)

test_index = 1
training_k_folds = KFOLDS.KFolds.join_k_folds_excluding_one(k_folds, test_index)
test_k_fold = k_folds[test_index]

prediction = KNNCLASSIFIER.KnnClassifier.predict(training_k_folds, test_k_fold[0], 5)

print('Expected %d, Got %d.' % (training_k_folds[0].outcome, prediction))
