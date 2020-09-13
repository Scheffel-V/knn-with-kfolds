class Patient:
    def __init__(self, pregnancies, glucose, blood_pressure, skin_thickness, insulin, BMI, diabetes_pedigree_function, age, outcome):
        self.pregnancies = pregnancies
        self.glucose = glucose
        self.bloodPressure = blood_pressure
        self.skinThickness = skin_thickness
        self.insulin = insulin
        self.BMI = BMI
        self.diabetesPedigreeFunction = diabetes_pedigree_function
        self.age = age
        self.outcome = outcome
        self.prediction = -1

    def is_positive(self):
        return self.outcome == 1

    def is_negative(self):
        return self.outcome == 0

    def __str__(self):
        return 'Pregnancies:' + str(self.pregnancies) + ', Glucose:' + str(self.glucose) + ', BloodPressure:' + str(self.bloodPressure) + ', SkinThickness:' + str(self.skinThickness) + ', Insulin:' + str(self.insulin) + ', BMI:' + str(self.BMI) + ', DiabetesPedigreeFunction:' + str(self.diabetesPedigreeFunction) + ', Age:' + str(self.age) + ', Outcome:' + str(self.outcome)

    @staticmethod
    def data_dictionary_to_patient_list(data_dictionary):
        patient_list = []

        for i in range(0, len(data_dictionary['Outcome'])):
            patient_list.append(Patient(data_dictionary['Pregnancies'][i],
                                        data_dictionary['Glucose'][i],
                                        data_dictionary['BloodPressure'][i],
                                        data_dictionary['SkinThickness'][i],
                                        data_dictionary['Insulin'][i],
                                        data_dictionary['BMI'][i],
                                        data_dictionary['DiabetesPedigreeFunction'][i],
                                        data_dictionary['Age'][i],
                                        data_dictionary['Outcome'][i]))

        return patient_list

    @staticmethod
    def how_many_positives_in_patient_list(patient_list):
        positives_count = 0

        for patient in patient_list:
            if patient.is_positive():
                positives_count = positives_count + 1

        return positives_count

    @staticmethod
    def how_many_negatives_in_patient_list(patient_list):
        negatives_count = 0

        for patient in patient_list:
            if patient.is_negative():
                negatives_count = negatives_count + 1

        return negatives_count
