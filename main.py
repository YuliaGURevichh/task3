from task3 import *

if 'tests.py' in os.listdir():
    import tests
    TESTING = True
    tests.python_version()
else:
    TESTING = False


def main():
    try:
        Nums.file_name = 'little.txt'
        print(finding(Nums.str_little))

        if not TESTING:
            return

        Nums.file_name = None

        print(
            tests.finding(
                Get.all(Nums.little)
            )
        )

        print(
            tests.timer(
                func_to_time_test=finding,
                nums_list=[
                    Nums.str_big,
                    Nums.str_little,
                ],
                names = [
                    'big.txt',
                    'little.txt',
                ]
            )
        )

    except (OverflowError , MemoryError):
        print(
            f'Too big numbers in {Get.file_name()}.'
            'Please edit it.'
        )


if __name__ == "__main__":
    main()
