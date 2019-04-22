import os
import re
import sys
from datetime import datetime, timedelta

FORMAT = "%H:%M:%S,%f"


def open_file(file):
    with open(file, 'r', encoding='ISO-8859-1') as file:
        return file.read()


def save_file(file, _str):
    with open(file, 'w+', encoding='ISO-8859-1') as file:
        return file.write(_str)


def __fix(seconds=0, microseconds=0):
    return lambda line: ' --> '.join([(i + timedelta(seconds=seconds,
                                                     microseconds=microseconds)).strftime(FORMAT)[:-3]
                                      for i in [datetime.strptime(d, FORMAT)
                                                for d in line.split(' --> ')]])


def sync(fix_func, sub_file):
    sub_data = open_file(sub_file).split('\n')

    time_re = re.compile(r'\d{2}:\d{2}:\d{2},\d{3}')
    synced_sub = [(fix_func(line) if time_re.match(line) else line)
                  for line in sub_data]
    synced_sub_str = '\n'.join(synced_sub)

    save_file(sub_file, synced_sub_str)
    return 'Done!'


def get_offset(offset):
    offset = offset.replace('.', ',')
    
    if ',' in offset:
        aux = offset.split(',')
        seconds, micro = aux[0], aux[1]
        if '-' in offset:
            micro = '-' + micro
    else:
        seconds, micro = offset, '0'

    micro_size = len(micro.replace('-', ''))
    if micro_size < 6:
        micro += '0' * (6 - micro_size)

    return [int(i) for i in [seconds, micro]]


if __name__ == "__main__":
    file = sys.argv[1]
    seconds, micro = get_offset(sys.argv[2])

    print(f'Offsetting file {file} by {seconds} seconds and {micro} microseconds...')
    print(sync(__fix(seconds, micro), file))
