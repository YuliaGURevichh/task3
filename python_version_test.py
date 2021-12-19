from sys import version_info
from inspect import cleandoc

required_version = '3.10.0 final'


version_info = list(version_info)[:4]
version_info = '.'.join(str(i) for i in version_info[:3])  + f' {version_info[-1]}'
if version_info == required_version:
    print('python version test passed\n')
else:
    raise SystemError(cleandoc(
            f'''
            wrong python version
            required: {required_version}
            your: {version_info}
            program may runs with errors
            '''
        )
    )
