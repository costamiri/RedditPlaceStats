import json
from typing import Dict

from base import PlaceStatistics


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
        with open("../output/color_count.json", "w") as output:
            json.dump(self.color_count, output, indent=4, sort_keys=True)


if __name__ == "__main__":
    # ColorCountStat("../raw_place_data/splitted/placedata02.txt").calculate()
    ColorCountStat("../raw_place_data/2022_place_canvas_history.csv").calculate()