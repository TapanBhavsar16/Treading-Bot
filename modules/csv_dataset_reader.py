import csv

from modules.dataset_reader import DatasetReader

class CsvDatasetReader(DatasetReader):
    def __init__(self):
        pass
    
    def read_file(self, file):
        with open(file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            return list(reader)
