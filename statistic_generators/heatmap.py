import json
from typing import Dict

from PIL import Image

from base import PlaceStatistics


class Heatmap(PlaceStatistics):
    heatmap: Dict[int, Dict[int, int]]
    admin_rects: int

    def __init__(self, path):
        super().__init__(path)
        self.heatmap = {i: {j: 0 for j in range(2000)} for i in range(2000)}
        self.admin_rects = 0

    def procress_line(self, line: str):
        super().procress_line(line)
        _, _, _, *coords = line.split(",")
        if len(coords) != 2:
            self.admin_rects += 1
            return
        self.heatmap[int(coords[0].replace('"', ''))][int(coords[1].replace('"', ''))] += 1

    def save(self):
        with open("../output/heatmap_count.json", "w") as output:
            json.dump(self.heatmap, output, indent=4)

    @staticmethod
    def generate_image():
        with open("../output/heatmap_count.json", "r") as heat:
            heatmap = json.load(heat)
            img = Image.new("L", (2000, 2000))
            for row, cols in heatmap.items():
                for col, value in cols.items():
                    img.putpixel((int(row), int(col)), value)
            img.save("../output/heatmap.png", "PNG")


if __name__ == "__main__":
    # Heatmap("../raw_place_data/splitted/placedata02.txt").calculate()
    Heatmap("../raw_place_data/2022_place_canvas_history.csv").calculate()
    Heatmap.generate_image()
