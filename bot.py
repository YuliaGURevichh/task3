import requests
from bot_token import TOKEN
import python_version_test
import correctness_test
import time_test

def msg(text):
    chat_id = '-1001568249366'
    url = (
        'https://'
        'api.telegram.org'
        '/'
        f'{TOKEN}'
        '/'
        'sendMessage'
        '?'
        f'chat_id={chat_id}'
        '&'
        f'text={text}'
    )
    return requests.get(url, stream='True').content

try:
    python_version_test.main()
    correctness_test.main()
    time_test.main()
except python_version_test.VersionError as e:
    print(msg(e))
except correctness_test.CorrectnessError as e:
    print(msg(e))
except TimeoutError as e:
    print(msg(e))
else:
    print(msg('all ok'))
