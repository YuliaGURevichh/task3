from dataclasses import dataclass
from inspect import cleandoc
from math import prod
import os

if 'tests.py' in os.listdir():
    import tests
    TESTING = True
else:
    TESTING = False


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

    @staticmethod
    def file_name():
        if not Nums.file_name and TESTING:
            file_name = tests.Nums.file_name
        else:
            file_name = Nums.file_name
        if not file_name:
            file_name = 'unknown'
        return file_name

    def all(nums):
        return cleandoc(
            f'''
            minimal: {Get.min(nums)}
            maximal: {Get.max(nums)}
            product: {Get.prod(nums)}
            sum: {Get.sum(nums)}
            '''
        )

@dataclass
class Nums:
    def to_int(nums):
        return list(map(int, nums))

    file_name = None

    str_big = Get.nums('big.txt')
    str_little = Get.nums('little.txt')

    big = to_int(str_big)
    little = to_int(str_little)


def finding(nums_str):
    return (
        f'in file: {", ".join(nums_str)}\n' +
        Get.all(Nums.to_int(nums_str))
    )
