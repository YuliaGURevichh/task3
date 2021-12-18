result = {
    True: 'passed successfull',
    False: 'failed',
}

def info(test, data):
    return (
        # gets docstrings of test function and removes tabs from it
        test.__doc__.replace('    ', '') +
        result[test(data)]
    )


def finding(tested_object):
    '''
    tests to check the correctness of the functions
    for finding the minimum, maximum, addition and multiplication
    '''
    return (tested_object ==
        'minimal: 1\n'
        'maximal: 29\n'
        'product: 8841761993739701954543616000000\n'
        'sum: 435')


def time():
    '''
    tests to check the speed of the program
    when the size of the input file increases
    '''