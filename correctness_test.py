'''
test to check the correctness of the functions
for finding the minimum, maximum, addition and multiplication
'''

from task3 import *


class CorrectnessError(Exception):
    pass

def main():
    Nums.file_name = 'little.txt'

    expected = cleandoc(
        '''
        minimal: 1
        maximal: 29
        product: 8841761993739701954543616000000
        sum: 435
        '''
    )

    output = Get.all(Nums.little)
    if output == expected:
        print(__doc__ + 'passed successfull'
        )
    else:

        raise CorrectnessError(
            __doc__ +
            f'''\
            failed,

            expected:
            {expected}

            get:
            {output}\
            '''.replace(" " * 4, "")
        )

if __name__ == "__main__":
    main()
