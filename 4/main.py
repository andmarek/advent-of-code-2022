class DayFour:

    def foo():
        return None

class PartOne(DayFour):
    def __init__(self, data) -> None:
        super().__init__()
        self.data = data
        self.count = 0

    def solve(self):
        for assignments in data.split("\n"):
            sections = assignments.split(",")

            section_one = sections[0]
            section_two = sections[1]

            if self._does_fully_contain(section_one, section_two):
                self.count += 1
            

    def _does_fully_contain(self, section_one: str, section_two: str) -> bool:
        section_one_components = section_one.split("-")
        section_one_start = int(section_one_components[0])
        section_one_end = int(section_one_components[1])

        section_two_components = section_two.split("-")
        section_two_start = int(section_two_components[0])
        section_two_end = int(section_two_components[1])

        # Does section 2 overlap one?
        if (section_two_start <= section_one_start) \
        and (section_two_end >= section_one_end):
            return True
        
        # Does section 1 overlap two?
        elif (section_one_start <= section_two_start) \
        and (section_one_end >= section_two_end):
            return True
        else: return False

class PartTwo(DayFour):
    def __init__(self, data) -> None:
        super().__init__()
        self.data = data
        self.count = 0

    def solve(self):
        for assignments in data.split("\n"):
            sections = assignments.split(",")

            section_one = sections[0]
            section_two = sections[1]

            if self._does_overlap(section_one, section_two) == True:
                self.count += 1
            


    def _does_overlap(self, section_one: str, section_two: str) -> bool:
        section_one_components = section_one.split("-")
        section_one_start = int(section_one_components[0])
        section_one_end = int(section_one_components[1])

        section_two_components = section_two.split("-")
        section_two_start = int(section_two_components[0])
        section_two_end = int(section_two_components[1])

        section_one_range = range(section_one_start, section_one_end+1)
        section_two_range = range(section_two_start, section_two_end+1)

        
        s1s = set(section_one_range)
        inter = s1s.intersection(section_two_range)
        if len(inter) > 0:
            print("True")
            return True
        return False




with open("data", "r") as f:
    data = f.read()

    part_one = PartOne(data)
    part_one.solve()

    part_two = PartTwo(data)
    part_two.solve()
    
print("Part One answer: " + str(part_one.count))
print("Part Two answer: " + str(part_two.count))
