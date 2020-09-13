import numpy
from tabulate import tabulate


class Statistics:
    def __init__(self, iterations_statistics, accuracy_mean, accuracy_standard_deviation, f1_measure_mean, f1_measure_standard_deviation):
        self.iterations_statistics = iterations_statistics
        self.accuracy_mean = accuracy_mean
        self.accuracy_standard_deviation = accuracy_standard_deviation
        self.f1_measure_mean = f1_measure_mean
        self.f1_measure_standard_deviation = f1_measure_standard_deviation


def accuracy_std(results):
    accuracy_list = []

    for result in results:
        accuracy_list.append(result[0])

    return numpy.std(accuracy_list)


def f1_measure_std(results):
    f1_measure_list = []

    for result in results:
        f1_measure_list.append(result[1])

    return numpy.std(f1_measure_list)


def get_results_statistics(results):
    true_positives = 0
    true_negatives = 0
    false_negatives = 0
    false_positives = 0

    for result in results:
        if result.got == 1:
            if result.expected == 1:
                true_positives = true_positives + 1
            else:
                false_positives = false_positives + 1
        else:
            if result.expected == 1:
                false_negatives = false_negatives + 1
            else:
                true_negatives = true_negatives + 1

    acc = (true_positives + true_negatives) / len(results),
    rec = true_positives / (true_positives + false_negatives)
    prec = true_positives / (true_positives + false_positives)

    # Utilizando beta = 1
    return acc, 2 * ((prec * rec) / (prec + rec))


class StatisticsCalculator:

    @staticmethod
    def get_statistics(results_per_iterations):
        iterations_statistics = []

        # Para cada iteração, calcular as estatisticas de Acurácia e F1-Measure.
        # O retorno será adicionado na lista das estatisticas para cada iteração.
        # Ele é composto de tuplas na forma (acurácia, F1-Measure)
        for results in results_per_iterations:
            iterations_statistics.append(get_results_statistics(results))

        # É calculado a média total da acurácia:
        accuracy_median = sum(result[0] for result in iterations_statistics) / len(iterations_statistics)

        # É calculado a média total da F1-Measure:
        f1_measure_median = sum(result[1] for result in iterations_statistics) / len(iterations_statistics)

        # É calculado o desvio padrão da acurácia:
        accuracy_standard_deviation = accuracy_std(iterations_statistics)

        # É calculado o desvio padrão da F1-Measure:
        f1_measure_standard_deviation = f1_measure_std(iterations_statistics)

        # Os valores são colocados no objeto Statistics.
        statistics = Statistics(iterations_statistics, accuracy_median, accuracy_standard_deviation, f1_measure_median,
                                f1_measure_standard_deviation)

        return statistics

    @staticmethod
    def statistics_to_table(statistics):
        data_list = []
        iterations_length = len(statistics.iterations_statistics)

        for i in range(iterations_length):
            data_list.append([i + 1, statistics.iterations_statistics[i][0], statistics.iterations_statistics[i][1]])

        data_list.append(
            ["Média (n = " + str(iterations_length) + ")", statistics.accuracy_mean, statistics.f1_measure_mean])
        data_list.append(
            ["Desvio Padrão", statistics.accuracy_standard_deviation, statistics.f1_measure_standard_deviation])

        return tabulate(data_list, headers=['Fold de Teste / Iteração', 'Acurácia', 'F1-Measure'])
