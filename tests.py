from dataclasses import dataclass
from inspect import cleandoc
from decimal import Decimal
import timeit
import sys


@dataclass
class Nums:
    file_name = None


def finding(tested_object):
    '''
    test to check the correctness of the functions
    for finding the minimum, maximum, addition and multiplication
    '''

    Nums.file_name = 'little.txt'

    expected = cleandoc(
        '''
        minimal: 1
        maximal: 29
        product: 8841761993739701954543616000000
        sum: 435
        '''
    )

    output = tested_object
    answer = '\n' + cleandoc(finding.__doc__)
    if output == expected:
        answer += '\npassed successfull'
    else:
        answer += (
            f'''
            failed,

            expected:
            {expected}

            get:
            {output}\
            '''.replace(" " * 12, "")
        )

    return answer


def b(num): # beautiful view of float num
    return str(Decimal(num))[:10]


def timer(func_to_time_test, nums_list, names):
    '''
    test to check the speed of the program
    when the size of the input file increases:
    '''
    execution_time = []

    for loop, nums in enumerate(nums_list):
        Nums.file_name = names[loop]
        start_time = timeit.default_timer()
        func_to_time_test(nums)

        end_time = timeit.default_timer()
        execution_time.append(b(end_time - start_time))

    return (
        '\n' +
        cleandoc(timer.__doc__) +
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


def python_version():
    '''
    any other test at my discretion
    '''
    version_info = list(sys.version_info)[:4]
    version_info = '.'.join(str(i) for i in version_info[:3])  + f' {version_info[-1]}'
    if version_info == '3.10.0 final':
        print('python version test passed\n')
    else:
        print(
            cleandoc(
                f'''
                wrong python version
                required: 3.10.0 final
                your: {version_info}
                program may runs with errors
                '''
            ) + '\n'
        )
