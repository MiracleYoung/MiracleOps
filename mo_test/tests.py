from django.test import TestCase

import os

def from_dir_get_files(dir: str):
    for item in os.walk(dir):
        if item[2]:
            for file in item[2]:
                yield os.path.join(item[0], file), item[0]


# if __name__ == '__main__':
#     for i in from_dir_get_files('/usr/local/src'):
#         print(i)