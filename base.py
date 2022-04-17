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