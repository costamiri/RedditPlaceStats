import json
from typing import Dict


class PlaceStatistics:
    file_path: str
    line_count: int

    def __init__(self, path):
        self.file_path = path
        self.line_count = 0

    def calculate(self):
        self.process_file()
        self.output()
        self.save()

    def process_file(self):
        with open(self.file_path, "r") as file:
            file.readline()  # header
            while line := file.readline():
                self.procress_line(line)

    def procress_line(self, line: str):
        self.line_count += 1
        if self.line_count % 1_000_000 == 0:
            print(self.line_count)

    def output(self):
        print(f"Line Count: {self.line_count}")

    def save(self):
        pass


class ColorCountStat(PlaceStatistics):
    color_count: Dict[str, int]

    def __init__(self, path):
        super().__init__(path)
        self.color_count = {}

    def procress_line(self, line: str):
        super().procress_line(line)
        color = line.split(",")[2]
        if color not in self.color_count:
            self.color_count[color] = 0
        self.color_count[color] += 1

    def save(self):
        with open("output/color_count.json", "w") as output:
            json.dump(self.color_count, output, indent=4, sort_keys=True)


if __name__ == "__main__":
    # ColorCountStat("raw_place_data/splitted/placedata02.txt").calculate()
    ColorCountStat("raw_place_data/2022_place_canvas_history.csv").calculate()