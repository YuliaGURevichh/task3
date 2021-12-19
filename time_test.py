'''
test to check the speed of the program
when the size of the input file increases:
'''

from inspect import cleandoc
from decimal import Decimal
import timeit
from task3 import *


def b(num): # beautiful view of float num
    return str(Decimal(num))[:10]

nums_list=[
    Nums.str_big,
    Nums.str_little,
]

names = [
    'big.txt',
    'little.txt',
]

execution_time = []

for loop, nums in enumerate(nums_list):
    Nums.file_name = names[loop]
    start_time = timeit.default_timer()
    finding(nums)

    end_time = timeit.default_timer()
    execution_time.append(b(end_time - start_time))

print(
    __doc__ +
    '\n' +
    cleandoc(
        f'''
        with {names[0]} process ends in {execution_time[0]} seconds
        with {names[1]} process ends in {execution_time[1]} seconds
        difference: {
            b(abs(
                float(execution_time[0]) - float(execution_time[1])
            ))
        } seconds
        '''
    )
)
