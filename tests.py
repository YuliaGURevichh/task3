from inspect import cleandoc

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


def time():
    '''
    test to check the speed of the program
    when the size of the input file increases
    '''
