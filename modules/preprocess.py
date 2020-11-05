class Preprocess:
    def __init__(self):
        pass
    
    def filter_data(self, data, *column_names):
        return [[element[column_name] for column_name in column_names] for element in data]
