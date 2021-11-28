import json
import pandas as pd
from pandas.core.frame import DataFrame

JSON_RESPONSE_FILE_NAME = 'response.json'

def get_json_content(file_name):
    with open(file_name, 'r') as f:
        lines = f.read()

    return lines

def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out

def main():
    lines = get_json_content(JSON_RESPONSE_FILE_NAME)
    content = json.loads(lines)
    #[print('{0}: {1}'.format(result['stock']['symbol'], result['quantity'])) for result in content['results']]
    [print(result['book_value']) for result in content['results']]

if __name__ == '__main__':
    main()