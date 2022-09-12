import csv
from functools import lru_cache


@lru_cache
def read(path):
    with open(path) as file:
        header, *data = csv.reader(file)

        result = []
        for array in data:
            line = {}
            for index, value in enumerate(array):
                line[header[index]] = value
            result.append(line)

    return result
