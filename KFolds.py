class KFolds:

    @staticmethod
    def patients_to_k_folds(patients, k_value):
        k_folds = {}

        for i in range(0, k_value):
            k_folds[i] = []

        fold_index_positive = 0
        fold_index_negative = 0

        for patient in patients:
            if patient.is_positive():
                k_folds[fold_index_positive].append(patient)
                fold_index_positive = fold_index_positive + 1

                if fold_index_positive == k_value:
                    fold_index_positive = 0
            else:
                k_folds[fold_index_negative].append(patient)
                fold_index_negative = fold_index_negative + 1

                if fold_index_negative == k_value:
                    fold_index_negative = 0

        return k_folds

    @staticmethod
    def join_k_folds_excluding_one(k_folds, excluded_index):
        k_folds_joined_list = []

        for i in range(len(k_folds)):
            if i != excluded_index:
                k_folds_joined_list = k_folds_joined_list + k_folds[i]

        return k_folds_joined_list
