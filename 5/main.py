class DayFive:

    def foo():
        return None

class PartOne(DayFive):
    def __init__(self, data) -> None:
        super().__init__()
        self.data = data

    def solve(self):
        print(data)

with open("data", "r") as f:
    data = f.read()

    part_one = PartOne(data)
    solution = part_one.solve()
    

print("Part One answer: " + solution)