import csv

class CSVHandler:
    def __init__(self, filename):
        self.filename = filename

    def read_csv(self):
        data = []
        with open(self.filename, mode='r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                data.append(row)
        return data

    def overwrite_csv(self, data):
        with open(self.filename, mode='w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(data)
        print("CSV file has been written successfully.")
    def append_csv(self, data):
        with open(self.filename, 'a', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(data)
        
        print("CSV file has been appended successfully.")
    def read_csv_dict(self):
        data = []
        with open(self.filename, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                data.append(row)
        return data

    def write_csv_dict(self, data, fieldnames):
        with open(self.filename, mode='a', newline='') as file:
            csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
            csv_writer.writeheader()
            csv_writer.writerows(data)
        print("CSV file has been written successfully.")