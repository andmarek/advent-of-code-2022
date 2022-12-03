from typing import List
import string

class DayThree:
    def calc_priority(self, letter):
        return string.ascii_letters.index(letter) + 1

class PartOne(DayThree):
    def __init__(self) -> None:
        self.priority = 0

    def _get_common_element(self, a: List[str], b: List[str]):
        common_elements = list(set(a).intersection(b))
        if common_elements:
            return common_elements[0]

    def solve(self):
        with open("data", "r") as f:
            rucksacks_str = f.read()
            rucksacks_arr = rucksacks_str.split("\n")

            for rucksack in rucksacks_arr:
                l = len(rucksack)
                half_rucksack = int(l/2)
                first_compartment = rucksack[0:(half_rucksack)]
                second_compartment = rucksack[(half_rucksack):].strip()

                common_element = self._get_common_element(first_compartment, second_compartment)
                if common_element:
                    priority = self.calc_priority(common_element)
                self.priority += priority
        
class PartTwo(DayThree):
    def __init__(self) -> None:
        self.priority = 0

    def _get_common_element(self, a: List[str], b: List[str], c: List[str]):
        common_elements_a_b = list(set(a).intersection(b))
        if common_elements_a_b:
            common_elements_a_b_c = list(set(common_elements_a_b).intersection(c))
            if common_elements_a_b_c:
                return list(common_elements_a_b_c)[0]

    def solve(self):
        with open("data", "r") as f:
            rucksacks_str = f.read()
            rucksacks_arr = rucksacks_str.split("\n")
            for i in range(0, len(rucksacks_arr), 3):
                first_of_group = rucksacks_arr[i]
                second_of_group = rucksacks_arr[i+1]
                third_of_group = rucksacks_arr[i+2]

                common_elemnt = self._get_common_element(first_of_group, second_of_group, third_of_group)
                if common_elemnt:
                    self.priority += self.calc_priority(common_elemnt)
            
with open("data", "r") as f:
    data_str = f.read()
    data_arr = rucksacks_str.split("\n")

part_one = PartOne(data_arr)
part_one.solve()
print(f"Part One answer: {part_one.priority}")

part_two = PartTwo()
part_two.solve()
print(f"Part Two answer: {part_two.priority}")
