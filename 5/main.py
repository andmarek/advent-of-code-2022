class DayThree:

    def foo():
        return None

class PartOne(DayThree):
    def __init__(self, data) -> None:
        super().__init__()
        self.data = data

    def solve(self):
        print(data)

with open("data", "r") as f:
    data = f.read()

    part_one = PartOne(data)
    part_one.solve()

print(f"Part One answer: {part_one.priority}")