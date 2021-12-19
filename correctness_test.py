'''
test to check the correctness of the functions
for finding the minimum, maximum, addition and multiplication
'''

from task3 import *


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
    print(
        cleandoc(
            __doc__
        ) + '\npassed successfull'
    )
else:
    raise RuntimeError(
        cleandoc(
            __doc__
        ) +
        f'''
        failed,

        expected:
        {expected}

        get:
        {output}\
        '''.replace(" " * 4, "")
    )
