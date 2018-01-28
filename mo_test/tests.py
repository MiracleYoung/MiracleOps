from django.test import TestCase

import os


def from_dir_get_files(dir: str):
    for item in os.walk(dir):
        if item[2]:
            for file in item[2]:
                yield os.path.join(item[0], file), item[0]


def get_tree(path='.', depth=0):
    _tree = ''
    def inner(path, depth):
        nonlocal _tree
        if depth == 0:
            _tree += 'root:[' + path + ']'

        for item in os.listdir(path):
            if item not in ('.git', '.idea', 'migrations', '__pycache__'):
                _line = "|\t" * depth + "+--" + item + '\n'
                print(_line)
                _tree += _line
                _newitem = path + '/' + item
                if os.path.isdir(_newitem):
                    inner(_newitem, depth + 1)
        return _tree

    return inner(path, depth)


if __name__ == '__main__':
    print(get_tree('../asset'))
