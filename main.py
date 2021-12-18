from dataclasses import dataclass
from math import prod
import os

TESTING = False
if 'tests.py' in os.listdir():
    import tests
    TESTING = True


def make_files():
    if 'little.txt' not in os.listdir():
        text = " ".join(str(i) for i in range(1, 30))
        file = open("little.txt", "w")
        file.write(text)

    if 'big.txt' not in os.listdir():
        text = " ".join(str(i) for i in range(1, 60))
        file = open("big.txt", "w")
        file.write(text)

make_files()

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

@dataclass
class Nums:
    def to_int(nums):
        return list(map(int, nums))

    filename = ""

    str_big = Get.nums('big.txt')
    str_little = Get.nums('little.txt')

    big = to_int(str_big)
    little = to_int(str_little)


def finding(nums_str):
    return (
        f'in file: {", ".join(nums_str)}\n' +
        Get.all(Nums.to_int(nums_str))
    )

def main():
    try:
        Nums.filename = 'little.txt'
        print(finding(Nums.str_little))

        if not TESTING:
            return

        print(
            tests.finding(
                Get.all(Nums.little)
            )
        )

        print(
            tests.timer(
                func_to_time_test=finding,
                nums_list=[
                    Nums.str_big,
                    Nums.str_little,
                ],
                names = [
                    'big.txt',
                    'little.txt',
                ]
            )
        )

    except (OverflowError , MemoryError):
        print(f'Too big numbers in {Nums.filename}. Please edit it.')


if __name__ == "__main__":
    main()
