# coding: utf-8

import os
import sys
import json
import shutil
from pprint import pprint


def generate_json(top_path, obj_path):
    top_entry = top_path[top_path.rfind('\\') + 1:]

    dir_struct = {top_entry: []}

    for root, dirs, files in os.walk(top_path):
        rest = root[len(top_path):]
        keys = rest.split('\\')
        keys.remove('')

        cur_list = dir_struct[top_entry]
        for ind in keys:
            cur_list = cur_list[-1][ind]

        # add files first
        cur_list += files

        # add dirs, create empty list for each dir
        dict_obj = {}
        for entry in dirs:
            dict_obj[entry] = []
        cur_list.append(dict_obj)

    obj_path = obj_path + '\\' + top_path.replace('\\', '_') + '.json'
    pos = obj_path.rfind(':')
    obj_path = obj_path[:pos] + obj_path[pos + 1:]
    print obj_path
    with open(obj_path, 'wb') as f:
        json.dump(dir_struct, f)

    pprint(dir_struct)


def move_flat(top_path, dest_path):
    for root, dirs, files in os.walk(top_path):
        for file in files:
            shutil.copy(root + '\\' + file, dest_path + '\\' + file)


def main():
    top_path = sys.argv[1]
    dest_path = sys.argv[2]
    json_path = sys.argv[3]
    print top_path
    print dest_path
    print json_path
    move_flat(top_path, dest_path)
    generate_json(top_path, json_path)


if __name__ == '__main__':
    main()
