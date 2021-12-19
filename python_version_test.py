'''
any other test at my discretion
'''

import sys
from inspect import cleandoc

class VersionError(Exception):
    pass


def main():
    required_version = '3.10.0 final'


    version_info = list(sys.version_info)[:4]
    version_info = '.'.join(str(i) for i in version_info[:3])  + f' {version_info[-1]}'
    if version_info == required_version:
        print('python version test passed\n')
    else:
        raise VersionError(cleandoc(
                f'''
                wrong python version
                required: {required_version}
                your: {version_info}
                program may runs with errors
                '''
            )
        )


if __name__ == "__main__":
    main()
