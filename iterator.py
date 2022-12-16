import csv
import re


class Iterator:
    def __init__(self, way_to_csv_file: str, name_class: str):
        self.name_class = name_class
        self.list = []
        self.way_to_file = way_to_csv_file
        self.counter = 0

        file = open(
            self.way_to_file, "r", encoding="utf-8")
        reader = csv.reader(file, delimiter="\t")
        for row in reader:
            self.list.append(row)

    def __iter__(self):
        return self

    def __next__(self) -> str:
        if self.counter < len(self.list):
            abs_way = re.split(";", str(self.list[self.counter]))
            self.counter += 1
            nc = self.name_class + "']"
            if abs_way[2] == nc:
                return abs_way[0][2:]
        else:
            raise StopIteration
