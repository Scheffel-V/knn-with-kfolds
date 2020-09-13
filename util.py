import csv


class Util:

    @staticmethod
    def read_file(filename):
        data_dictionary = {}

        data_file = open(filename, 'r')
        spam_reader = csv.reader(data_file)

        attributes = spam_reader.__next__()

        for attribute in attributes:
            data_dictionary[attribute] = []

        for line in spam_reader:
            for i in range(0, 9):
                data_dictionary[attributes[i]].append(float(line[i]))

        return data_dictionary

    @staticmethod
    def normalize_data_dictionary(data_dictionary):
        for attribute in data_dictionary.keys():
            attribute_max_value = max(data_dictionary[attribute])
            for i in range(0, len(data_dictionary[attribute])):
                data_dictionary[attribute][i] = data_dictionary[attribute][i] / attribute_max_value

        return data_dictionary
