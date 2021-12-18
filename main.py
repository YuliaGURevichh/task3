from dataclasses import dataclass
from math import prod
import os
TESTING = False
if 'tests.py' in os.listdir():
    import tests
    TESTING = True


@dataclass
class Get:
    def nums(file_name):
        return open(file_name, 'r').read().split()

    def min(nums):
        return min(nums)

    def max(nums):
        return max(nums)

    def sum(nums):
        return sum(nums)

    def prod(nums):
        return prod(nums)

    def all(nums):
        return (
            f'minimal: {Get.min(nums)}\n'
            f'maximal: {Get.max(nums)}\n'
            f'product: {Get.prod(nums)}\n'
            f'sum: {Get.sum(nums)}'
        )

def make_files():
    if 'little.txt' not in os.listdir():
        text = " ".join(str(i) for i in range(1, 30))
        file = open("little.txt", "w")
        file.write(text)

    if 'big.txt' not in os.listdir():
        text = " ".join(str(i) for i in range(1, 60))
        file = open("big.txt", "w")
        file.write(text)

def main(file_name):
    try:
        make_files()
        nums = Get.nums(file_name)
        print(f'in file: {", ".join(nums)}\n')
        nums = list(map(int, nums))
        print(Get.all(nums))

        if not TESTING:
            return



    except (OverflowError, MemoryError):
        print(f'Too big numbers in {file_name}. Please edit it.')


if __name__ == "__main__":
    main(file_name="little.txt")
