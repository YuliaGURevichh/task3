from datetime import datetime
import decimal
from inspect import cleandoc
from decimal import Decimal
import time
from math import modf
import timeit


def finding(tested_object):
    '''
    test to check the correctness of the functions
    for finding the minimum, maximum, addition and multiplication
    '''
    expected = (
        'minimal: 1\n'
        'maximal: 29\n'
        'product: 8841761993739701954543616000000\n'
        'sum: 435'
    )
    output = tested_object
    answer = '\n' + cleandoc(finding.__doc__)
    if output == expected:
        answer += '\npassed successfull'
    else:
        answer += (f'''
            failed, expected:
            {expected}
            get:
            {output}
        '''.replace(" " * 12, ""))

    return answer

def b(num):
    return str(Decimal(num))[:10]

def timer(func_to_time_test, nums_list, names):
    '''
    test to check the speed of the program
    when the size of the input file increases:
    '''
    execution_time = []
    for nums in nums_list:
        start_time = timeit.default_timer()

        func_to_time_test(nums)

        end_time = timeit.default_timer()
        execution_time.append(b(end_time - start_time))
    return (
        '\n' +
        cleandoc(timer.__doc__) +
        '\n' +
        cleandoc(f'''
            with {names[0]} process ends in {execution_time[0]} seconds
            with {names[1]} process ends in {execution_time[1]} seconds
            difference: {b(abs(float(execution_time[0]) - float(execution_time[1])))} seconds
        ''')
    )
